#include <stdio.h>
#include <omp.h>


#define MAX 50


long fib_value[MAX];
int done[MAX];


long fib(int n) {
    if (n < 2)
        return 1;


    long i, j;


    #pragma omp task shared(i)
    i = fib(n - 1);


    #pragma omp task shared(j)
    j = fib(n - 2);


    #pragma omp taskwait


    return i + j;
}


int main() {
    long result;


    #pragma omp parallel
    {
        #pragma omp single
        result = fib(10);
    }


    printf("Fib(10) = %ld\n", result);


    return 0;
}
