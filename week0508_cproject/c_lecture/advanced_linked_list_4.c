// 이중포인터를 이용한 삽입

// void insert_node(ListNode *phead, ListNode *prev, ListNode *new);
// 단일포인터를 이용하여 삽입하는 경우, 다음의 문제가 발생한다.
// head의 값을 함수에서는 변경하지만 main 함수에서는 변경되지 않는다.

// void insert_node(ListNode **phead, ListNode *prev, ListNode *new);
// main 함수의 head 주소값을 가져와 값을 변경하게 된다.


// 연결 리스트의 삭제
// 연결 리스트의 노드는 동적으로 삽입, 삭제할 수 있음
// 노드 삭제 후 free() 함수를 통해 heap 메모리로 반납

// 헤드 노드 삭제할 경우,
// 헤드 노드를 temphead에 대입하고,
// 다음 노드를 헤드 노드로 지정한 다음,
// temphead의 메모리를 반납(free)한다

// 삭제노드 이전노드를 알 경우,
// 이전노드의 link에 삭제노드의 link 값을 넣어주고,
// 삭제노드의 메모리를 반납(free)한다.
// 그러나 이전노드의 정보를 잘못 입력하면 심각한 문제를 초래하게 된다.
// 따라서 노드를 순회하면서 특정 값을 만날 경우 삭제하는 방식으로 해결해야 한다.

#include <stdio.h>
#include <stdlib.h>

typedef int item;
typedef struct ListNode {
    item data;
    struct ListNode *link;
} ListNode;

void insert_node(ListNode **phead, ListNode *prev_node, ListNode *new_node);
void remove_head(ListNode **phead);
void display_head(ListNode **phead);
void remove_node(ListNode **phead, ListNode *prev, ListNode *remove);
void display_list(ListNode *head);

int main(void) {
    ListNode *head = NULL, *prev_node = NULL;
    ListNode *node1, *node2;

    node1 = (ListNode *)malloc(sizeof(ListNode));
    node2 = (ListNode *)malloc(sizeof(ListNode));

    // 헤드 노드 삭제 예시
    // node1->data = 100;
    // insert_node(&head, prev_node, node1);
    // prev_node = node1;

    // node2->data = 200;
    // insert_node(&head, prev_node, node2);
    // prev_node = node2;

    // display_head(&head);

    // remove_head(&head);
    // display_head(&head);
    
    // remove_head(&head);
    // display_head(&head);

    // 일반 노드 삭제 예시
    node1->data = 100;
    node1->link = NULL;
    node2->data = 200;
    node2->link = NULL;

    insert_node(&head, prev_node, node1);
    prev_node = node1;
    insert_node(&head, prev_node, node2);
    prev_node = node2;
    display_list(head);

    remove_node(&head, node1, node2);
    display_list(head);

    remove_node(&head, NULL, node1);
    display_list(head);
    
    return 0;
}

void insert_node(ListNode **phead, ListNode *prev_node, ListNode *new_node) {

    printf("before: new_node = %p\n", new_node);
    printf("before: *phead = %p\n", *phead);

    if (prev_node == NULL) {
        new_node->link = NULL;
        *phead = new_node;
    } else {
        new_node->link = NULL;
        prev_node->link = new_node;
    }

    printf("after: new_node = %p\n", new_node);
    printf("after: *phead = %p\n", *phead);
}

void remove_head(ListNode **phead) {
    if (*phead != NULL) {
        ListNode *tempHead;
        tempHead = *phead;
        *phead = (*phead)->link;
        free(tempHead);
    }
}

void display_head(ListNode **phead) {
    printf("head_node (%d)\n", (*phead)->data);
}

void remove_node(ListNode **phead, ListNode *prev, ListNode *remove) {
    if (prev == NULL) {
        *phead = (*phead)->link;
    } else {
        prev->link = remove->link;
    }

    free(remove);
}

void display_list(ListNode *head) {
    ListNode *p = head;
    printf("( ");
    while(p!=NULL) {
        printf("%d", p->data);
        p = p->link;
        if (p!=NULL) {
            printf(", ");
        }
    }
    printf(" )\n");
}