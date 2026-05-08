#include <stdio.h>

#define V 4
#define INF 9999

int minDistance(int dist[], int visited[])
{
    int min = INF, min_index;

    for(int v = 0; v < V; v++)
    {
        if(visited[v] == 0 && dist[v] <= min)
        {
            min = dist[v];
            min_index = v;
        }
    }

    return min_index;
}

void dijkstra(int graph[V][V], int src)
{
    int dist[V];
    int visited[V];

    for(int i = 0; i < V; i++)
    {
        dist[i] = INF;
        visited[i] = 0;
    }

    dist[src] = 0;

    for(int count = 0; count < V - 1; count++)
    {
        int u = minDistance(dist, visited);

        visited[u] = 1;

        for(int v = 0; v < V; v++)
        {
            if(!visited[v] &&
               graph[u][v] &&
               dist[u] != INF &&
               dist[u] + graph[u][v] < dist[v])
            {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    printf("Vertex\tDistance from Source\n");

    for(int i = 0; i < V; i++)
    {
        printf("%d \t %d\n", i, dist[i]);
    }
}

int main()
{
    int graph[V][V] = {
        {0, 5, 0, 10},
        {5, 0, 3, 0},
        {0, 3, 0, 1},
        {10, 0, 1, 0}
    };

    dijkstra(graph, 0);

    return 0;
}b