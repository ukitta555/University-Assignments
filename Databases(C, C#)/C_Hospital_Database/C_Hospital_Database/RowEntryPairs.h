#pragma once
#include "MasterFileStruct.h"
#include "SlaveFileStruct.h"
typedef struct MasterRowEntryPair {
	MasterFileStruct* entryPtr;
	size_t rowNumber;
} MasterRowEntryPair;

typedef struct SlaveRowEntryPair {
	SlaveFileStruct* entryPtr;
	size_t rowNumber;
} SlaveRowEntryPair;