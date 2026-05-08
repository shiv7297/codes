#include <stdio.h>
#include <omp.h>
#include<stdlib.h>


#define V 5
#define INF 1000000


int dist[V][V] = {{0, 4, INF, 5, INF},
               {INF, 0, 1, INF, 6},
               {2, INF, 0, 3, INF},
               {INF, INF, 1, 0, 2},
               {1, INF, INF, 4, 0}};


int main() {
   #pragma omp parallel
   {
       #pragma omp single
       {
           for (int k = 0; k < V; k++) {


               for (int i = 0; i < V; i++) {
                   for (int j = 0; j < V; j++) {


                       #pragma omp task
                       //#pragma omp task firstprivate(i,j,k)
                       {
                           if (dist[i][k] != INF &&  dist[k][j] != INF && dist[i][j] > dist[i][k] + dist[k][j]) {
                               dist[i][j] = dist[i][k] + dist[k][j];
                           }
                       }


                   }
               }


               #pragma omp taskwait
           }
       }
   }


   printf("Shortest distances:\n");
   for (int i = 0; i < V; i++) {
       for (int j = 0; j < V; j++) {
           if (dist[i][j] == INF)
               printf("INF ");
           else
               printf("%3d ", dist[i][j]);
       }
       printf("\n");
   }


   return 0;
}
