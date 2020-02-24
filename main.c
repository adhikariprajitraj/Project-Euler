#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i;
    int sum = 0;
for (int i = 0; i < 1000; i++)
{
    if ((i % 3 == 0) || (i % 5 == 0))
    {
        sum = sum + i;
       // printf("%d \n", sum);
    }
}
    printf("%d", sum);
    return 0;
}
