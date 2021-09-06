#include <stdio.h>
#include <string.h>

// 자료형
// 기초 자료형 (char, int, short, float, double)
// 파생 자료형 (배열, 포인터, 구조체, 공용체, 함수형)
// 사용자 정의 자료형 (typedef, enum)

// 구조체 정의
// 기본 자료형만으로 표현하지 못하는 복잡한 형 (예를 들면 사람 정보)

struct Person {
    char name[100];
    int age;
    int height;
    int weight;
};

struct Point2D {
    int x;
    int y;
};

// int main (int args, const char * argv[]) {

//     struct Person personA, personB;

//     strcpy(personA.name, "GilDong");
//     personA.age = 20;
//     personA.height  = 179;
//     personA.weight = 73.2;

//     strcpy(personB.name, "Gilsun");
//     personB.age = 23;
//     personB.height = 166;
//     personB.weight = 58.2;

//     struct Point2D p1, p2;
//     p1.x = 100;
//     p1.y = 100;
//     p2 = p1; // 구조체 복사

//     // 구조체 초기화
//     // 정의된 순서대로 입력
//     struct Person personC = {"Park", 40, 170, 66};
//     printf("personC의 이름 = %s, 나이 = %d\n", personC.name, personC.age);

//     return 0;
// }

// 구조체를 멤버로 가지는 구조체 (가능)
// 구조체의 대입연산 (가능)
// 구조체의 비교연산 또는 사칙연산 (불가)
// 구제초의 배열선언 (가능)

struct point {
    int x;
    int y;
};

struct rect {
    struct point p1;
    struct point p2;
};

int main(void) {
    struct rect r;
    int width, height, area, peri;

    printf("왼쪽 상단의 좌표를 입력하시오 : ");
    scanf("%d %d", &r.p1.x, &r.p1.y);

    printf("왼쪽 상단의 좌표를 입력하시오 : ");
    scanf("%d %d", &r.p2.x, &r.p2.y);

    width = r.p2.x - r.p1.x;
    height = r.p2.y - r.p1.y;

    area = width * height;
    peri = 2 * width + 2 * height;
    printf("사각형의 면적은 %d이고, 둘레는 %d입니다.\n", area, peri);

    struct rect new_r;

    new_r = r; // 대입 가능
    // .. struct rect rx = r * new_r; 연산 불가
    // .. if (r < new_r) 비교 불가
    struct rect array_r[10]; // 구조체 배열 가능

    return 0;
}