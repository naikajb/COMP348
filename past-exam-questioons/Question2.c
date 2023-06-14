// What is the output of the following C code? Explain your answer.

// char c[] = "GEEK2018";
// char *p =c;
// printf("%c,%c", *p,*(p+p[3]-p[1]));

#include <stdio.h>
int main(int argc, char const *argv[])
{
    char c[] = "GEEK2018";
    char *p =c;
    printf("%c,%c", *p,*(p+p[3]-p[1]));

    return 0;
}
