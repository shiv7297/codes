#include <stdio.h>
#include <stdlib.h>
#include <omp.h>


#define N 100000


int main() {
   int i;
   double A[N], B[N];
   double parallel = 0.0;
   double serial = 0.0;


   srand(1);
   for (i = 0; i < N; i++) {
       A[i] = (rand() % 100) + 1;
       B[i] = (rand() % 100) + 1;
   }


   double start_single = omp_get_wtime();


   for (i = 0; i < N; i++) {
       serial += A[i] * B[i];
   }


   double end_single = omp_get_wtime();


   omp_set_nested(1);


   double start_parallel = omp_get_wtime();


   #pragma omp parallel
   {
       int tid = omp_get_thread_num();
       int num_threads = omp_get_num_threads();


       int chunk_size = N / num_threads;
       int start = tid * chunk_size;
       int end = start + chunk_size;


       double local_sum = 0.0;


       #pragma omp parallel for reduction(+:local_sum)
       for (int j = start; j < end; j++) {
           local_sum += A[j] * B[j];
       }


       #pragma omp atomic
       parallel += local_sum;
   }
  
   double end_parallel = omp_get_wtime();


   printf("Serial dot product   = %.2f\n", serial);
   printf("Parallel dot product = %.2f\n", parallel);


   if (serial == parallel)
       printf("Result is CORRECT\n");
   else
       printf("Result is INCORRECT\n");


    printf("Serialtime: %.6f seconds\n", end_single - start_single);
   printf("Parallel time: %.6f seconds\n", end_parallel - start_parallel);


   return 0;
}
