#include "Database_Operations.h"
#include "MasterFileIO.h"
#include "IndexTableRAM.h"
#include "TrashIO.h"
#include "SlaveIO.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define SLAVE_FILENAME_DB "./Slave.fl"
#define MEMORY_DATABASE_OPERATIONS -1002
#define STRING_PARSING_ERROR_DB_OPER -2000

int stringToInt(char* stringToConvert) {
	char* end = NULL; //for strtol()
	int intValue = (int)strtol(stringToConvert, &end, 10);
	if (intValue == LONG_MAX || intValue == LONG_MIN || *end != '\0') {
		printf("Something wrong with parsing the string...");
		exit(STRING_PARSING_ERROR_DB_OPER);
	}
	return intValue;
}

Date* getDateFromInput(char* newValue) {
	size_t y, m, d;
	int code = sscanf_s(newValue, "%d-%d-%d", &y, &m, &d);
	if (code == EOF || code == 0 || code == -1) {
		printf("Something is wrong with the date....");
		exit(STRING_PARSING_ERROR_DB_OPER);
	}
	Date date = { y, m, d };
	return &date;
}

void insert_m(MasterFileStruct* masterEntry, size_t whereToInsertMasterEntry, size_t* sizeOfMaster, IndexTableEntry** indexEntries, size_t* indexTableSize) {
	// write row to master
	writeRowToMaster(masterEntry, whereToInsertMasterEntry);
	// printf("Check what we inserted in master: \n");
	// printMasterRow(getRowFromMaster(whereToInsertMasterEntry));

	// add memory for new index entry
	IndexTableEntry* ptr = realloc(*(indexEntries), sizeof(IndexTableEntry) * (*(indexTableSize) + 1));
	if (ptr == NULL) exit(MEMORY_DATABASE_OPERATIONS);
	*(indexEntries) = ptr;
	
	// create new entry
	IndexTableEntry newIndexEntry = { masterEntry->docInfo.uuid, whereToInsertMasterEntry };
	// add it to the end of the array
	int length = *(indexTableSize);
	*((*indexEntries) + length) = newIndexEntry;
	
	// printf("Check index after inserting new index entry: \n");
	// printIndexEntries(*(indexEntries), *(indexTableSize) + 1);
	
	// actually increase the size of array 
	*(indexTableSize) += 1;
	*sizeOfMaster += 1;
	
	//sort
	// printf("Check index after sorting: \n");
	sortEntriesById(*(indexEntries), *(indexTableSize));
 //	printIndexEntries(*(indexEntries), *(indexTableSize));
}

MasterRowEntryPair get_m(IndexTableEntry* indexEntries, size_t id, size_t indexSize) {
	if (id == 0) {
		printAllMasterEntries();
		MasterRowEntryPair pair = {NULL, -1};
		return pair;
	}
	else {
		size_t rowNumberMaster = getRowNumberById(indexEntries, id, indexSize);
		if (rowNumberMaster == -1) {
			MasterRowEntryPair pair = { NULL, -1 };
			return pair;
		}
		MasterFileStruct* masterEntry = getRowFromMaster(rowNumberMaster);
		MasterRowEntryPair pair = { masterEntry, rowNumberMaster };
		return pair;
	}
}

void update_m(IndexTableEntry* indexEntries, size_t id, size_t indexSize, char* columnName, char* newValue, size_t newValueBufferSize) {
	MasterRowEntryPair entryRowPair = get_m(indexEntries, id, indexSize);
	MasterFileStruct* rowFromMaster = entryRowPair.entryPtr;
	size_t rowNumber = entryRowPair.rowNumber;
	if (rowFromMaster == NULL) {
		printf("No such entry... \n");
	}
	else {
		if (strcmp(columnName, "salary") == 0) {
			int salaryValue = stringToInt(newValue);
			rowFromMaster->docInfo.salary = salaryValue;
		}
		else if (strcmp(columnName, "hire_date") == 0) {
			Date date = *(getDateFromInput(newValue));
			rowFromMaster->docInfo.hireDate = date;
		}
		else if (strcmp(columnName, "first_name") == 0 ) {
			if (newValueBufferSize <= 50) {
				memcpy_s(rowFromMaster->docInfo.firstName, 50, newValue, newValueBufferSize);
			}
			else {
				printf("The name is too long!");
				exit(MEMORY_DATABASE_OPERATIONS);
			}
		}
		else if (strcmp(columnName, "last_name") == 0) {
			if (newValueBufferSize <= 50) {
				memcpy_s(rowFromMaster->docInfo.lastName, 50, newValue, newValueBufferSize);
			}
			else {
				printf("Surname is too long!");
				exit(MEMORY_DATABASE_OPERATIONS);
			}
		}
		else if (strcmp(columnName, "first_appointment") == 0) {
			int idValue = stringToInt(newValue);
			rowFromMaster->firstAppointment = idValue;
		}
		else if (strcmp(columnName, "is_present") == 0) {
			int isDeleted = stringToInt(newValue);
			rowFromMaster->isPresentInDB = isDeleted;
		}
		else {
			printf("No such field found.");
			return;
		}
		//printf("Updated row in memory: \n");
		//printMasterRow(rowFromMaster);

		writeRowToMaster(rowFromMaster, rowNumber);
		
		
		// debug prints for this method
		//printf("Debug print for update_m: \n");
		/*
		MasterFileStruct* entry = getRowFromMaster(rowNumber);
		printMasterRow(entry);
		*/
		//printAllMasterEntries();
	}
}

