#pragma once
#include "MasterFileStruct.h"
#include "SlaveIO.h"
#include "IndexTableIO.h"
#include "RowEntryPairs.h"

int stringToInt(char* stringToConvert);
Date* getDateFromInput(char* newValue);

void insert_m(MasterFileStruct* masterEntry, size_t whereToInsertMasterEntry, size_t* sizeOfMaster, IndexTableEntry** indexEntries, size_t* indexTableSize);
MasterRowEntryPair get_m(IndexTableEntry* indexEntries, size_t id, size_t indexSize);
void update_m(IndexTableEntry* indexEntries, size_t id, size_t indexSize, char* columnName, char* newValue, size_t newValueBufferSize);
void del_m(IndexTableEntry* indexEntries, size_t id, size_t* indexSize, size_t* sizeOfMaster, size_t* slaveSize);
void insert_s(SlaveFileStruct* slaveEntry, size_t whereToInsertSlaveEntry, size_t* sizeOfSlave, IndexTableEntry* indexEntries, size_t indexSize);
SlaveRowEntryPair* get_s(IndexTableEntry* indexEntries, size_t masterId, size_t slaveId, size_t indexSize);
void update_s(IndexTableEntry* indexEntries, size_t masterId, size_t slaveId, size_t indexSize, char* columnName, char* newValue, size_t newValueBufferSize);
void del_s(IndexTableEntry* indexEntries, size_t masterId, size_t slaveId, size_t indexSize, size_t* slaveSize);