/*
    COMP 348 - Programming Languages
    Assignment 1 - Due June 5th 2023 @ midnight
    Naika Jean-Baptiste (40227367)
*/

/*
        compilation: gcc -Wall aggregate.c singular.c mathpipe.c
        execution:
                ex ==> cat sample.txt | mathpipe sum -size = 2
                ex ==> cat sample.txt | mathpipe -size=1 FILTER GEQ 10 | mathpipe SUM
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{

    char buffer = 0;
    // space for values in the input file
    double *valuesArr = (double *)malloc(256 * sizeof(double));
    double value = 0;
    int scanned = 0;
    int n = 0;

    //reads a line by line from stdin 
    //in this case will read a line from sample.txt file 
    while (fgets(&buffer, 1000, stdin) != NULL)
    {
        int offset = 0;
        
        //this will look at the line currently in the buffer
        //each double at a time is analysed and put in the array "valuesArr"
        while(sscanf(&buffer + offset, "%lf%n", &value, &scanned) == 1){
            valuesArr[n] = value;
            printf("[%d]\t --> \t%f\n", n,valuesArr[n]);
            n++;
            offset += scanned;
        }
    }
    free(valuesArr);

    return 0;
}
