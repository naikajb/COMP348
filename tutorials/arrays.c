#include <stdio.h>
#include <stdlib.h>


int main(int argc, char const *argv[])
{
    //static memory alloxation at compile-time
    int array_static[5] = {1,2,3,4,5};

    //dynamic memory allocation at run-time
    int n = 5;
    int *array_dynamic = (int *)malloc(n * sizeof(int));//default initialize to 0

    for(int i = 0; i < n; i++){
        array_dynamic[i] = i + 1;
    }

    
    return 0;
}
