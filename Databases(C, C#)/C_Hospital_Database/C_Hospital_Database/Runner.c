#include "Database_Operations.h"
#include "IndexTableIO.h"
#include "IndexTableRAM.h"
#include "MasterFileIO.h"
#include "TrashIO.h"
#include "SlaveIO.h"
#include <stdlib.h>
#include <string.h>

#define COMMAND_LINE_ERROR -9090


size_t indexTableSize = 0;
size_t sizeOfMaster = 0;
size_t sizeOfSlave = 0;
size_t idCounter = 1;
size_t slaveIdCounter = 1;
IndexTableEntry* indexEntries;


int getPositiveIntFromUser(char* message, size_t messageSize) {
    int result;
    int number = -1;
    // positive number in our case
    while (number < 0) {
        printf("%s", message);
        result = scanf_s("%d", &number);
        if (result != 1) exit(COMMAND_LINE_ERROR);
    }
    return number;
}


void debugInfo() {
    printf("**********************************************************\n");
    printAllMasterEntries();
    printIndexEntries(indexEntries, indexTableSize);
    printTrashContents();
    printSlaveEntries(sizeOfSlave);
}

int main()
{

    printf("Creating index... \n");
    createIndexFile(indexTableSize);
    printf("Creating master & trash files... \n");
    createMasterFile();
    createTrashFile();
    createSlaveFile();
    writeRowNumberToTrash(&sizeOfMaster, 0);
    indexEntries = getIndexContents();

    /*

    Date date = { 2000, 12, 12 };
    DoctorInfo di = { 12000, date, "xd", "lmao", 1 };
    MasterFileStruct mfs1 = {  di, 1, -1 };
    int q = 0;
    printf("insert_m \n");
    insert_m(&mfs1, q, &sizeOfMaster, &indexEntries, &indexTableSize);


    Date date2 = { 2900, 29, 29 };
    DoctorInfo di2 = { 99999, date2, "Ella", "Nekriach", 2 };
    MasterFileStruct mfs3 = { di2, 1, -1 };

    q = 1;
    insert_m(&mfs3, q, &sizeOfMaster, &indexEntries, &indexTableSize);




    SlaveFileStruct* ptr = malloc(sizeof(SlaveFileStruct));
    AppointmentInfo info = { {150,12,12}, {14, 01}, 1, 2};
    ptr->info = info;
    ptr->nextSlave = -1;
    ptr->appointmentId = 1;

    printf("insert_s 1 \n");
    insert_s(ptr, sizeOfSlave, &sizeOfSlave, indexEntries, indexTableSize);
    debugInfo();
    printSlaveEntries(sizeOfSlave);

    SlaveFileStruct* ptr1 = malloc(sizeof(SlaveFileStruct));
    AppointmentInfo info1 = { {151,13,13}, {15, 0}, 1, 3};
    ptr1->info = info1;
    ptr1->nextSlave = -1;
    ptr1->appointmentId = 2;

    printf("insert_s 2 \n");
    insert_s(ptr1, sizeOfSlave, &sizeOfSlave, indexEntries, indexTableSize);
    debugInfo();
    printSlaveEntries(sizeOfSlave);

    SlaveFileStruct* ptr2 = malloc(sizeof(SlaveFileStruct));
    AppointmentInfo info2 = { {155,13,13}, {9, 0}, 1, 4};
    ptr2->info = info2;
    ptr2->nextSlave = -1;
    ptr2->appointmentId = 3;

    printf("insert_s 3 \n");
    insert_s(ptr2, sizeOfSlave, &sizeOfSlave, indexEntries, indexTableSize);
    debugInfo();
    printSlaveEntries(sizeOfSlave);

    printf("insert_s 4 \n");
    SlaveFileStruct* ptr3 = malloc(sizeof(SlaveFileStruct));
    AppointmentInfo info3 = { {166,13,13}, {9, 0}, 2, 4 };
    ptr3->info = info3;
    ptr3->nextSlave = -1;
    ptr3->appointmentId = 4;

    insert_s(ptr3, sizeOfSlave, &sizeOfSlave, indexEntries, indexTableSize);


    printSlaveEntries(sizeOfSlave);

    get_s(indexEntries, 1, 2, indexTableSize);
    update_s(indexEntries, 1, 2, indexTableSize, "appointment_time", "17:05",  strlen("17:05"));
    get_s(indexEntries, 1, 2, indexTableSize);
    printSlaveEntries(sizeOfSlave);

    printf("\n\n DEL_S \n");
    del_s(indexEntries, 1, 1, indexTableSize, &sizeOfSlave);
    debugInfo();
    del_m(indexEntries, 2, &indexTableSize, &sizeOfMaster, &sizeOfSlave);
    debugInfo();
    */


    // CLI! DONT REMOVE!
   
    char userInput[51] = "lolxd";
    int result;
    

    while (strcmp(userInput, "stop") != 0) {
        printf("$");
        result = scanf_s("%50s", userInput, (unsigned)_countof(userInput));
        if (result != 1) exit(COMMAND_LINE_ERROR);

        if (strcmp(userInput, "insert_m") == 0) {
            Date date = { -1, -1, -1 };
            DoctorInfo info;

            info.salary = -1;


            char message[] = "Salary:";
            info.salary = getPositiveIntFromUser(message, strlen(message));


            while ((date.year < 0 || date.year > 2021) || (date.month <= 0 || date.month > 12) || (date.day <= 0 || date.day > 31)) {
                printf("Hire date:");
                result = scanf_s("%d-%d-%d", &(date.year), &(date.month), &(date.day));
                if (result != 3) exit(COMMAND_LINE_ERROR);
            }

            printf("First name:");
            result = scanf_s("%49s", &(info.firstName), (unsigned)_countof(info.firstName));
            if (result != 1) exit(COMMAND_LINE_ERROR);


            printf("Last name:");
            scanf_s("%49s", &(info.lastName), (unsigned)_countof(info.lastName));
            if (result != 1) exit(COMMAND_LINE_ERROR);

            info.hireDate = date;
            info.uuid = idCounter++;
            size_t whereToInsertMasterEntry = getAndRemoveLastRowFromTrash();
            // isPresent = 1, reference to slave = no => -1.
            MasterFileStruct masterRow = { info, 1, -1 };
            insert_m(&masterRow, whereToInsertMasterEntry, &sizeOfMaster, &indexEntries, &indexTableSize);
            // first number in trash = where to write if no entries are deleted
            writeRowNumberToTrash(&sizeOfMaster, 0);
        }
        else if (strcmp(userInput, "del_m") == 0) {
            char message[] = "Enter id of entry you want to remove:";
            int id = getPositiveIntFromUser(message, strlen(message));
            del_m(indexEntries, (size_t)id, &indexTableSize, &sizeOfMaster, &sizeOfSlave);
        }
        else if (strcmp(userInput, "get_m") == 0) {
            char message[] = "Enter id of entry you want to retrieve:";
            int id = getPositiveIntFromUser(message, strlen(message));
            get_m(indexEntries, (size_t)id, indexTableSize);
        }
        else if (strcmp(userInput, "update_m") == 0) {
            char message[] = "Enter id of entry you want to update:";
            int id = getPositiveIntFromUser(message, strlen(message));

            char columnName[50];
            printf("Column name:");
            result = scanf_s("%49s", &(columnName), (unsigned)_countof(columnName));
            if (result != 1) exit(COMMAND_LINE_ERROR);

            char newValue[50];
            printf("New value:");
            result = scanf_s("%49s", &(newValue), (unsigned)_countof(newValue));
            if (result != 1) exit(COMMAND_LINE_ERROR);


            update_m(indexEntries, id, indexTableSize, columnName, newValue, 50);
        }
        else if (strcmp(userInput, "insert_s") == 0) {
            SlaveFileStruct* newSlave = malloc(sizeof(SlaveFileStruct));
            
            Date date = { -1, -1, -1 };
            while ((date.year < 0 || date.year > 2021) || (date.month <= 0 || date.month > 12) || (date.day <= 0 || date.day > 31)) {
                printf("Appointment date:");
                result = scanf_s("%d-%d-%d", &(date.year), &(date.month), &(date.day));
                if (result != 3) exit(COMMAND_LINE_ERROR);
            }
            newSlave->info.appointmentDate = date;

            Time time = { -1, -1 };
            while ((time.hour < 0 || time.hour > 24) || (time.minutes <= 0 || time.minutes > 60)) {
                printf("Appointment time:");
                result = scanf_s("%d:%d", &(time.hour), &(time.minutes));
                if (result != 2) exit(COMMAND_LINE_ERROR);
            }
            newSlave->info.appointmentTime = time;

            int doctorId = getPositiveIntFromUser("Doctor ID:", strlen("Doctor ID:"));
            newSlave->info.doctorId = doctorId;

            int patientId = getPositiveIntFromUser("Patient ID:", strlen("Patient ID:"));
            newSlave->info.patientId = patientId;

            newSlave->appointmentId = slaveIdCounter++;
            newSlave->nextSlave = -1;

            insert_s(newSlave, sizeOfSlave, &sizeOfSlave, indexEntries, indexTableSize);
        }
        else if (strcmp(userInput, "get_s") == 0) {
            char message[] = "Enter id of master entry you want to retrieve:";
            int masterId = getPositiveIntFromUser(message, strlen(message));
            int slaveId = getPositiveIntFromUser("Enter id of master entry you want to retrieve:", strlen("Enter id of master entry you want to retrieve:"));
            get_s(indexEntries, masterId, slaveId, indexTableSize);
        }
        else if (strcmp(userInput, "update_s") == 0) {
            char masterMessage[] = "Enter id of master entry you want to update:";
            int masterId = getPositiveIntFromUser(masterMessage, strlen(masterMessage));
        
            char message[] = "Enter id of slave entry you want to update:";
            int slaveId = getPositiveIntFromUser(message, strlen(message));

            
            char columnName[50];
            printf("Column name:");
            result = scanf_s("%49s", &(columnName), (unsigned)_countof(columnName));
            if (result != 1) exit(COMMAND_LINE_ERROR);

            char newValue[50];
            printf("New value:");
            result = scanf_s("%49s", &(newValue), (unsigned)_countof(newValue));
            if (result != 1) exit(COMMAND_LINE_ERROR);

            update_s(indexEntries, masterId, slaveId, indexTableSize, columnName, newValue, 50);
        }
        else if (strcmp(userInput, "del_s") == 0) {
            char masterMessage[] = "Enter master id of entry you want to remove:";
            int masterId = getPositiveIntFromUser(masterMessage, strlen(masterMessage));

            char message[] = "Enter slave id of entry you want to remove:";
            int slaveId = getPositiveIntFromUser(message, strlen(message));

            del_s(indexEntries, masterId, slaveId, &indexTableSize, &sizeOfSlave);
        }
        else if (strcmp(userInput, "ut_m") == 0) {
            printf("------------------------------------------------------------------------\n");
            printAllMasterEntries();
        }
        else if (strcmp(userInput, "ut_s") == 0) {
            printf("**********************************************************\n");
            printSlaveEntries(sizeOfSlave);
        }
        else if (strcmp(userInput, "calc_m") == 0) {
            printf("Entries in master: %d \n", sizeOfMaster);
        }
        else if (strcmp(userInput, "calc_s") == 0) {
            printf("Entries in slave: %d \n", sizeOfSlave);
        }
        else if (strcmp(userInput, "debug") == 0) {
            debugInfo();
        }
    }






    


    /*
    IndexTableEntry* entries = getIndexContents();

    Date date = { 2000, 12, 12 };
    DoctorInfo di = { 12000, date, "xd", "lmao", 1 };
    MasterFileStruct mfs1 = { di, 1, 1 };

    
    Date date1 = { 2111, 1, 1 };
    DoctorInfo di1 = { 121212, date1, "new", "doctor", 2 };
    MasterFileStruct mfs2 = { di1, 1, 3 };

    Date date2 = { 2900, 29, 29 };
    DoctorInfo di2 = { 99999, date2, "Ella", "Nekriach", 3 };
    MasterFileStruct mfs3 = { di2, 1, 4 };


    createMasterFile();
    size_t q = 0;
    insert_m(&mfs2, &q, &entries, &indexTableSize);
    q = 1;
    insert_m(&mfs1, &q, &entries, &indexTableSize);
    q = 2;
    insert_m(&mfs3, &q, &entries, &indexTableSize);
    printf("Check that index size increased: %d", indexTableSize);
    printf("\n");
    get_m(entries, 1, indexTableSize);
    printf("\n");
    */

    /*
    update_m(entries, 1, indexTableSize, "salary", "5555", 5);
    update_m(entries, 1, indexTableSize, "hire_date", "2222-22-22", 11);
    update_m(entries, 1, indexTableSize, "first_name", "Doctor", 7);
    update_m(entries, 1, indexTableSize, "last_name", "House", 6);
    update_m(entries, 1, indexTableSize, "first_appointment", "567", 3);
    update_m(entries, 1, indexTableSize, "is_present", "0", 1);
    */
    /*
    printIndexEntries(entries, 3);
    del_m(entries, 1, &indexTableSize);


    size_t l = 123;
    size_t l1 = 999;

    

    writeRowNumberToTrash(&l1, 0);
    writeRowNumberToTrash(&l, -1);
    writeRowNumberToTrash(&l1, -1);
    getAndRemoveLastRowFromTrash();
    getAndRemoveLastRowFromTrash();
    getAndRemoveLastRowFromTrash();

    */

    /*
    indexTableSize = 2;
    entries = malloc(sizeof(IndexTableEntry) * indexTableSize);
    IndexTableEntry entry1 = { 1231432, 321 };
    IndexTableEntry entry2 = { 12432, 3213212 };
    
    entries[0] = entry1;
    entries[1] = entry2;
    

    writeIndexContents (entries, &(indexTableSize), 2);
    entries = getIndexContents();
    
    printIndexEntries(entries, indexTableSize);
    changeRowNumberInIndex(entries, 0, 900);
    printIndexEntries(entries, indexTableSize);
    
    writeIndexContents(entries, &(indexTableSize), 2);
    entries = getIndexContents();



    Date date = { 2000, 12, 12 };
    DoctorInfo di = { 12000, date, "xd", "lmao", 1 };
    MasterFileStruct mfs = { di, 1, 1 };
    createMasterFile();
    writeRowToMaster(&mfs, 0);
    MasterFileStruct* ptr = malloc(sizeof(MasterFileStruct));
    ptr = getRowFromMaster(0);

    printMasterRow(ptr);
    */


    return 0;
}