#include "IndexTableIO.h"
#include "IndexTableRAM.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INDEX_FILEPATH "./Doctors.ind"
#define INDEX_DUMMY 0
#define INDEX_ERROR_CODE -1
#define INDEX_MEMORY_CODE -1001



// Clear file and insert header row inside it.
void createIndexFile(size_t amountOfEntries) {
	FILE* out;
	fopen_s(&out, INDEX_FILEPATH, "wb");
	// write header row to the file
	// second number = amount of rows in the index table
	IndexTableEntry rowAmount = { INDEX_DUMMY, amountOfEntries }; 
	writeEntryToIndex(rowAmount, out);
	fclose(out);
}


// returns amount of bytes written to file
void writeIntsToIndex(size_t numbersToWrite[], size_t amount, FILE* out) {
	size_t k = fwrite(numbersToWrite, sizeof(size_t), amount, out);
	//printf("Bytes written: %d \n", k * sizeof(size_t));
	if (k != amount) exit(INDEX_ERROR_CODE);
}

int writeEntryToIndex(IndexTableEntry entry, FILE* out) {
	size_t entryArray[] = { entry.doctorId, entry.rowNumber };
	writeIntsToIndex(entryArray, 2, out);
}

// sizeOfIndex - pointer to the number of rows for the main file, amountOfEntries - number of rows to write to file
// inserts header row using createIndexFile()
void writeIndexContents(IndexTableEntry* entries, size_t* sizeOfIndex, size_t newAmountOfEntries) {
	printf("Writing to index... \n");
	*sizeOfIndex = newAmountOfEntries;
	createIndexFile(newAmountOfEntries);
	sortEntriesById(entries, newAmountOfEntries);
	FILE* out;
	fopen_s(&out, INDEX_FILEPATH, "ab");
	if (out == NULL)
	{
		printf("Error! Could not open file\n");
		exit(INDEX_ERROR_CODE);
	}

	// -1 as no header!
	for (size_t i = 0; i < newAmountOfEntries; i++) {
		writeEntryToIndex(entries[i], out);
	}

	printf("\n");
	fclose(out);
}




// returns amount of bytes retrieved from index
int* getIntsFromIndex(size_t intCount, size_t rowNumber, FILE* in) {

	int* buffer = malloc(intCount * sizeof(int));
	if (!buffer) exit(INDEX_MEMORY_CODE);
	// add offset to where we should start getting ints
	fseek(in, rowNumber * 2 * sizeof(int), SEEK_SET);
	int k = fread(buffer, sizeof(int), intCount, in);

	if (k != intCount) {
		int bad = INDEX_ERROR_CODE;
		return &bad;
	}

	/*
	printf("Bytes read: %d \n", k * sizeof(int));
	for (size_t i = 0; i < intCount; i++) {
		printf("Number read: %d \n", buffer[i]);
	}
	printf("\n");
	*/

	return buffer;
}

IndexTableEntry getEntryFromIndex(size_t rowNumber, FILE* in) {
	int* info = getIntsFromIndex(2, rowNumber, in);
	if (*(info) == INDEX_ERROR_CODE) {
		IndexTableEntry bad = { INDEX_ERROR_CODE, INDEX_ERROR_CODE };
		return bad;
	}
	IndexTableEntry entry = { info[0], info[1] };
	return entry;
}

// DOESN'T RETURN HEADER ROW!
IndexTableEntry* getIndexContents() {
	printf("Reading index contents... \n");
	FILE* in;
	fopen_s(&in, INDEX_FILEPATH, "rb");
	if (in == NULL)
	{
		printf("Error! Could not open file \n");
		exit(INDEX_ERROR_CODE);
	}

	
	int currentRow = 0;
	// get first row where the info about the total number of rows is stored
	IndexTableEntry rowCountStruct = getEntryFromIndex(currentRow, in);
	int rowsInIndexFile = rowCountStruct.rowNumber;

	IndexTableEntry* entries = malloc(sizeof(IndexTableEntry) *  rowsInIndexFile); // don't include header
	if (!entries) exit(INDEX_MEMORY_CODE);
	
	currentRow++; // currentRow = 1;

	while (!feof(in)) {
		// get current row from file
		IndexTableEntry entry = getEntryFromIndex(currentRow, in);
		// Detect EOF when feof fails to do so
		if (entry.doctorId == INDEX_ERROR_CODE && entry.rowNumber == INDEX_ERROR_CODE) {
			break;
		}
		// add it to the array ( currentRow - 1  => no header returned )
		entries[currentRow - 1] = entry;

		//printf("Doc id: %d \nRow number: %d \n", entry.doctorId, entry.rowNumber);
		
		// move to the next row
		++currentRow;
	}

	printf("\n");
	fclose(in);
	return entries;
}