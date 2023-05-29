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
int main(int argc, char const *argv[])
{
    
   //int number = 0;
   char buffer = 0;

   while(fgets(&buffer, 10,stdin) != NULL){
        printf("%s",&buffer);
   }
    return 0;
}
