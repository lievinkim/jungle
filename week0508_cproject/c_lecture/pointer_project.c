#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int level;
int arrayFish[6];
int* cursor;

void initData();
void printFishes();
void decreaseWater(long elapsedTime);
int checkFishAlive();

// 물고기 게임
int main(void) {
    long startTime = 0; // 게임 시작 시간
    long totalElapsedTime = 0; // 총 경과 시간
    long prevElapsedTime  = 0; // 직전 경과 시간

    int num; // 몇 번 어항에 물을 줄 것인지 사용자가 입력
    initData(); // 게임 초기화

    cursor = arrayFish; //배열과 똑같이 쓸 수 있음

    startTime = clock();
    while (1) {
        printFishes();
        printf("몇 번 어항에 물을 주시겠어요? ");
        scanf("%d", &num);

        if (num<1 || num>6) {
            printf("\n입력값이 잘못되었습니다.\n");
            continue;
        }
        
        // 총 경과 시간
        long current = clock();
        long totalElapsedTime = (current - startTime)/100;
        // long totalElapsedTime = (current-startTime)/CLOCKS_PER_SEC;
        printf("총 경과 시간 : %ld 초\n", totalElapsedTime);

        // 직전에 물 준 시간 이후로 흐른 시간
        prevElapsedTime = totalElapsedTime - prevElapsedTime;
        printf("최근 경과 시간 : %ld 초\n", prevElapsedTime);

        // 어항의 물을 감소
        decreaseWater(prevElapsedTime);

        // 사용자 입력한 어항에 물을 준다
        if (cursor[num-1] <= 0) {
            printf("%d 번 물고기는 이미 죽었습니다.. 물을 주지 않습니다.\n", num);
        } else if (cursor[num-1]+1<=100) {
            printf("%d 번 어항에 물을 줍니다.\n", num);
            cursor[num-1] += 1;
        }

        // 레벨업을 할 건지 확인
        if (totalElapsedTime/20 > level-1) {
            level++;
            printf("***축 레벨업*** %d 레벨에서 %d 레벨로 업그레이드!\n\n", level-1, level);

            if (level == 5) {
                printf("\n\n축하합니다. 최고 레벨을 달성하였습니다. 게임을 종료합니다.\n\n");
                exit(0);
            }
        }

        if (checkFishAlive() == 0) {
            printf("모든 물고기가..ㅠㅠ 흑흑..\n");
            exit(0);
        } else {
            printf("물고기가 아직 살아 있어요!\n");
        }
        prevElapsedTime = totalElapsedTime;

    }


    return 0;
}

void initData() {
    level = 1;
    for (int i=0; i<6; i++) {
        arrayFish[i] = 100; //어항의 물 높이
    }
}

void printFishes() {
    printf("%3d번 %3d번 %3d번 %3d번 %3d번 %3d번\n", 1, 2, 3, 4, 5, 6);
    for (int i=0; i<6; i++) {
        printf(" %4d ", arrayFish[i]);
    }
    printf("\n\n");
}

void decreaseWater(long elapsedTime) {
    for (int i=0; i<6; i++) {
        arrayFish[i] -= (level*3*(int)elapsedTime);
        if (arrayFish[i] < 0) {
            arrayFish[i] = 0;
        }
    }
}

int checkFishAlive() {
    for (int i=0; i<6; i++) {
        if (arrayFish[i]>0) {
            return 1;
        }
    }
    return 0;
}