#include "SlaveIO.h"
#include <stdlib.h>
#include <windows.h>
#include <io.h>
#include <errno.h>

#define SLAVE_FILENAME "./Slave.fl"
#define SLAVE_FILE_ERROR -5500
#define SLAVE_MEMORY_ERROR -6600

void createSlaveFile() {
	FILE* out;
	fopen_s(&out, SLAVE_FILENAME, "wb");
	fclose(out);
}

void writeToSlave(SlaveFileStruct* slaveEntry, size_t rowNumber) {
	FILE* out;
	fopen_s(&out, SLAVE_FILENAME, "rb+");
	fseek(out, rowNumber * sizeof(SlaveFileStruct), SEEK_CUR);
	int k = fwrite(slaveEntry, sizeof(SlaveFileStruct), 1, out);
	if (k != 1) exit(SLAVE_FILE_ERROR);
	fclose(out);
	return;
}

SlaveFileStruct* readFromSlave(int rowNumber) { 
	FILE* in;
	fopen_s(&in, SLAVE_FILENAME, "rb");
	fseek(in, rowNumber * sizeof(SlaveFileStruct), SEEK_CUR);
	SlaveFileStruct* entryFromSlave = malloc(sizeof(SlaveFileStruct));
	if (entryFromSlave == NULL) exit(SLAVE_MEMORY_ERROR);
	int k = fread(entryFromSlave, sizeof(SlaveFileStruct), 1, in);
	if (k != 1) exit(SLAVE_FILE_ERROR);
	fclose(in);
	return entryFromSlave;
}

void printSlaveEntries(size_t slaveSize) {
	SlaveFileStruct* entry = malloc(sizeof(SlaveFileStruct));
	for (size_t i = 0; i < slaveSize; i++) {
		entry = readFromSlave(i);
		printSlaveEntry(entry);
	}
	free(entry);
	return; 
}

void printSlaveEntry(SlaveFileStruct* slaveEntry) {
	printf("************\n");
	printf("Appointment date:%d-%d-%d \n\
Appointment time: %d:%d \n\
Doctor ID: %d\n\
Patient ID: %d\n\
Next slave: %d\n\
Appointment ID: %d\n",
		slaveEntry->info.appointmentDate.year,
		slaveEntry->info.appointmentDate.month, 
		slaveEntry->info.appointmentDate.day,
		slaveEntry->info.appointmentTime.hour, 
		slaveEntry->info.appointmentTime.minutes, 
		slaveEntry->info.doctorId, 
		slaveEntry->info.patientId, 
		slaveEntry->nextSlave,
		slaveEntry->appointmentId);

}

void removeLastSlaveRecord() {
	// prepare for removing last record (get file size & its descriptor)
	FILE* out;
	fopen_s(&out, SLAVE_FILENAME, "rb+");
	fseek(out, 0, SEEK_END);
	size_t fileSize = ftell(out);
	int fileDescriptor = _fileno(out);
	// removing last record
	errno_t error = _chsize_s(fileDescriptor, fileSize - sizeof(SlaveFileStruct));
	fclose(out);
}