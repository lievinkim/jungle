#include <stdio.h>
#include <stdlib.h>

int main(void) {

    // 1. 배열
    // int subway_1 = 30;
    // int subway_2 = 40;
    // int subway_3 = 50;
    // printf("지하철 1호차에 %d 명이 타고 있습니다.", subway_1);
    // printf("지하철 2호차에 %d 명이 타고 있습니다.", subway_2);
    // printf("지하철 3호차에 %d 명이 타고 있습니다.", subway_3);
    // int subway_array[3];
    // subway_array[0] = 30;
    // subway_array[1] = 40;
    // subway_array[2] = 50;
    // for(int i=0; i<3; i++) {
    //     printf("지하철 %d호차에 %d 명이 타고 있습니다.\n", i+1, subway_array[i]);
    // }
    // int arr[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    // for (int i=0; i<10; i++) {
    //     printf("%d\n", arr[i]);
    // }
    // int size = 10;
    // // int arr[size]; // 상수값이 들어 와야 함
    // int arr[10] = {1, 2}; // 3번째 값부터는 자동으로 '0'이 들어감. 단순 선언 시에는 더미값이 들어감
    // int arr[] = {1, 2}; // 배열의 길이가 자동으로 2가 됨
    // float arr_f[5] = { 1.0f, 2.0f, 3.0f}; // 나머지 값은 자동으로 '0.0'이 들어감
    // for (int i=0; i<5; i++) {
    //     printf("%.2f\n", arr_f[i]);
    // }

    // 2. 문자와 문자열
    // char c = 'A';
    // printf("%c\n", c);
    // char str[6] = "coding"; // 6개의 문자 공간을 열어서 삽입
    // printf("%s\n", str);
    // char str[] = "coding";
    // printf("%s\n", str);
    // for (int i=0; i<sizeof(str); i++) {
    //     printf("%c\n", str[i]);
    // }
    // char kor[] = "나도코딩";
    // printf("%s\n", kor);
    // printf("%ld\n", sizeof(kor));

    // 3. 문자열 심화
    // char c_array[7] = { 'c', 'o', 'd', 'i', 'n', 'g', '\0'};
    // char c_array[6] = { 'c', 'o', 'd', 'i', 'n', 'g'};
    // printf("%s\n", c_array);
    // char c_array[10] = {'c', 'o', 'd', 'i', 'n', 'g'};
    // printf("%s\n", c_array);
    // for (int i=0; i<sizeof(c_array); i++) {
    //     printf("%c\n", c_array[i]);
    // }
    // for (int i=0; i<sizeof(c_array); i++) {
    //     printf("%d\n", c_array[i]); // ASCII 코드 값 출력 (null 문자는 0으로)
    // }
    // char name[256];
    // printf("이름을 입력하세요 : ");
    // scanf("%s", name);
    // printf("%s\n", name);
    // 아스키 코드
    // printf("%c\n", 'a');
    // printf("%d\n", 'a');
    // printf("%c\n", 'b');
    // printf("%d\n", 'b');
    // printf("%c\n", 'A');
    // printf("%d\n", 'A');
    // printf("%c\n", '\0');
    // printf("%d\n", '\0');
    // printf("%c\n", '0');
    // printf("%d\n", '0');
    // printf("%c\n", '1');
    // printf("%d\n", '1');
    // for (int i = 0; i<128; i++) {
    //     printf("아스키 코드 정수 %d : %c\n", i, i);
    // }

    return 0;
}