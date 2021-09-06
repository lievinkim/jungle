// 포인터와 함수
// 함수는 특정 작업을 수행하는 독립적인 부분으로 재사용을 통해 코드의 중복을 줄여줌
// 함수 선언, 함수 구현, 호출의 형태로 이루어짐

// 호출된 함수로 전달된 매개변수는 지역 변수로 할당되기 때문에 실행 후 소멸됨
// 이를 값에 의한 호출 (call by value)라고 부름
// return 키워드를 통해 단 하나의 값만을 전달할 수 있음

// 변수 자체를 바꾸고 싶다면 포인터를 활용해야 함
// 이때 호출된 함수로 전달된 매개변수는 변수의 주소를 가져오게 됨
// 이를 주소에 의한 호출 (call by address)라고 부름

// 대표적인 예 swap 함수

#include <stdio.h>

void swap(int x, int y);
void swap_ptr(int* px, int* py);

int main(void) {
    int a = 100, b = 200;

    printf("a = %d, b = %d\n", a, b);
    swap(a, b);
    printf("a = %d, b = %d\n", a, b);
    swap_ptr(&a, &b);
    printf("a = %d, b = %d\n", a, b);

    return 0;
}

void swap(int x, int y) {
    int tmp;
    printf("swap() x = %d, y = %d\n", x, y);
    tmp = x;
    x = y;
    y = tmp;
    printf("swap() x = %d, y = %d\n", x, y);
}

void swap_ptr(int* px, int* py) {
    int tmp;

    tmp = *px;
    *px = *py;
    *py = tmp;
}