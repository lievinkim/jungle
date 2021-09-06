// 포인터와 배열
// int a[10];
// a[0] = *a or *(a+0) 동일한 표현식
// a[1] = *(a+1) 동일한 표현식
// 배열명 a는 a[0]의 변수를 참조하고 있기 때문

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a[5] = {20, 30, 40};

    // a와 &a[0]의 값을 확인
    printf("a = %p, &a[0] = %p \n", a, &a[0]);

    // a[i]와 *(a+i)의 값을 확인
    for (int i=0; i<5; i++) {
        printf("a[%d] = %d, *(a+%d) = %d \n", i, a[i], i, *(a+i));
    }

    // 동적 할당 메모리

    int* b;
    b = (int* )malloc(5*sizeof(int));
    if (b == NULL) {
        printf("메모리 할당 에러 \n");
        return -1;
    }
    *(b+0) = 20;
    *(b+1) = 30;
    *(b+2) = 40;
    *(b+3) = 0;
    *(b+4) = 0;

    for (int i=0; i<5; i++) {
        printf("b[%d] = %d, *(b+%d) = %d \n", i, b[i], i, *(b+i));
    }

    free(b);
    return 0;
}

// 동적 할당 메모리를 배열로 사용 가능
