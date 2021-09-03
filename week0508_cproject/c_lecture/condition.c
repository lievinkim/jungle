#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void) {

    // 1. if 조건문
    // int age_1 = 15;
    // if(age_1>=20) {
    //     printf("일반인 입니다.\n");
    // } else {
    //     printf("학생입니다.\n");
    // }
    // int age_2 = 8;
    // if(age_2>=8 && age_2<=13) {
    //     printf("초등학생입니다.\n");
    // } else if (age_2>=14 && age_2<=16) {
    //     printf("중학생입니다.\n");
    // } else if (age_2>=17 && age_2<=19) {
    //     printf("고등학생입니다.\n");
    // } else {
    //     printf("학생이 아닙니다.\n");
    // }

    // 2. break와 continue
    // for (int i=1; i<=30; i++) {
    //     if(i>=6) {
    //         printf("나머지 학생은 집에 가세요.\n");
    //         break;
    //     }
    //     pintf("%d 번 학생은 조별 발표 준비를 하세요.\n", i);
    // }
    // for (int i=1; i<=30; i++) {
    //     if (i>=6 && i<=10) {
    //         if (i==7) {
    //             printf("%d 번학 생은 결석입니다.\n", i);
    //             continue;
    //         }
    //         printf("%d 번 학생은 발표 준비를 하세요.\n", i);
    //     }
    // }
    // // && ||
    // int a = 10;
    // int b = 10;
    // int c = 12;
    // int d = 13;
    // if (a==b || c==d) {
    //     printf("a와 b 혹은 c와 d의 값이 같습니다.\n");
    // } else {
    //     printf("값이 서로 다릅니다.\n");
    // }
    // // 난수 함수
    // srand(time(NULL)); // 난수 초기화
    // int num = rand() % 3; // 0~2 중에 하나 선택
    // printf("난수 초기화 이전 \n");
    // for (int i=0; i<10; i++) {
    //     printf("%d ", rand() % 10 + 1); // 0~9를 1~10으로 변경
    // }
    // srand(time(NULL)); // 난수 초기화
    // printf("\n난수 초기화 이후 \n");
    // for (int i=0; i<10; i++) {
    //     printf("%d ", rand() % 10);
    // }
    // // 가위, 바위, 보 (1)
    // srand(time(NULL));
    // int i = rand() % 3;
    // if (i==0) {
    //     printf("가위\n");
    // } else if (i==1) {
    //     printf("바위\n");
    // } else if (i==2) {
    //     printf("보\n");
    // }
    // // 가위, 바위, 보 (2)
    // srand(time(NULL));
    // int i = rand() % 3;
    // switch (i) {
    //     case 0: printf("가위\n"); break;
    //     case 1: printf("바위\n"); break;
    //     case 2: printf("보\n"); break;
    //     default: printf("몰라요\n"); break;
    // }

    // 3. 프로젝트
    // srand(time(NULL));
    // int num = rand() % 100 + 1; // 1~100 사이의 숫자
    // printf("숫자 : %d\n", num);
    // int answer = 0;
    // int chance = 5;
    // while (chance>0) {
    //     printf("남은 기회 %d 번\n", chance--);
    //     printf("숫자를 맞혀보세요 (1~100) : ");
    //     scanf("%d", &answer);
    //     if (answer>num) {
    //         printf("DOWN \n\n");
    //     } else if (answer<num) {
    //         printf("UP \n\n");
    //     } else if (answer==num) {
    //         printf("정답입니다! \n");
    //         break;
    //     }
    //     printf("모든 기회를 다 사용하셨습니다.\n");
    // }

    return 0;
}