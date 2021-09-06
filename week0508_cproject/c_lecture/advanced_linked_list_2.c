// 연결 리스트 만들기
// 단순 연결 리스트
// 하나의 링크 필드 사용
// 링크의 시작 포인터를 유지 (헤더 노드)
// 마지막 노드의 링크 값은 NULL로 유지

#include <stdio.h>
#include <stdlib.h>

typedef char item;
typedef struct ListNode {
    item data;
    struct ListNode* link;
} ListNode;

int main(void) {

    ListNode* head,* current,* new_node;
    head = current = new_node = NULL; // 초기화 작업
    item n;

    printf("문자 데이터를 입력하세요 : ");
    while (scanf("%c\n", &n) != EOF) {

        new_node = (ListNode* )malloc(sizeof(ListNode));
        new_node->data = n;
        new_node->link = NULL;

        if (head == NULL) {
            head = new_node;
            current = new_node;
        } else {
            current->link = new_node;
            current = new_node;
        }
    }

    printf("연결리스트의 원소들은 다음과 같습니다.\n");
    current = head;
    while (current != NULL) {
        printf("%c", current->data);
        current = current->link;
    }

    return 0;
}