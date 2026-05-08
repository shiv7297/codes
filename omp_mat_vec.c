#include <stdio.h>
#include <stdlib.h>
#include <omp.h>


#define SIZE 4 


int privateVar;
#pragma omp threadprivate(privateVar)


int main() {
   int mat[SIZE][SIZE];
   int vec[SIZE];
   int result[SIZE] = {0};
   int sum_result = 0;


   for (int i = 0; i < SIZE; i++) {
       vec[i] = rand() % 10 + 1;


       for (int j = 0; j < SIZE; j++) {
           mat[i][j] = rand() % 10 + 1;
       }
   }


   #pragma omp parallel
   {
       #pragma omp single
       {
           printf("Starting parallel matrix-vector multiplication\n");
       }


       privateVar = omp_get_thread_num();


       #pragma omp for
       for (int i = 0; i < SIZE; i++) {
           int temp = 0;


           for (int j = 0; j < SIZE; j++) {
               temp += mat[i][j] * vec[j];
           }


           result[i] = temp;


           printf("Thread %d computed result[%d] = %d\n", privateVar, i, result[i]);
       }


       #pragma omp sections
       {
           #pragma omp section
           {
               int local_sum = 0;
               for (int i = 0; i < SIZE; i++) {
                   local_sum += result[i];
               }
              
                   sum_result += local_sum;
                   printf("Thread %d computed sum_result = %d\n", privateVar, sum_result);
              
           }


           #pragma omp section
           {
               int local_max = result[0];
               for (int i = 1; i < SIZE; i++) {
                   if (result[i] > local_max) local_max = result[i];
               }
             
                   printf("Thread %d computed max element = %d\n", privateVar, local_max);
              
           }
       }
   }


   printf("\nMatrix-Vector Result:\n");
   for (int i = 0; i < SIZE; i++) {
       printf("%d ", result[i]);
   }
   printf("\nSum of elements = %d\n", sum_result);


   return 0;
}
