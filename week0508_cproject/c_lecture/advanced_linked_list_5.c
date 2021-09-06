// 삭제함수 구현 2탄
// 특정한 필드값을 가지는 노드를 삭제하는 기능
// 노드를 따라 가다가 특정한 필드값을 발견하면 삭제
// 선행 노드는 유지할 수 있도록 해야 함

#include <stdio.h>
#include <stdlib.h>

typedef int item;
typedef struct ListNode {
    item data;
    struct ListNode *link;
} ListNode;

void insert_node(ListNode **phead, ListNode *prev_node, ListNode *new_node);
void remove_node(ListNode **phead, int value);
void display_list(ListNode *head);

int main(void) {
    ListNode *head = NULL, *prev_node = NULL;
    ListNode *node1, *node2, *node3;

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
    node3->data = 300;
    node3->link = NULL;

    insert_node(&head, prev_node, node1);
    prev_node = node1;
    insert_node(&head, prev_node, node2);
    prev_node = node2;
    insert_node(&head, prev_node, node3);
    prev_node = node3;

    printf("100, 200, 300 데이터를 가진 노드 삽입 후 결과\n");
    display_list(head);

    remove_node(&head, 200);
    printf("200 데이터를 가진 노드 삭제 후\n");
    display_list(head);

    remove_node(&head, 100);
    printf("100 데이터를 가진 노드 삭제 후\n");
    display_list(head);

    remove_node(&head, 300);
    printf("300 데이터를 가진 노드 삭제 후\n");
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

void remove_node(ListNode **phead, int value) {

    ListNode *curr, *prev;
    curr = *phead;
    prev = NULL;

    while (curr != NULL) {
        if (curr->data == value) {
            if (prev == NULL) {
                *phead = curr->link;
            } else {
                prev->link = curr->link;
            }
            free(curr);
            return;
        }
        prev = curr;
        curr = curr->link;
    }

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
