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

int main(int argc, char const *argv[])
{

   int size = 0;
   int prec = 0;

   //printf("%s\n", argv[0]);
   char buffer = 0;
   for(int i = 1; i < argc; i++){

    const char * arg = argv[i];
    if(strstr(arg,"sum")){
        printf("hello sum\n");
    }else if (strstr(arg,"-size=")){

        printf("hello -size= \n");

    }
    //printf("[%d]\t%s\n", i,argv[i]);
     /*if (strcmp(argv[i],"sum")){
        printf("hello");
     }*/

   }
   
   
   /*while(fgets(&buffer, 10,stdin) != NULL){
        printf("%s",&buffer);
   }*/
   

    return 0;
}
