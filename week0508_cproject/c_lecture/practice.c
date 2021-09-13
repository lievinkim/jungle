#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int x = 1, y = 2;
    int *p_x = &x;

    y = *p_x;
    printf("%d\n", y);

    *p_x = 0;
    printf("%d", x);

}