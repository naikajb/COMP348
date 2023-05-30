/*
    COMP 348 - Programming Languages
    Assignment 1 - Due June 5th 2023 @ midnight 
    Naika Jean-Baptiste (40227367)
*/
#include <stdio.h>
#include "aggregate.h"
#include <string.h>

static double count(double* arr, int size);
static double min(double * arr, int size);

double aggregrate(const char* func, double* arr,int size){

    //TODO print error message when size of arr less than 1
    if(size < 0){
        fprintf(stderr, "FATAL ERROR in line %d where", __LINE__);
    }
    return 0;

}


