#include <math.h>
#include <iostream>
#include <stdio.h>
// #include <mpi.h>
#include <omp.h>
#include <chrono>


// using namespace std;
using namespace std::chrono;

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


    int q = 600;
    bool f = false;

    auto start = steady_clock::now();
	for (int i = 0; i < counts; i++) {
        int leftover = q - a[i];
        for (int j = 0; j < counts; j++) {
            if (a[j] == leftover) {
                f = true;
            }
        }
    }
	auto end = steady_clock::now();


	printf("%\nTime elapsed: %7.4f", (double)duration_cast<microseconds>(end - start).count() / 1000000.0);
	printf("\n-------\n");


    int part = counts / procNum;
	double startPar = omp_get_wtime();
	#pragma omp parallel for shared(a)
    for (int i = 0; i < procNum; i++) {
        int maxInd = (i + 1) * part;
        for (int j = 0; j < counts; j++) {
            int leftover = q - a[j];
            for (int k = i * part; k < maxInd; k++) {
                if (leftover == a[k]) {
                    f = true;
                }
            }
        }
    }

	double endPar = omp_get_wtime();
    printf("%\nTime elapsed: %7.4f", endPar - startPar);



    /*
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
                // cout << "Processor" << proc_rank << "found two-sum: " << a[i] << "+" << bufNumbers[j] << endl;
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
    // MPI_Finalize(); // finish MPI environment
    */
    return 0;
}