void del_m(IndexTableEntry* indexEntries, size_t id, size_t* indexSize, size_t* sizeOfMaster, size_t* slaveSize) {
	size_t rowNumberToRemove = getRowNumberById(indexEntries, id, *(indexSize));
	if (rowNumberToRemove == -1) return;
	int firstAppointment = get_m(indexEntries, id, *indexSize).entryPtr->firstAppointment;
	SlaveFileStruct* currentSlave;
	while (firstAppointment != -1) {
		currentSlave = readFromSlave(firstAppointment);
		del_s(indexEntries, id, currentSlave->appointmentId, *indexSize, slaveSize);
		printMasterRow(getRowFromMaster(getRowNumberById(indexEntries, id, *indexSize)));
		printSlaveEntries(*slaveSize);
		firstAppointment = get_m(indexEntries, id, *indexSize).entryPtr->firstAppointment;
	}
	update_m(indexEntries, id, *(indexSize), "is_present", "0", 1);
	removeIndexEntry(&indexEntries, id, indexSize);
	writeRowNumberToTrash(&rowNumberToRemove, -1);
	*sizeOfMaster -= 1;
}

void insert_s(SlaveFileStruct* slaveEntry, size_t whereToInsertSlaveEntry, size_t* sizeOfSlave, IndexTableEntry* indexEntries, size_t indexTableSize) {
	int masterEntryId = slaveEntry->info.doctorId;
	MasterRowEntryPair pair = get_m(indexEntries, masterEntryId, indexTableSize);
	if (pair.entryPtr == NULL)
	{
		return;
	}
	int firstAppointment = pair.entryPtr->firstAppointment;

	slaveEntry->nextSlave = firstAppointment;
	char valueBuffer[50];
	_itoa_s(*sizeOfSlave, valueBuffer, 50, 10);
	// itoa() - bad. Redo if have time
	update_m(indexEntries, masterEntryId, indexTableSize, "first_appointment", valueBuffer, 50);
	writeToSlave(slaveEntry, *sizeOfSlave);
	*(sizeOfSlave) += 1;
}

SlaveRowEntryPair* get_s(IndexTableEntry* indexEntries, size_t masterId, size_t slaveId, size_t indexSize) {
MasterRowEntryPair tmp = get_m(indexEntries, masterId, indexSize);
if (tmp.entryPtr == NULL) exit(MEMORY_DATABASE_OPERATIONS);
int firstSlaveRow = tmp.entryPtr->firstAppointment;
if (firstSlaveRow == -1) {
	printf("No slaves for this master entry found.");
	return NULL;
}
int nextSlave = firstSlaveRow;
SlaveFileStruct* slaveEntry = readFromSlave(nextSlave);
while (slaveEntry->nextSlave != -1 && slaveEntry->appointmentId != slaveId) {
	nextSlave = slaveEntry->nextSlave;
	slaveEntry = readFromSlave(nextSlave);
}
if (slaveEntry->nextSlave == -1 && slaveEntry->appointmentId != slaveId) {
	printf("No such slave entry found.");
	return NULL;
}
printf("Slave found: \n");
printSlaveEntry(slaveEntry);
SlaveRowEntryPair* pair = malloc(sizeof(SlaveRowEntryPair));
pair->entryPtr = slaveEntry;
pair->rowNumber = (size_t)nextSlave;
return pair;
}

