#include <math.h>
#include <iostream>
#include <stdio.h>
#include <mpi.h>
#include <chrono>


using namespace std;

inline const char * const BoolToString(bool b)
{
  return b ? "true" : "false";
}

int main(int nargs, char* args[])
{
    int numprocs, proc_rank;
    int counts = 50000;
    int tag = 1;
    int procNum = 4;
    std::cout << procNum << std::endl;

    int a[counts];

    for (int i = 0; i < counts - 2; i++) {
        a[i] = 1;
    }
    a[counts - 2] = 100;
    a[counts - 1] = 500;




    MPI_Init (&nargs, &args);
    MPI_Comm_size (MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank (MPI_COMM_WORLD, &proc_rank);


    int current_element = 0;
    int numbers_per_part = ceil((double)counts / (double)(numprocs - 1));

    cout << "HERE" << endl;
    if (proc_rank == 0) {
        for (int destination_process = 1; destination_process < numprocs; destination_process++) {
            int index_offset = (destination_process-1) * numbers_per_part;
            cout << "IN LOOP: INDEX OFFSET: " << index_offset << " NUMPROCS: " <<  numprocs << " RANK:" << destination_process << endl;
            if (current_element + numbers_per_part <= counts) {
                current_element += numbers_per_part;

                MPI_Send(
                    a+index_offset, // starting position
                    numbers_per_part, // nums per part
                    MPI_INT, // type
                    destination_process, // destination
                    tag, // tag
                    MPI_COMM_WORLD // communicator
                );
            } else {
                MPI_Send(
                    a+index_offset, // starting position
                    counts - current_element, // nums per part
                    MPI_INT, // type
                    destination_process, // destination
                    tag, // tag
                    MPI_COMM_WORLD // communicator
                );
            }
        }
    }

    int* bufNumbers = new int[numbers_per_part];
    bool f = false;
    MPI_Status status;

    if (proc_rank != 0) {
        MPI_Recv(
            bufNumbers,
            numbers_per_part,
            MPI_INT,
            0,
            tag,
            MPI_COMM_WORLD,
            &status
        );
    }


    cout << "Processor" << proc_rank << " received buffer" << endl;


    int k = 600;
    double start = MPI_Wtime();
    for (int i = 0; i < counts; i++) {
        int leftover = k - a[i];
        for (int j = 0; j < numbers_per_part; j++) {
            if (bufNumbers[j] == leftover) {
                f = true;
            }
        }
    }
    double end = MPI_Wtime();
	double parallel = end - start;

    MPI_Finalize ();

    if (proc_rank == 0) {
        printf("P: %7.4fs\n", parallel);
    }

    cout << "Two-sum found: " << BoolToString(f) << endl;


    return 0;
}
