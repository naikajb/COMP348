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
#include "singular.h"
#include "aggregate.h"

int prec = -1;
int size = 0;
int singFuncIdx; // index at which the singular function is;
double singFuncValue;
bool isAggregate = false;
bool isSingular = false;
char *aggFunc;
char *singFunc;
char *filterType;
char *filterOpt;

 
void handleCmdLine(int argc, char const **argv);
void checkAggregate(char *funcName);
void checkSingular(char *funcName, const char **args);
void performActions(double arr[], int sizeVal);

int main(int argc, char const *argv[])
{

    if (argc == 1)
    {
        printf("usage: cat <input file> | mathpipe <function name> <optional parameters> ");
        return 0;
    }
    else
    {
        handleCmdLine(argc, argv);
    }

    // printf("\n%s", aggFunc);

    char buffer = 0;
    // space for values in the input file

    double *valuesArr = (double *)malloc(256 * sizeof(double));
    double value = 0;
    int scanned = 0;
    int n = 0;

    // reads a line by line from stdin
    // in this case will read a line from sample.txt file
    while (fgets(&buffer, 100, stdin) != NULL)
    {
        printf("\t[size-->]%i\n",size);
        if (size == 0)
        {
            int offset = 0;
            // this will look at the line currently in the buffer
            // each double at a time is analysed and put in the array "valuesArr"
            while (sscanf(&buffer + offset, "%lf%n", &value, &scanned) == 1)
            {
                valuesArr[n] = value;
                printf("[%d]\t --> \t%f\n", n, valuesArr[n]);
                n++;
                offset += scanned;
            }
            size = n;
            performActions(valuesArr,size);
        }
        else
        {
            int offset = 0;
            // this will look at the line currently in the buffer
            // each double at a time is analysed and put in the array "valuesArr"
            while (sscanf(&buffer + offset, "%lf%n", &value, &scanned) == 1)
            {
                valuesArr[n] = value;
                printf("[%d]\t --> \t%f\n", n, valuesArr[n]);
                n++;
                offset += scanned;
            }
            performActions(valuesArr, n);
            n = 0;
        }

        // TODO check for the precision and size before performing actions method
        // performActions(valuesArr,);
    }
    free(valuesArr);

    return 0;
}

void checkAggregate(char *funcName)
{
    if (isAggregate == false)
    {
        isAggregate = true;
        aggFunc = funcName;
        // printf("the chosen function is %s", funcName);
    }
    else
    {
        fprintf(stderr, "\nProblem: your are trying to use two aggregate functions at once\n\t-->current specificed function: %s\n\t-->trying to use function: %s", aggFunc, funcName);
    }
}

void checkSingular(char *funcName, const char **args)
{
    if (isSingular == false)
    {
        if (strstr(funcName, "FILTER") != NULL)
        {
            isSingular = true;
            printf("\nmissing implemetation of filter func for options: %s %s", args[singFuncIdx + 1], args[singFuncIdx + 2]);
            singFunc = "filter";
        }
        else if (strstr(funcName, "PRINT") != NULL)
        {
            isSingular = true;
            //printf("\nmissing implemetation of print func");
            singFunc = "print";
        }
        else if (strstr(funcName, "SHIFT") != NULL)
        {
            isSingular = true;
            singFunc = "shift";
        }
    }else{
        fprintf(stderr, "can have two singular functions");
    }
}

void performActions(double arr[], int sizeVal)
{
    if (isAggregate)
    {
        //double var = aggregrate(aggFunc,arr, size);
    }
    else if (isSingular)
    {
        if (strcmp(singFunc, "FILTER") == 0)
        {
            /* code */
        }
        else if (strcmp(singFunc, "PRINT") == 0)
        {
            size_t s = (size_t) size;
            print(arr, s);
        }
        else if (strcmp(singFunc, "SHIFT") == 0)
        {
            // shift(a);
        }
    }
}

