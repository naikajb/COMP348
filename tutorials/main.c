#include <stdio.h>

void print(double a[], int size){
    for(int i = 0; i < size; i++){
        printf("%d",a[i]);
    }
    printf("\n");
}
int main(int argc, char const *argv[])
{
    double b[5] = {4, 5, 6, 7, 8};
    print(b,5);
    return 0;
}
