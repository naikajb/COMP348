/*
    a0 = 3;
    ak = 2 * ak-1 - 1; for k > 0
*/

// Write a function in C that receives two arguments: a pointer to an array of integers, and an integer 𝑛, and generates the first  𝑛 elements of the above sequence and stores them sequentially in input array. The function returns the number of generated elements.

// Notes:

// If the input n is less than or equal to 0, nothing is generated.

// If a NULL pointer is passed, the function simply returns and leaves the array untouched.

// Calling the function with 1,  stores the first element ( 𝑎0 ) in the destination array.

// The function must strictly use pointers to access the array.


#include <stdio.h>

int generate(int *arr, int n);

int main()
{
    int arr[10];
    int n = 5;
    int i = generate(arr, n);
    printf("%d elements were created\n", i);
    for(int k = 0; i < n; k++){
        printf("%d ", arr[k]);
    }
    return 0;
}

int generate(int * arr, int n){
    if (arr == NULL){
        return 0;
    }
    int generated = 1;
    if (n <= 0){
        arr[0] = 3;
    }else{
        int prev = 3;
        arr[0] = 3;

        for(int i = 1; i < n; i++){
            arr[i] = 2 * prev - 1;
            prev = arr[i];
            generated++;
        }
    }
    return generated;
}
