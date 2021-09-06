// 연결 리스트
// 리스트 - 순서를 가진 항목들의 모임, 대표적인 선형 자료구조, 노드들이 일렬로 연결된 구조
// 이때, 노드는 데이터와 다른 노드에 대한 포인터를 갖는다.
// 연결 리스트는
   // 링크의 갯수 : 단일 연결 리스트, 이중 연결 리스트
   // 링크의 순환 구조 : 선형 연결 리스트, 원형 연결 리스트
// 연결 리스트 vs 배열

// 연결 리스트 구성 요소
// 노드 = <항목, 링크>
// 항목 = 데이터 필드
// 링크 = 다음 노드에 대한 주소

// -> 표기법은 구조체를 참조하고 있는 포인터로 구조체의 멤버에 접근할 때
// (*ptr).data 대신 ptr->data로 보다 쉽게 표현할 수 있는 방법

#include <stdio.h>
#include <stdlib.h>

typedef int item;
typedef struct ListNode {
    item data;
    struct ListNode *link;
} ListNode;

int main(void) {
    ListNode node = {100, NULL};
    ListNode* list = &node;

    printf("node.data = %d\n", node.data);
    printf("(*list).data = %d\n", (*list).data);
    printf("list->data = %d\n", list->data);

    ListNode* p1;
    ListNode* p2;
    
    p1 = (ListNode* )malloc(sizeof(ListNode));
    p1->data = 20;

    p2 = (ListNode* )malloc(sizeof(ListNode));
    p2->data = 30;

    p1->link = p2;
    p2->link = NULL;

    printf("p1->data = %d\n", p1->data);
    printf("p1->link->data = %d\n", p1->link->data);
    printf("p2->data = %d\n", p2->data);

    return 0;
}

