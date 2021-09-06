// 이진 탐색 트리 (Binary Search Tree)

// 이진 트리

// 기본 조건
// 1) 루트 노드를 중심으로 자식 노드는 왼쪽과 오른쪽에 하나씩 올 수 있다.
// 2) 왼쪽 자식 노드의 값은 부모 노드보다 더 작은 값을 갖는다.
// 3) 오른쪽 자식 노드의 값은 부모 노드보다 더 큰 값을 갖는다.
// 4) 동일한 값을 갖는 노드는 존재하지 않는다.

// 탐색
// 탐색하고자 하는 값이 루트 노드 보다 작을 경우 왼쪽 자식을 방문한다.
// 탐색하고자 하는 값이 루트 노드 보다 클 경우 오른쪽 자식을 방문한다.
// 탐색하고자 하는 값이 루트 노드와 동일할 경우 탐색을 마친다. (탐색 성공)
// 더 이상 방문할 수 있는 자식이 없을 경우 탐색을 마친다. (탐색 실패)

// 삽입
// 삽입하고자 하는 값이 루트 노드 보다 작을 경우 왼쪽 자식을 방문한다.
// 삽입하고자 하는 값이 루트 노드 보다 클 경우 오른쪽 자식을 방문한다.
// 더 이상 방문할 수 있는 자식(왼쪽 또는 오른쪽)이 없을 경우 해당 위치에 삽입한다.

// 삭제
// 삭제하고자 하는 값을 탐색 후 삭제한다.
// 이 때, 3가지 경우의 수가 발생한다.
    // 1) 자식 노드가 없는 경우 : 부모 노드와 연결을 끊고 해당 노드를 삭제한다.
    // 2) 자식 노드가 하나만 있는 경우 : 부모 노드와 자식 노드를 연결하고 해당 노드를 삭제한다.
    // 3) 자식 노드가 두개 모두 있는 경우 : 오른쪽 자식 노드의 트리에서 가장 작은 값을 탐색하여 해당 노드의 위치에 대입한 후 해당 노드를 삭제한다.

#include <stdio.h>
#include <stdlib.h>

//
// 1. 구조체 선언
//
typedef int item;
typedef struct BinNode {

    item data;
    struct BinNode *parent;
    struct BinNode *left_child;
    struct BinNode *right_child;

} BinNode;

//
// 2. 함수 선언
//
BinNode *create_node(item data);
void insert_node(BinNode **root_ptr, BinNode *new_node);
void display_bst(BinNode *root);


//
// 3. 메인 함수
//
int main(void) {
    BinNode *root = NULL;

    insert_node(&root, create_node(50));
    insert_node(&root, create_node(60));
    display_bst(root);

    return 0;
}

//
// 4. 함수 생성
//

// 4-1. 노드 생성 함수
BinNode *create_node(item data) {
    BinNode *new_node;
    new_node = (BinNode *)malloc(sizeof(BinNode));

    if (new_node == NULL) {
        fprintf(stderr, "메모리 할당 에러가 발생했습니다.\n");
        exit(1);
    }

    new_node->data = data;
    new_node->parent = NULL;
    new_node->left_child = NULL;
    new_node->right_child = NULL;

    return (new_node);
}

// 4-2. 노드 삽입 함수
void insert_node(BinNode **root_ptr, BinNode *new_node) {

    BinNode *current_root = *root_ptr;

    if (current_root == NULL) {
        *root_ptr = new_node;
    }

    if (new_node->data == current_root->data) {
        printf("동일한 값을 갖는 노드가 이미 존재합니다.\n");
        free(new_node);
        return;
    } else if (new_node->data < current_root->data) {
        insert_node(&(current_root->left_child), new_node);
    } else if (new_node->data > current_root->data) {
        insert_node(&(current_root->right_child), new_node);
    }
}

// 4-3. 이진탐색트리 표시 함수
void display_bst(BinNode *root) {
    BinNode *p = root;

    if (p == NULL) {
        printf("표시할 노드가 없습니다.\n");
        return;
    }

    printf("NODE[%d] > ", p->data);
    if (p->left_child != NULL) {
        printf("[LEFT-%d]",p->left_child->data);
    } else if (p->right_child != NULL) {
        printf("[RIGHT-%d]", p->right_child->data);
    }
    printf("\n");

    if (p->left_child != NULL) {
        display_bst(p->left_child);
    } else if (p->right_child != NULL) {
        display_bst(p->right_child);
    }
}