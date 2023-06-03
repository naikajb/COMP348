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
#include <stdbool.h>

int prec = 0;
int size = 0;
bool isAggregate = false;
bool isSingular = false;
char* aggFunc;

void checkAggregate(char* funcName);

int main(int argc, char const *argv[])
{

    if(argc == 1 ){
        printf("usage: cat <input file> | mathpipe <function name> <optional parameters> ");
        return 0;
    }

    for( int i = 1; i < argc; i++)
    {
        if(strcasecmp(argv[i],"sum") == 0)
        {
           // printf("first function is sum");
            checkAggregate("sum");
            
        }else if (strcasecmp(argv[i], "PAVG") == 0)
        {
            //printf("func is PAVG");
            checkAggregate("PAVG");
            
        }
        else if (strcasecmp(argv[i],"AVG") == 0)
        {
            //printf("func is AVG");
            checkAggregate("AVG");

        }
        else if (strcasecmp(argv[i],"COUNT") == 0)
        {
            checkAggregate("COUNT");
        }
        
        printf("\n[%d]\t%s\n", i,argv[i]);
    }

    //printf("\n%s", aggFunc);
   
    /*char buffer = 0;
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

    return 0;*/
}

void checkAggregate(char* funcName){
    if (isAggregate == false){
        isAggregate = true;
        aggFunc = funcName;
        printf("the chose function is %s", funcName);
    }else{
        fprintf(stderr, "\nProblem: your are trying to use two aggregate functions at once\n\t-->current specificed function: %s\n\t-->trying to use function: %s", aggFunc,funcName);
    }
}