void update_s(IndexTableEntry* indexEntries, size_t masterId, size_t slaveId, size_t indexSize, char* columnName, char* newValue, size_t newValueBufferSize) {
	SlaveRowEntryPair* slavePair = get_s(indexEntries, masterId, slaveId, indexSize);
	SlaveFileStruct* slaveEntry = slavePair->entryPtr;
	if (slaveEntry == NULL) {
		return;
	}
	if (strcmp(columnName, "appointment_date") == 0) {
		Date date = *(getDateFromInput(newValue));
		slaveEntry->info.appointmentDate = date;
	}
	else if (strcmp(columnName, "appointment_time") == 0) {
		size_t hour, minutes;
		int code = sscanf_s(newValue, "%d:%d", &hour, &minutes);
		printf("%d %d \n", hour, minutes);
		if (code == EOF || code == 0 || code == -1) {
			printf("Something is wrong with the time....");
			exit(STRING_PARSING_ERROR_DB_OPER);
		}
		Time time = { hour, minutes };
		slaveEntry->info.appointmentTime = time;
	}
	else if (strcmp(columnName, "next_slave") == 0) {
		int nextSlave = stringToInt(newValue);
		slaveEntry->nextSlave = nextSlave;
	}
	writeToSlave(slaveEntry, slavePair->rowNumber);
}

void del_s(IndexTableEntry* indexEntries, size_t masterId, size_t slaveId, size_t indexSize, size_t* slaveSize) {
	// get master entry for the slave to delete
	MasterRowEntryPair pair = get_m(indexEntries, masterId, indexSize);
	if (pair.entryPtr == NULL) {
		printf("No such master row exists... \n");
		return;
	}
	// read first 
	SlaveFileStruct* currentSlave = readFromSlave(pair.entryPtr->firstAppointment);
	int positionOfDeletedRow = 0;
	// updating list for deleted entry
	// case 1: the entry to delete is NOT pointed to by master row
	if (currentSlave->appointmentId != slaveId) {
		// check for correctness
		if (currentSlave->nextSlave == -1) {
			printf("No such slave entry exists. \n");
			return;
		}

		// find the successor of the entry we are looking for
		int rowNumberForCurrentSlave = pair.entryPtr->firstAppointment;
		SlaveFileStruct* nextSlave = readFromSlave(currentSlave->nextSlave);
		// traverse list until nextSlave is the right node
		while (nextSlave->appointmentId != slaveId) {
			// stop if we traversed all nodes(*.nextSlave == -1) and didn't find a match (*.appointmentId != slaveId)
			if (nextSlave->nextSlave == -1) {
				printf("No such slave entry exists. \n");
				return;
			}
			rowNumberForCurrentSlave = currentSlave->nextSlave;
			currentSlave = readFromSlave(currentSlave->nextSlave);
			nextSlave = readFromSlave(nextSlave->nextSlave);
		}
		// in nextSlave we store node which we have to remove.
		// if we get to this line of code, it means that nextSlave.id = slaveId => nextSlave.nextSlave is where currentSlave.id has to point.
		positionOfDeletedRow = currentSlave->nextSlave;
		currentSlave->nextSlave = nextSlave->nextSlave;
		writeToSlave(currentSlave, rowNumberForCurrentSlave);
	}
	// case 2: the entry to delete IS pointed to by master row
	else {
		positionOfDeletedRow = pair.entryPtr->firstAppointment;
		char tmp[50];
		_itoa_s(currentSlave->nextSlave, tmp, 50, 10);
		// modify the master row so that it points to the currentSlave->nextSlave.
		update_m(indexEntries, masterId, indexSize, "first_appointment", tmp, 50);
	}


	// updating list for last entry
	if (positionOfDeletedRow != (*slaveSize) - 1) {
		// get entry that will replace the deleted entry
		SlaveFileStruct* lastEntry = readFromSlave((*slaveSize) - 1);

		// find its master to find its successor
		MasterRowEntryPair masterForLastEntry = get_m(indexEntries, lastEntry->info.doctorId, indexSize);
		// finding successor:
		int firstAppointment = masterForLastEntry.entryPtr->firstAppointment;

		currentSlave = readFromSlave(firstAppointment);
		// If no successor:
		if (masterForLastEntry.entryPtr->firstAppointment == (*slaveSize) - 1) {
			char tmp[50];
			_itoa_s(positionOfDeletedRow, tmp, 50, 10);
			// update master row so that 
			update_m(indexEntries, lastEntry->info.doctorId, indexSize, "first_appointment", tmp, 50);
		}
		else {
			int currentSlaveRow = firstAppointment;
			// while the pointer isn't pointing to the last row, continue search
			while (currentSlave->nextSlave != (*slaveSize) - 1) {
				currentSlave = readFromSlave(currentSlave->nextSlave);
				currentSlaveRow = currentSlave->nextSlave;
			}
			// move pointer to the deleted row
			currentSlave->nextSlave = positionOfDeletedRow;
			// update the slave entry
			writeToSlave(currentSlave, currentSlaveRow);
		}
		// copy data from last entry to the deleted row 
		writeToSlave(lastEntry, positionOfDeletedRow);
	}
	
	//remove last slave record
	removeLastSlaveRecord();
	*slaveSize -= 1;
}