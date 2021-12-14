#include "TrashIO.h"
#include <windows.h>
#include <io.h>
#include <errno.h>

#define MASTER_TRASH_FILENAME "./Doctors.trsh"
#define MASTER_TRASH_MEMORY_ERROR -4500

void createTrashFile() {
	FILE* out;
	fopen_s(&out, MASTER_TRASH_FILENAME, "wb");
	fclose(out);
}

/* 
positiion < 0 => write to the end of file
else write to the specified position	
*/
void writeRowNumberToTrash(size_t* rowNumber, int position) {
	FILE* out;
	fopen_s(&out, MASTER_TRASH_FILENAME, "rb+");
	if (position < 0) {
		fseek(out, 0L , SEEK_END);
	}
	else {
		fseek(out, (long)position * sizeof(size_t), SEEK_CUR);
	}
	int k = fwrite(rowNumber, sizeof(size_t), 1, out);
	//printf("Bytes written: %d \n", k * sizeof(size_t));
	if (k != 1) exit(MASTER_TRASH_MEMORY_ERROR);
	fclose(out);
}



size_t getAndRemoveLastRowFromTrash() {
	FILE* in;

	fopen_s(&in, MASTER_TRASH_FILENAME, "rb+");

	// get last entry in trash section
	fseek(in, -4L, SEEK_END);

	size_t* rowNumber = malloc(sizeof(size_t));
	int k = fread(rowNumber, sizeof(size_t), 1, in);

	//printf("Bytes read: %d \n", k * sizeof(size_t));
	//printf("Number read: %d \n", *rowNumber);
	if (k != 1) exit(MASTER_TRASH_MEMORY_ERROR);

	// prepare for removing last record (get file size & its descriptor)
	size_t fileSize = ftell(in);
	int fileDescriptor = _fileno(in);
	// removing last record
	errno_t error = _chsize_s(fileDescriptor, fileSize - sizeof(size_t));

	fclose(in);
	return *rowNumber;
}

void printTrashContents() {
	FILE* in;
	printf("---------------------\n");
	printf("Trash contents: \n");
	fopen_s(&in, MASTER_TRASH_FILENAME, "rb+");

	size_t* rowNumber = malloc(sizeof(size_t));
	while (!feof(in))
	{
		int k = fread(rowNumber, sizeof(size_t), 1, in);
		if (k != 1) break;
		printf("%d \n", *rowNumber);
	}
	
	fclose(in);
}