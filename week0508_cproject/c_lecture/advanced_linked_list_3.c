// 연결 리스트 삽입

#include <stdio.h>
#include <stdlib.h>

typedef char item;
typedef struct ListNode {
    item data;
    struct ListNode *link;
} ListNode;

// 삽입방법 1
// void insert_node(ListNode **phead, ListNode *new_node);
// int main(void) {
//     ListNode *head = NULL;
//     ListNode *node, *current_node;
//     for (int i=0; i<5; i++) {
//         node = (ListNode *)malloc(sizeof(ListNode));
//         node->data = i;
//         insert_node(&head, node);
//     }

//     current_node = head;
//     while (current_node != NULL)
//     {
//         printf("current_node->data = %d\n", current_node->data);
//         current_node = current_node->link;
//     }

//     return 0;
// }
// void insert_node(ListNode **phead, ListNode *new_node) {
//     new_node->link = *phead;
//     *phead = new_node;
// }

void insert_node(ListNode **phead, ListNode *prev_node, ListNode *new_node);
int main(void) {
    ListNode *head = NULL, *prev_node = NULL;
    ListNode *node, *current_node;

    for (int i=0; i<5; i++) {
        node = (ListNode *)malloc(sizeof(ListNode));
        node->data = i;
        insert_node(&head, prev_node, node);
        
        prev_node = node;
    }

    current_node = head;
    while (current_node != NULL)
    {
        printf("current_node->data %d\n", current_node->data);
        current_node = current_node->link;
    }
    
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