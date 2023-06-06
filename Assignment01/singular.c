/*
    COMP 348 - Programming Languages
    Assignment 1 - Due June 5th 2023 @ midnight 
    Naika Jean-Baptiste (40227367)
*/
#include <stdio.h>
#include <stdlib.h>
#include "singular.h"


void print(double a[], size_t size){
    
    for(size_t i = 0; i < size; i++){
        fprintf(stdout,"[%zu]\t%f",i,a[i]);
    }
    //printf("%d\n", prec);
}
void shift(double a[], size_t size, double by){
    for(int i = 0; i < size; i++){

    }
}

/*size_t filter(double a[], size_t count, filter_type t, double threshold){
    
}*/

