/*
    COMP 348 - Programming Languages
    Assignment 1 - Due June 5th 2023 @ midnight 
    Naika Jean-Baptiste (40227367)
*/
#include <stdio.h>
#include "aggregate.h"
#include <string.h>

static double count(double* arr, int size);

const char *func_names = {"COUNT", "MIN", "MAX", "SUM","AVG","PAVG"};

double aggregrate(const char* func, double* arr,int size){

    //TODO print error message when size of arr less than 1
    if(size < 0){
        fprintf(stderr, "FATAL ERROR in line %d where", __LINE__);
    }
    return 0;

    if(strcmp(func,func_names[0])){
        return count(arr,size);
    }
}


