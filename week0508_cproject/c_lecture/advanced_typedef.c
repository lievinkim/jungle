// typedef
// 새로운 자료형을 정의하는 역할
// C의 기본 자료형 확장

typedef unsigned char BYTE;
BYTE index; // unsigend char index;와 동일

typedef int INT32; 
typedef unsigned int UNIT32;

INT32 i; // int i;와 동일
UNIT32 k; // unsigned int k;와 동일

struct Person {
    char name[100];
    int age;
    int height;
    float weight;
};

typedef struct Person Person;

// struct Point2D {
//     int x;
//     int y;
// };
// typedef struct Point2D Point2D;

typedef struct Point2d {
    int x;
    int y;
} Point2D;

// int main(int argc, const char * argv[]) {
//     struct Person PersonA, PersonB;
//     // vs
//     Person PersonC, PersonD;
    
//     // struct Point2D p1, p2;
//     // vs
//     Point2D p3, p4;
// }

// 새롭게 정의한 typedef 자료형은 함수의 매개변수 및 반환값으로도 적용 가능
// 배열 자체도 typedef로 정의 가능

typedef float Vector[2];

int main(int argc, const char * argv[]) {
    Vector v1, v2;
    v1[0] = 10.0f;
    v1[1] = 10.0f;

    printf("v1[0] = %4.2f, v1[1] = %4.2f \n", v1[0], v1[1]);
    
    // v2 = v1; 불가
    // 배열형은 원소 단위로만 assign 가능하면 전체 단위로는 불가

    printf("v2[0] = %4.2f, v2[1] = %4.2f \n", v1[0], v1[1]);
    return 0;
}