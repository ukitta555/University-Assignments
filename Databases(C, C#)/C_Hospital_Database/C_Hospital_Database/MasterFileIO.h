#pragma once
#include <stdio.h>
#include "MasterFileStruct.h"

void createMasterFile();

MasterFileStruct* getRowFromMaster(size_t row);
void writeRowToMaster(MasterFileStruct* entry, size_t row);


int parseMasterEntry(MasterFileStruct* entry, FILE* in);
MasterFileStruct* getRowFromMaster(size_t row);

void printMasterRow(MasterFileStruct* entry);
void printAllMasterEntries();