/*
    COMP 348 - Programming Languages
    Assignment 1 - Due June 5th 2023 @ midnight 
    Naika Jean-Baptiste (40227367)
*/
#include <stdio.h>
#include "aggregate.h"
#include <string.h>

static double count(double* arr, int size);
static double min(double* arr, int size);
static double max(double* arr, int size);
static double sum(double* arr, int size);
static double avg(double* arr, int size);
static double pavg(double* arr, int size);

static const char* funcNames[] = {"COUNT","MIN", "MAX", "SUM", "AVG","PAVG"};
double (*func[6]) (double* arr, int size) = {count,min,max,sum,avg,pavg};


double aggregrate(const char* func, double* arr,int size){

    double val = 0;
    //TODO print error message when size of arr less than 1
    if(size < 0){
        fprintf(stderr, "FATAL ERROR in line %d where", __LINE__);
    }else{
        
        for(int i = 0; i < 6; i++){
            if(strcasecmp(func,funcNames[i]) == 0){
                //val = func[i](arr,size);
            }
        }
    }
    return 0;

}

static double count(double* arr, int size){

    double cnt = (double) size;
    
}
static double min(double* arr, int size){
    double min = arr[0];

    for(int i = 0; i < size; i++){
        if(arr[i] < min ){
            min = arr[i];
        }
    }
    return min;
}


static double max(double* arr, int size){
    double m = 0;

    for(int i = 0; i < size; i++){
        if(arr[i] > m){
            m = arr[i];
        }
    }
    return m;

}

static double sum(double* arr, int size){

    double sumDbl = 0;

    for(int i = 0; i < size; i++){
        sumDbl += arr[i];
    }
    return sumDbl;

}
static double avg(double* arr, int size){

    double sumV = sum(arr,size);
    double c = count(arr,size);
    double average = sumV / c;

    return average;

}

static double pavg(double* arr, int size){

    double mi = min(arr,size);
    double ma = max(arr,size);

    double p = (mi + ma) / 2;
}




