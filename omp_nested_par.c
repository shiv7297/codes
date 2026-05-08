#include <stdio.h>
#include <omp.h>


void subprogram() {
   printf("subprogram: outside (thread %d)\n",
          omp_get_thread_num());


   #pragma omp parallel
   {
       printf("subprogram: inside (thread %d)\n",
              omp_get_thread_num());
   }
}


int main() {
 


   printf("Main: outside \n");


   subprogram();


   #pragma omp parallel
   {
       printf("Main: inside (thread %d)\n",
              omp_get_thread_num());


       #pragma omp barrier


       subprogram();
   }


   return 0;
}
