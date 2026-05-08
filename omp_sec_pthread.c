#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>


#define N 1000000


int privateVar = 2;
#pragma omp threadprivate(privateVar)


int computeA() {
   printf("computeA() executed by thread %d\n", omp_get_thread_num());
   return 5;
}


int computeB() {
   printf("computeB() executed by thread %d\n", omp_get_thread_num());
   return 10;
}


int main() {


   int A[N], B[N];


   long long serial_dot = 0;
   long long parallel_dot = 0;


   double start, end;
   int sharedVar = 0;


   srand(time(NULL));


   for (int i = 0; i < N; i++) {
       A[i] = (rand() % 100) + 1;
       B[i] = (rand() % 100) + 1;
   }


   start = omp_get_wtime();


   for (int i = 0; i < N; i++) {
       serial_dot += A[i] * B[i];
   }


   end = omp_get_wtime();
   double serial_time = end - start;


   start = omp_get_wtime();


   #pragma omp parallel
   {


       #pragma omp for reduction(+:parallel_dot)
       for (int i = 0; i < N; i++) {
           parallel_dot += A[i] * B[i];
       }
   }


   end = omp_get_wtime();
   double parallel_time = end - start;




   long long sectionResultA = 0;
   long long sectionResultB = 0;


   #pragma omp parallel
   {
       privateVar = 3;  


       #pragma omp single
       {
           sharedVar = 4;
           printf("sharedVar initialized to %d by thread %d\n",
                  sharedVar, omp_get_thread_num());
       }


       #pragma omp barrier


       #pragma omp sections
       {
           #pragma omp section
           {
               sectionResultA = computeA() * sharedVar * privateVar;
               printf("Section A executed by thread %d, Result = %lld\n",
                      omp_get_thread_num(), sectionResultA);
           }


           #pragma omp section
           {
               sectionResultB = computeB() * sharedVar * privateVar;
               printf("Section B executed by thread %d, Result = %lld\n",
                      omp_get_thread_num(), sectionResultB);
           }
       }
   }




   printf("\nResults : \n");
   printf("Serial  Product   : %lld\n", serial_dot);
   printf("Parallel  Product : %lld\n", parallel_dot);
   printf("Section A Result     : %lld\n", sectionResultA);
   printf("Section B Result     : %lld\n", sectionResultB);
   printf("Serial Time          : %f seconds\n", serial_time);
   printf("Parallel Time        : %f seconds\n", parallel_time);




   return 0;
}
