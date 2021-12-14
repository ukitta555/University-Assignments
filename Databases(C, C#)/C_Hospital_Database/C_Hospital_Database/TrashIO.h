#pragma once

#include <stdio.h>

void writeRowNumberToTrash(size_t* rowNumber, int position);
size_t getAndRemoveLastRowFromTrash();
void printTrashContents();
void createTrashFile();