void handleCmdLine(int argc, char const **argv)
{
    printf("Function to handle command line inputs:\n");

    for (int i = 1; i < argc; i++)
    {
        if (strcasecmp(argv[i], "sum") == 0)
        {
            // printf("first function is sum");
            checkAggregate("SUM");
        }
        else if (strcasecmp(argv[i], "PAVG") == 0)
        {
            // printf("func is PAVG");
            checkAggregate("PAVG");
        }
        else if (strcasecmp(argv[i], "AVG") == 0)
        {
            // printf("func is AVG");
            checkAggregate("AVG");
        }
        else if (strcasecmp(argv[i], "COUNT") == 0)
        {
            checkAggregate("COUNT");
        }
        else if (strcasecmp(argv[i], "MAX") == 0)
        {
            checkAggregate("MAX");
        }
        else if (strcasecmp(argv[i], "MIN") == 0)
        {
            checkAggregate("MIN");
        }
        else if (strcasecmp(argv[i], "FILTER") == 0)
        {
            if (strcasecmp(argv[i + 1], "EQ") == 0)
            {

                if (sscanf(argv[i + 2], "%lf", &singFuncValue) == 1)
                {
                    filterOpt = "EQ";
                    singFuncIdx = i;
                    checkSingular("FILTER", argv);
                }
            }
            else if (strcasecmp(argv[i + 1], "GEQ") == 0)
            {

                if (sscanf(argv[i + 2], "%lf", &singFuncValue) == 1)
                {
                    singFuncIdx = i;
                    filterOpt = "GEQ";
                    checkSingular("FILTER", argv);
                }
            }
            else if (strcasecmp(argv[i + 1], "NEQ") == 0)
            {

                if (sscanf(argv[i + 2], "%lf", &singFuncValue) == 1)
                {
                    filterOpt = "NEQ";
                    singFuncIdx = i;
                    checkSingular("FILTER", argv);
                }
            }
            else if (strcasecmp(argv[i + 1], "LEQ") == 0)
            {
                if (sscanf(argv[i + 2], "%lf", &singFuncValue) == 1)
                {
                    filterOpt = "LEQ";
                    singFuncIdx = i;
                    checkSingular("FILTER", argv);
                }
            }
            else if (strcasecmp(argv[i + 1], "LESS") == 0)
            {

                if (sscanf(argv[i + 2], "%lf", &singFuncValue) == 1)
                {
                    singFuncIdx = i;
                    filterOpt = "LESS";
                    checkSingular("FILTER", argv);
                }
            }
            else if (strcasecmp(argv[i + 1], "GREATER") == 0)
            {

                if (sscanf(argv[i + 2], "%lf", &singFuncValue) == 1)
                {
                    filterOpt = "GREATER";
                    singFuncIdx = i;
                    checkSingular("FILTER", argv);
                }
            }
            else
            {
                fprintf(stderr, "smtg went wrong with trying initialize the FILTER command");
            }
        }
        else if (strcasecmp(argv[i], "PRINT") == 0)
        {
            singFuncIdx = i;
            checkSingular("PRINT", argv);
        }
        else if (strcasecmp(argv[i], "SHIFT") == 0)
        {
            if(sscanf(argv[i+1], "%lf", &singFuncValue) == 1){
                 singFuncIdx = i;
                checkSingular("SHIFT", argv);
            }else{
                 fprintf(stderr, "smtg went wrong with trying initialize the SHIFT command");
            }
           
        }
        else if (strstr(argv[i], "-size=") != NULL)
        {

            // scans the string for the integer representing size
            while (sscanf(argv[i], "-size=%d", &size) == 1)
            {
                printf("Specified size of arrays --> %d\n", size);
                break;
            }
        }
        else if (strstr(argv[i], "-prec=") != NULL)
        {

            // scans the string for the integer representing precision
            while (sscanf(argv[i], "-prec=%d", &prec) == 1)
            {
                printf("Specified precision of arrays --> %d", prec);
                break;
            }
        }

        //printf("\n\t[%d]\t%s\n", i, argv[i]);
    }

    if (isAggregate == true)
    {
        printf("The chosen aggregate function is %s\n", aggFunc);
    }

    if (isSingular == true)
    {
       
        printf("The chosen singular function is %s with  option %s and value %f\n", singFunc, filterOpt, singFuncValue);
    }
}
