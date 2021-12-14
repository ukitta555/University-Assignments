#pragma once
#include "IndexTableIO.h"

void sortEntriesById(IndexTableEntry* indexEntries, int amount);
int comparator(const void* elem1, const void* elem2);
void changeRowNumberInIndex(IndexTableEntry* entries, size_t entryIndex, size_t newRowNumber);
size_t getRowNumberById(IndexTableEntry* indexEntries, size_t id, size_t indexSize);
void printIndexEntries(IndexTableEntry* indexEntries, size_t size);
void removeIndexEntry(IndexTableEntry** entries, size_t id, size_t* indexSize);