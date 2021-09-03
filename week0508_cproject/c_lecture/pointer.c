#include <stdio.h>

void swap (int a, int b);
void swap_addr (int* a, int* b);
void changeArray(int* ptr);

int main(void) {

    // 1. 포인터
    // // 철수네 : 101호 (실제는 메모리 공간)
    // // 영희네 : 102호
    // // 민수네 : 103호
    // // 각 문 앞에 '암호'가 걸려 있음
    // int cheol = 1;
    // int young 1= 2;
    // int min = 3;
    // printf("철수네 주소 : %d, 암호 : %d\n", &cheol, cheol);
    // printf("영희네 주소 : %d, 암호 : %d\n", &young, young);
    // printf("민수네 주소 : %d, 암호 : %d\n", &min, min);
    // // mission 
    // int *mission;
    // mission = &cheol;
    // printf("미션맨이 방문하는 곳 주소 : %d, 암호 : %d\n", mission, *mission);
    // mission = &young;
    // printf("미션맨이 방문하는 곳 주소 : %d, 암호 : %d\n", mission, *mission);
    // mission = &min;
    // printf("미션맨이 방문하는 곳 주소 : %d, 암호 : %d\n", mission, *mission);
    // mission = &cheol;
    // *mission = *mission * 3;
    // printf("미션맨이 암호를 변경한 곳 주소 : %d, 암호 : %d\n", mission, *mission);
    // mission = &young;
    // *mission = *mission * 3;
    // printf("미션맨이 암호를 변경한 곳 주소 : %d, 암호 : %d\n", mission, *mission);
    // mission = &min;
    // *mission = *mission * 3;
    // printf("미션맨이 암호를 변경한 곳 주소 : %d, 암호 : %d\n", mission, *mission);
    // // spy
    // int *spy = mission;
    // printf("\n ... 스파이가 미션 수행하는 중 ... \n\n");
    // spy = &cheol;
    // *spy = *spy - 2;
    // printf("스파이가 방문하는 곳 주소 : %d, 암호 : %d\n", spy, *spy);
    // spy = &young;
    // *spy = *spy - 2;
    // printf("스파이가 방문하는 곳 주소 : %d, 암호 : %d\n", spy, *spy);
    // spy = &min;
    // *spy = *spy - 2;
    // printf("스파이가 방문하는 곳 주소 : %d, 암호 : %d\n", spy, *spy);
    // printf(" ... 철수, 영희, 민수는 집에 오고 바뀐 암호를 보고 깜 놀 ... \n\n");
    // printf("철수네 주소 : %d, 암호 : %d\n", &cheol, cheol);
    // printf("영희네 주소 : %d, 암호 : %d\n", &young, young);
    // printf("민수네 주소 : %d, 암호 : %d\n", &min, min);
    // printf("미션맨의 주소 : %d\n", &mission);
    // printf("스파이의 주소 : %d\n", &spy);

    // 2. 배열
    // int arr[3] = {5, 10, 15};
    // int *ptr = arr;
    // for (int i=0; i<3; i++) {
    //     printf("배열 arr[%d]의 값 : %d\n", i, arr[i]);
    // }
    // for (int i=0; i<3; i++) {
    //     printf("포인터 ptr[%d]의 값 : %d\n", i, ptr[i]);
    // }
    // ptr[0] = 100;
    // ptr[1] = 200;
    // ptr[2] = 300;
    // for (int i=0; i<3; i++) {
    //     //printf("배열 arr[%d]의 값 : %d\n", i, arr[i]);
    //     printf("배열 arr[%d]의 값 : %d\n", i, *(arr + i)); // 위 문법과 완전 동일
    // }
    // for (int i=0; i<3; i++) {
    //     printf("포인터 ptr[%d]의 값 : %d\n", i, ptr[i]);
    // }
    // printf("arr 자체의 주소 : %d\n", arr);
    // printf("arr[0]의 주소 : %d\n", &arr[0]);
    // printf("arr 자체의 주소가 가지는 값 : %d\n", *arr);
    // printf("arr[0]의 주소가 가지는 값 : %d\n", *&arr[0]);

    // 3. Swap
    // int a = 10;
    // int b = 20;
    // printf("a의 주소 : %d\n", &a);
    // printf("b의 주소 : %d\n", &b);
    // printf("swap 함수 전 => a : %d, b : %d\n", a, b);
    // swap(a,b);
    // printf("swap 함수 후 => a : %d, b : %d\n", a, b);
    // printf(" ... 처음부터 주소값을 전달한다면? ... ");
    // printf("swap_addr 함수 전 => a : %d, b : %d\n", a, b);
    // swap_addr(&a,&b);
    // printf("swap_addr 함수 후 => a : %d, b : %d\n", a, b);

    // 4. 포인터로 배열 값 변경하기
    // int arr2[3] = {10, 20, 30};
    // //changeArray(arr2); // 배열 자체가 주소값을 반환하기 때문 & 표시할 필요가 없음
    // changeArray(&arr2[0]); // 위 내용과 결과는 똑같음
    // for (int i=0; i<3; i++) {
    //     printf("%d\n", arr2[i]);
    // }

    return 0;
}

void swap (int a, int b) {

    // 아래 방법대로 작성하는 경우 함수 내에서만 바뀌고 실제로 바뀌지 않음
    // 주소를 찾아보면 알 수 있음. 이를 값에 의한 복사라고 함 (call by value)
    printf("a의 주소 : %d\n", &a);
    printf("b의 주소 : %d\n", &b);
    int temp = a;
    a = b;
    b = temp;
}

void swap_addr (int* a, int* b) {

    printf("a의 주소 : %d\n", a);
    printf("b의 주소 : %d\n", b);
    int temp = *a;
    *a = *b;
    *b = temp;
}

void changeArray(int* ptr) {
    ptr[2] = 50;
}