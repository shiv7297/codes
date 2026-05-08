#include <stdio.h>
#include <omp.h>


int main() {
    int shared_variable = 0;
    omp_lock_t mylock;


    omp_init_lock(&mylock);


    #pragma omp parallel
    {
        omp_set_lock(&mylock);
        shared_variable += 1;
        printf("Thread %d updated value to %d\n",
               omp_get_thread_num(), shared_variable);
        omp_unset_lock(&mylock);
    }


    omp_destroy_lock(&mylock);


    printf("Final value = %d\n", shared_variable);


    return 0;
}
