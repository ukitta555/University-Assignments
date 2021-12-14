#include "MasterFileIO.h"

#define MASTER_FILEPATH "./Doctors.fl"
#define MASTER_DUMMY 0
#define MASTER_ERROR_CODE -2
#define MASTER_MEMORY_CODE -1000



void createMasterFile() {
	FILE* out;
	fopen_s(&out, MASTER_FILEPATH, "wb");
	printf("Master file cleared!\n");
	fclose(out);
}


void writeMasterEntry(MasterFileStruct* entry, FILE* out) {
	int k = fwrite(entry, sizeof(MasterFileStruct), 1, out);
	//printf("Bytes written: %d \n", k * sizeof(MasterFileStruct));
	if (k != 1) exit(MASTER_ERROR_CODE);
}

void writeRowToMaster(MasterFileStruct* entry, size_t row) {
	FILE* out;
	fopen_s(&out, MASTER_FILEPATH, "rb+");

	fseek(out, row * sizeof(MasterFileStruct), SEEK_SET);
	writeMasterEntry(entry, out);

	fclose(out);
}



int parseMasterEntry(MasterFileStruct* entry, FILE* in) {
	int k = fread(entry, sizeof(MasterFileStruct), 1, in);
	//printf("Bytes read: %d \n", sizeof(MasterFileStruct) * k);
	if (k != 1) return MASTER_ERROR_CODE;
	return k;
}

MasterFileStruct* getRowFromMaster(size_t row) {
	MasterFileStruct* entry = malloc(sizeof(MasterFileStruct));
	if (!entry) exit(MASTER_MEMORY_CODE);
	FILE* in;
	fopen_s(&in, MASTER_FILEPATH, "rb");

	fseek(in, row * sizeof(MasterFileStruct), SEEK_SET);
	parseMasterEntry(entry, in);

	fclose(in);
	return entry;
}

void printAllMasterEntries() {
	printf("Entries in master: \n");
	MasterFileStruct* entry = malloc(sizeof(MasterFileStruct));
	if (!entry) exit(MASTER_MEMORY_CODE);
	FILE* in;
	fopen_s(&in, MASTER_FILEPATH, "rb");

	while (!feof(in)) {
		if (parseMasterEntry(entry, in) != MASTER_ERROR_CODE) {
			printMasterRow(entry);
		}
	}
	

	fclose(in);
}

void printMasterRow(MasterFileStruct* ptr) {
	printf("--------------------- \n");
	printf("Salary: %d \n Is Present in DB: %d \n Hire date: %d %d %d \n\
First Name: %s  \n Last Name: %s \n UUID: %d \n First appointment: %d \n",
		ptr->docInfo.salary, ptr-> isPresentInDB, ptr->docInfo.hireDate.year,
		(ptr)->docInfo.hireDate.month, ptr->docInfo.hireDate.day, (ptr)->docInfo.firstName,
		(ptr)->docInfo.lastName, (ptr)->docInfo.uuid, (ptr)->firstAppointment
	);
}