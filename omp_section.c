#include <stdio.h>
#include <omp.h>


int computeA() {
   printf("computeA() executed by thread %d\n", omp_get_thread_num());
   return 10;
}


int computeB() {
   printf("computeB() executed by thread %d\n", omp_get_thread_num());
   return 20;
}


int main() {
   int shared = 0;
   int final_result = 0;


   #pragma omp parallel reduction(+:final_result)
   {
       #pragma omp single
       {
           shared = 5;
           printf("shared initialized to %d by thread %d\n",
                  shared, omp_get_thread_num());
       }


       #pragma omp barrier


       #pragma omp sections
       {
           #pragma omp section
           {
               int localResult = computeA() * shared;
               printf("Section A executed by thread %d, Result = %d\n",
                      omp_get_thread_num(), localResult);
               final_result += localResult;
           }


           #pragma omp section
           {
               int localResult = computeB() * shared;
               printf("Section B executed by thread %d, Result = %d\n",
                      omp_get_thread_num(), localResult);
               final_result += localResult;
           }
       }
   }


   printf("\nFinal Result = %d\n", final_result);


   return 0;
}
