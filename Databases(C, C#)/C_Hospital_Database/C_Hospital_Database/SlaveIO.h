#pragma once
#include "SlaveFileStruct.h"
#include <stdio.h>

void createSlaveFile();
void writeToSlave(SlaveFileStruct* slaveEntry, size_t rowNumber);
SlaveFileStruct* readFromSlave(size_t rowNumber);
void printSlaveEntries(size_t slaveSize);
void printSlaveEntry(SlaveFileStruct* slaveEntry);
void removeLastSlaveRecord();
