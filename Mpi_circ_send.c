#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char *argv[])
{
    int rank, numprocs;
    int msg_size = 64;
    int tag = 0;
    char *buf;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	

    if (numprocs != 3) {
        if (rank == 0)
            printf("The number of processes must be three!\n");
        MPI_Finalize();
        return 0;
    }

    printf("Process %d started\n", rank);

    while (msg_size <= 1000000) {

        buf = (char *)malloc(msg_size * sizeof(char));

        int next = (rank + 1) % 3;
        int prev = (rank + 2) % 3;


        if (rank == 0) {
            MPI_Send(buf, msg_size, MPI_BYTE, next, tag, MPI_COMM_WORLD);
            printf("P0 sent %d bytes to P1\n", msg_size);

            MPI_Recv(buf, msg_size, MPI_BYTE, prev, tag, MPI_COMM_WORLD, &status);
            printf("P0 received %d bytes from P2\n", msg_size);
        }


        else if (rank == 1) {
            MPI_Recv(buf, msg_size, MPI_BYTE, prev, tag, MPI_COMM_WORLD, &status);
            printf("P1 received %d bytes from P0\n", msg_size);

            MPI_Send(buf, msg_size, MPI_BYTE, next, tag, MPI_COMM_WORLD);
            printf("P1 sent %d bytes to P2\n", msg_size);
        }
