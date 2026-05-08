#include <stdio.h>
#include <omp.h>


int main() {
    omp_lock_t lockA, lockB;
    omp_init_lock(&lockA);
    omp_init_lock(&lockB);


    #pragma omp parallel sections
    {
        #pragma omp section
        {
            omp_set_lock(&lockA);
            omp_set_lock(&lockB);


            printf("Section 1\n");


            omp_unset_lock(&lockB);
            omp_unset_lock(&lockA);
        }


        #pragma omp section
        {
            omp_set_lock(&lockA);
            omp_set_lock(&lockB);


            printf("Section 2\n");


            omp_unset_lock(&lockB);
            omp_unset_lock(&lockA);
        }
    }


    omp_destroy_lock(&lockA);
    omp_destroy_lock(&lockB);


    return 0;
}
