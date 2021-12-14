#pragma once
#include "Date.h"

typedef struct DoctorInfo {
    int salary;
    Date hireDate;
    char firstName[50];
    char lastName[50];
    int uuid;
} DoctorInfo;

typedef struct MasterFileStruct {
    DoctorInfo docInfo;
    int isPresentInDB;
    int firstAppointment; // pointer to the slave file!
} MasterFileStruct;