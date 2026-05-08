#include <stdio.h>
#include <omp.h>


#define N 8


int main() {
    int x[N], y[N];


    #pragma omp parallel
    {
        int tid = omp_get_thread_num();


        if (tid < N) {
            x[tid] = tid * 10;
        }


        #pragma omp barrier  


        if (tid < N - 1) {
            y[tid] = x[tid] + x[tid + 1];
        }
    }


    printf("Results:\n");
    for (int i = 0; i < N - 1; i++) {
        printf("y[%d] = %d\n", i, y[i]);
    }


    return 0;
}
