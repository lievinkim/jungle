#include <stdio.h>

struct GameInfo {
    char* name;
    int year;
    int price;
    char* company;

    struct GameInfo* friendGame;
};

typedef struct GameInformation {
    // GameInformation 이름 활용 가능
    // GameInformation 삭제해도 사용 가능
    char* name;
    int year;
    int price;
    char* company;

    struct GameInfo* friendGame;
} GAME_INFO;

int main(void) {

    // 일반적인 사용
    char* name = "나도게임";
    int year = 2017;
    int price = 50;
    char* company = "나도회사";

    // 구조체 활용 1
    struct GameInfo gameInfo1;
    gameInfo1.name = "나도게임2";
    gameInfo1.year = 2018;
    gameInfo1.price = 80;
    gameInfo1.company = "나도회사";
    printf("### 게임 출시 정보 ###\n");
    printf("  게임명   : %s\n", gameInfo1.name);
    printf("  발매년도  : %d\n", gameInfo1.year);
    printf("  가격     : %d\n", gameInfo1.price);
    printf("  제작사   : %s\n\n", gameInfo1.company);

    // 구조체 활용 2
    struct GameInfo gameInfo2 = {"나도게임3", 2019, 90, "나도회사"};
    printf("### 게임 출시 정보 ###\n");
    printf("  게임명   : %s\n", gameInfo2.name);
    printf("  발매년도  : %d\n", gameInfo2.year);
    printf("  가격     : %d\n", gameInfo2.price);
    printf("  제작사   : %s\n\n", gameInfo2.company);

    // 구조체 배열
    struct GameInfo gameArray[2] = {
        {"나도게임4", 2020, 100, "나도회사"},
        {"나도게임5", 2021, 100, "나도회사"}
    };

    // 구조체 포인터
    struct GameInfo* gamePtr;
    gamePtr = &gameInfo1;
    printf("### 게임 출시 정보 ###\n");
    printf("  게임명   : %s\n", (*gamePtr).name);
    printf("  발매년도  : %d\n", (*gamePtr).year);
    printf("  가격     : %d\n", (*gamePtr).price);
    printf("  제작사   : %s\n\n", (*gamePtr).company);
    printf("### 게임 출시 정보 ###\n");
    printf("  게임명   : %s\n", gamePtr->name);
    printf("  발매년도  : %d\n", gamePtr->year);
    printf("  가격     : %d\n", gamePtr->price);
    printf("  제작사   : %s\n\n", gamePtr->company);

    // 구조체 안의 구조체
    gameInfo1.friendGame = &gameInfo2;
    printf("### 자사 게임 출시 정보 ###\n");
    printf("  게임명   : %s\n", gameInfo1.friendGame->name);
    printf("  발매년도  : %d\n", gameInfo1.friendGame->year);
    printf("  가격     : %d\n", gameInfo1.friendGame->price);
    printf("  제작사   : %s\n\n", gameInfo1.friendGame->company);

    // typedef
    // 자료형에 별명 지정
    int i = 1;
    typedef int 정수;
    typedef float 실수;
    정수 정수변수 = 3; // int i = 3;과 동일
    실수 실수변수 = 3.23f;
    printf("\n\n정수변수 : %d, 실수변수 : %.2f\n\n", 정수변수, 실수변수);

    typedef struct GameInfo 게임정보;
    게임정보 game1;
    game1.name = "한글 게임";
    game1.year = 2015;

    GAME_INFO game2;
    game2.name = "한글 게임2";
    game2.year = 2016;

    return 0;
}