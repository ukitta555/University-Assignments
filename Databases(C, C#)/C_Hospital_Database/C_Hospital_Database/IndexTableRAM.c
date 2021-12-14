#include "IndexTableRAM.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INDEX_TABLE_RAM_MEMORY_ERROR -1005
int comparator(const void* elem1, const void* elem2)
{
    IndexTableEntry lhs = *((IndexTableEntry*)elem1);
    IndexTableEntry rhs = *((IndexTableEntry*)elem2);
    if (lhs.doctorId > rhs.doctorId) return  1;
    if (lhs.doctorId < rhs.doctorId) return -1;
    return 0;
}

void sortEntriesById(IndexTableEntry* entries, int amount)
{
    qsort(entries, amount, sizeof(IndexTableEntry), comparator);
}

void changeRowNumberInIndex(IndexTableEntry* entries, size_t entryIndex, size_t newRowNumber) {
    entries[entryIndex].rowNumber = newRowNumber;
    printf("changed %d-th entry's row number address to %d \n", entryIndex, newRowNumber);
    printf("\n");
}

// change to bin. search if lacking performance
size_t getRowNumberById(IndexTableEntry* entries, size_t id, size_t indexSize) {
    for (size_t i = 0; i < indexSize; i++) {
        if (entries[i].doctorId == id) {
            //printf("Returning row number %d found for d %d \n", entries[i].rowNumber, entries[i].doctorId);
            return entries[i].rowNumber;
        }
    }
    printf("No such entry found in index table. Returning -1 \n");
    return -1;
}

// debug method
void printIndexEntries(IndexTableEntry* entries, size_t size) {
    printf("Printing index contents: \n");
    for (size_t i = 0; i < size; i++) {
        printf("*********************** \n");
        printf("Entry %d: \n docId: %d \n rowNumber: %d \n", i, entries[i].doctorId, entries[i].rowNumber);
    }
    printf("\n");
}


void removeIndexEntry(IndexTableEntry** entries, size_t id, size_t* indexSize) {
    
    IndexTableEntry* entryToRemove;
    for (size_t i = 0; i < *indexSize; i++) {
        if ( ((*entries) + i)->doctorId == id) {
          //  printf("Returning row number %d found for d %d \n", ((*entries) + i)->rowNumber, ((*entries) + i)->doctorId);
            entryToRemove = ((*entries) + i);
            // printIndexEntries(entryToRemove, 1);
            // printIndexEntries(entryToRemove + 1, 1);
            memmove(entryToRemove, entryToRemove + 1, (*indexSize - i - 1) * sizeof(IndexTableEntry));
            break;  
        }
    }

    *indexSize -= 1;

    IndexTableEntry* ptr;
    if (*indexSize == 0) {
        free(*entries);
        ptr = malloc(sizeof (IndexTableEntry));
    }
    else {
        ptr = realloc(*entries, sizeof(IndexTableEntry) * (*indexSize));
        if (!ptr) exit(INDEX_TABLE_RAM_MEMORY_ERROR);
    } 
    *(entries) = ptr;
}