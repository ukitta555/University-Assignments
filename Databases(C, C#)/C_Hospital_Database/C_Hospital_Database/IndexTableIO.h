#pragma once
#include <stdio.h>

typedef struct IndexTableEntry {
	size_t doctorId;
	size_t rowNumber;
} IndexTableEntry;


void createIndexFile(size_t amountOfEntries);

// write methods
// write all ints from numbersToWrite[]
void writeIntsToIndex(size_t numbersToWrite[], size_t amount, FILE* out);
int writeEntryToIndex(IndexTableEntry entry, FILE* out); // write to the end of file
void writeIndexContents(IndexTableEntry* entries, size_t* sizeOfIndex, size_t newAmountOfEntries);

// read methods
// read from *rowNumber* row *intCount* integers
int* getIntsFromIndex(size_t intCount, size_t rowNumber, FILE* in);
// read 2 ints
IndexTableEntry getEntryFromIndex(size_t rowNumber, FILE* in);
// read the whole index file
IndexTableEntry* getIndexContents();
