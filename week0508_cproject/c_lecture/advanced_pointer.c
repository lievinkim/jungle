// 포인터
// C의 변수
// 다른 객체를 참조하기 위해 사용
// 일반 변수를 통해서도 메모리에 값을 저장하고 불러올 수 있음
// 그러나 포인터를 사용하면 일반적인 방식에서 허용되지 않는 접근이 가능
// 도서관에서 책을 찾을 때 책의 인덱스를 확인하고 찾아가는 것이 효율적
// 책 - 데이터
// 인덱스 - 데이터 주소
// 책의 물리적인 존재와 구분되는 논리적인 정렬이 가능하듯 데이터도 동일하게 적용 가능
// sizeof를 활용하여 자료형이나 변수의 크기를 얻을 수 있음
// 주소연산자 : & (실행할 때마다 변경됨
// 변수를 참조한다고 표현함

#include <stdio.h>

int main(int argc, const char * argv[]) {

    int *myPointer;
    int myVar = 10;
    
    printf("myVar = %d\n", myVar);
    myPointer = &myVar; //myPointer는 myVar 변수를 참조한다.

    *myPointer = 20; //myPointer가 참조하는 변수의 값을 20으로 변경한다.
    printf("\n*myPoitner = 20으로 변경\n");
    printf("myVar = %d\n", myVar);

    printf("NULL value = %p\n", NULL);

    return 0;
}

// NULL 값
// C 컴파일러에서 0으로 추정하는 값
// 포인터 변수를 초기화할 때 주로 사용하며 이때 포인터 변수는 아무것도 가리키지 않는다는 것을 의미한다.