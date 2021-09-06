// 동적 메모리 할당

// 정적 메모리 할당이란 프로그램이 시작되기 전 미리 정해진 메모리를 할당하는 것
// 처음에 결정된 크기의 값만 처리함

// 프로그램 실행 도중 메모리 할당 받음
// 운영체제의 힙 영역의 메모리를 할당 받아 사용
// 운영체제에 프로그램이 필요로 하는 메모리 용량 알려줘야 함
// 또한 할당된 메모리의 주소를 알아야 사용할 수 있음
// malloc() 함수
// malloc() 함수는 할당된 메모리의 주소값을 반환함 (memory allocate)

// int* ip; // 동적으로 할당 받은 기억 공간을 참조하는 포인터 변수
// ip = (int*)malloc(sizeof(int)) // 동적으로 기억 공간을 할당
// *ip = 20; // 동적으로 할당받은 기억공간을 사용하여 20의 값을 할당
// free(ip);

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int* ip;
    double* dp;

    ip = (int* )malloc(sizeof(int));
    dp = (double* )malloc(sizeof(double));

    *ip = 10;
    *dp = 3.4;

    printf("정수형 포인터 변수의 값 : %d\n", *ip);
    printf("실수형 포인터 변수의 값 : %lf\n", *dp);

    free(ip);
    free(dp);
    return 0;
}

// malloc() 함수
// 원형 : void* malloc (size_t size);
// size는 바이트 값이며 malloc() 함수는 메모리 블럭의 첫번째 바이트에 대한 주소를 반환
// 할당할 수 없을 경우 NULL 반환
// 반환한 값은 반드시 포인터 변수가 받아야 함

// free() 함수
// 동적으로 할당된 메모리 블럭의 사용이 종료되는 경우 시스템 반납
// 반납 안하면 시스템 성능 저하 -> 메모리 누수(leak)라고 하면 사용되지 않는 메모리 블럭을 가비지(garbage) 메모리라고 함