#include <stdio.h>  
#include <string.h>  
#include <stdlib.h>  
#include <omp.h>  

typedef struct People *people;

struct People
{  
    char name[20];  
    int age;  
};  
  
people people_init(int age)
{   
    people p = (people)malloc(sizeof(people));   
    strcpy(p->name, "Joe");  
    p->age = age;  
	#pragma omp parallel
	{
	fprintf(stderr, "Hello from thread %d of %d\n", omp_get_thread_num(), omp_get_num_threads());
	}
      
    return p;   
}  
