#include <iostream>
#include <pthread.h>
using namespace std;


int primes[10] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};


void* compute_factorial(void* arg) {
   int index = *(int*)arg;
   int num = primes[index];


   unsigned long long* result = new unsigned long long;
   *result = 1;


   for (int i = 1; i <= num; i++)
       *result *= i;
  


   pthread_exit(result);
}


int main() {
   pthread_t threads[10];
   int indices[10];
   unsigned long long sum = 0;


   for (int i = 0; i < 10; i++) {
       indices[i] = i;  // avoid race condition
       pthread_create(&threads[i], NULL, compute_factorial, &indices[i]);
   }


   for (int i = 0; i < 10; i++) {
       unsigned long long* res;
       pthread_join(threads[i], (void**)&res);
       sum += *res;
       delete res;
   }


   cout << "Sum of factorials = " << sum << endl;
   return 0;
}
