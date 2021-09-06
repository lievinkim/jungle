// 연결리스트 함수
// 연결리스트를 이용하여 많은 기능을 사용할 수 있음
// 첫 노드 삭제, 마지막 노드 삭제
// 연결리스트 내 항목값을 모두 더하기
// 항목값 중 최대값, 최소값 등

#include <stdio.h>
#include <stdlib.h>

typedef int item;
typedef struct ListNode {
    item data;
    struct ListNode *link;
} ListNode;

void display_list(ListNode *head);
int get_length(ListNode *head);
int sum(ListNode *head);
int get_max(ListNode *head);
int get_min(ListNode *head);

void delete_max(ListNode **phead);
void delete_min(ListNode **phead);

ListNode *create_node(item data, ListNode *link);
void insert_node(ListNode **phead, ListNode *prev_node, ListNode *new_node);
void remove_node(ListNode **phead, ListNode *prev, ListNode *removed);
ListNode *concat(ListNode *head1, ListNode *head2);

int main(void) {

    ListNode *list1 = NULL, *list2 = NULL;
    ListNode *p;

    insert_node(&list1, NULL, create_node(90, NULL));
    insert_node(&list1, NULL, create_node(80, NULL));
    insert_node(&list1, NULL, create_node(70, NULL));
    insert_node(&list1, NULL, create_node(60, NULL));
    insert_node(&list1, NULL, create_node(50, NULL));
    insert_node(&list1, NULL, create_node(40, NULL));

    printf("연결리스트 출력\n");
    printf("list1 = ");
    display_list(list1);

    // 연결 리스트의 길이
    printf("\n연결리스트의 길이를 알아봅시다.\n");
    int n = get_length(list1);
    printf("list1의 노드는 %d개 입니다.\n", n);

    // 연결 리스트의 항목값의 총합
    printf("\n연결리스트의 항목값의 총합을 알아봅시다.\n");
    int m = sum(list1);
    printf("list1의 노드 총합은 %d입니다.\n", m);

    // 연결 리스트의 최대값
    printf("\n연결리스트의 최대값을 알아봅시다.\n");
    int h = get_max(list1);
    printf("list1의 노드 최대값은 %d입니다.\n", h);

    // 연결 리스트의 최대값 노드 삭제
    printf("\n연결리스트의 최대값 %d를 삭제한 후를 알아봅시다.\n", h);
    delete_max(&list1);
    display_list(list1);

    // 연결 리스트의 최소값
    printf("\n연결리스트의 최소값을 알아봅시다.\n");
    int l = get_min(list1);
    printf("list1의 노드 최소값은 %d입니다.\n", l);

    // 연결 리스트의 최소값 노드 삭제
    printf("\n연결리스트의 최소값 %d를 삭제한 후를 알아봅시다.\n", l);
    delete_min(&list1);
    display_list(list1);

    insert_node(&list2, NULL, create_node(9000, NULL));
    insert_node(&list2, NULL, create_node(9100, NULL));

    printf("\n연결리스트 출력\n");
    printf("list1 = ");
    display_list(list1);
    printf("list2 = ");
    display_list(list2);

    // 연결 리스트 합병
    list1 = concat(list1, list2);
    printf("합병 후의 list1 = ");
    display_list(list1);

    return 0;
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

int get_length(ListNode *head) {

    int length = 0;

    ListNode *current = head;
    while (current != NULL) {
        current = current->link;
        length++;
    }

    return length;
}

int sum(ListNode *head) {
    int sum = 0;

    ListNode *current = head;
    while (current != NULL) {
        sum += current->data;
        current = current->link;
    }

    return sum;
}

int get_max(ListNode *head) {
    ListNode *current = head;
    int max;

    if (current == NULL) {
        return 0;
    } else {
        max = current->data;
        current = current->link;
    }

    while (current != NULL) {
        if (current->data > max) {
            max = current->data;
        }
        current = current->link;
    }

    return max;
}

int get_min(ListNode *head) {

    ListNode *current = head;
    int min;

    if (current == NULL) {
        return 0;
    } else {
        min = current->data;
        current = current->link;
    }

    while (current != NULL) {
        if (current->data < min) {
            min = current->data;
        }
        current = current->link;
    }

    return min;
}

void delete_max(ListNode **phead) {
    int max = 0;
    ListNode *current = *phead;
    ListNode *prev = NULL, *next = NULL;

    if (current == NULL) {
        return;
    } else if (current->link == NULL) {
        *phead = NULL;
        free(current);
    }

    max = get_max(*phead);
    
    while ( current->link != NULL) {
        prev = current;
        next = current->link;
        
        if( current->data == max ) { // current 노드가 max 값을 가질때
            remove_node(phead, NULL, current);
            current = next;
        }
        else if( next->data == max) { // next 노드가 max 값을 가질때
            remove_node(phead, current, next);
            current = prev;
        }
        else
            current = current->link;
    }

}

void delete_min(ListNode **phead)
{
    int min = 0;
    ListNode *current = (*phead);
    ListNode *prev = NULL, *next = NULL;
    
    if( current == NULL)  // NULL리스트이면 return;
        return;
    else if ( current->link == NULL ) // 단일노드 리스트이면
    {
        *phead = NULL; // head를 NULL로 하고
        free(current);  // current를 제거함
    }
    
    min = get_min(*phead);
    
    while ( current->link != NULL) {
        prev = current;
        next = current->link;
        
        if( current->data == min ) { // current 노드가 max 값을 가질때
            remove_node(phead, NULL, current);
            current = next;
        }
        else if( next->data == min) { // next 노드가 max 값을 가질때
            remove_node(phead, current, next);
            current = prev;
        }
        else
            current = current->link;
    }
}

ListNode *create_node(item data, ListNode *link) {
    ListNode *new_node;
    new_node = (ListNode *)malloc(sizeof(ListNode));
    if (new_node == NULL) {
        fprintf(stderr, "메모리 할당 에러\n");
        exit(1);
    }
    new_node->data = data;
    new_node->link = link;

    return (new_node);
}

void insert_node(ListNode **phead, ListNode *prev_node, ListNode *new_node) {
    if (prev_node == NULL) {
        new_node->link = *phead;
        *phead = new_node;
    } else {
        new_node->link = prev_node->link;
        prev_node->link = new_node;
    }
}

void remove_node(ListNode **phead, ListNode *prev, ListNode *removed)
{
    if (prev == NULL)
        *phead = (*phead)->link;
    else
        prev->link = removed->link;
    free(removed);
}

ListNode *concat(ListNode *head1, ListNode *head2) {
    ListNode *p;
    if (head1 == NULL) {
        return head2;
    } else if (head2 == NULL) {
        return head1;
    } else {
        p = head1;
        while (p->link != NULL) {
            p = p->link;
        }
        p->link = head2;

        return head1;
    }
}