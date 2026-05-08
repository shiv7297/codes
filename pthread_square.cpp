#include <iostream>
#include <pthread.h>
using namespace std;


void* compute_square(void* arg) { // default argument and return type for pthreads
   int num = *(int*)arg;   //type cast and then derefrencing


   int* result = new int;
   *result = num * num;


   pthread_exit(result);
}






int main() {
   pthread_t threads[5];
   int nums[5] = {1, 2, 3, 4, 5};
   int sum = 0;


   for (int i = 0; i < 5; i++) {
       pthread_create(&threads[i], NULL, compute_square, &nums[i]);
   }


   for (int i = 0; i < 5; i++) {
       int* res;
       int status = pthread_join(threads[i], (void**)&res);  //pointer to pointer -> the val returned by sqr func
       if(status != 0) {
           cout<<"error while joining threads";
           exit(1);
       }
       else{
           sum += *res;
           delete res;
       }
   }


   cout << "Sum of squares = " << sum << endl;
   return 0;
}
