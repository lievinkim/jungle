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

// //
// // 1. 구조체 및 함수 선언
// //
typedef struct bstree_node {
    int key;
    struct bstree_node *left;
    struct bstree_node *right;    
} bstree_node;

bstree_node *search(bstree_node *root, int x);
bstree_node *find_min(bstree_node *root);
bstree_node *find_max(bstree_node *root);
bstree_node *root_node();
bstree_node *new_node(int x);
void *insert(bstree_node **root_ptr, int x);
void *delete(bstree_node **root_ptr, int x);
void inorder(bstree_node *root);

// //
// // 2. 메인 함수
// //
int main() {

    bstree_node *root;
    root = root_node();
    insert(&root,5);
    insert(&root,1);
    insert(&root,15);
    insert(&root,9);
    insert(&root,7);
    insert(&root,12);
    insert(&root,30);
    insert(&root,25);
    insert(&root,40);
    insert(&root,45);
    insert(&root,42);

    inorder(root);
    printf("\n");

    delete(&root, 1);
    inorder(root);
    printf("\n");

    delete(&root, 40);
    inorder(root);
    printf("\n");

    delete(&root, 45);
    inorder(root);
    printf("\n");

    delete(&root, 9);
    inorder(root);
    printf("\n");

    delete(&root, 5);
    inorder(root);
    printf("\n");

    return 0;
}

// //
// // 3. 함수 생성
// //

bstree_node *search(bstree_node *root, int x) {

    if(root == NULL) {
        printf("탐색할 노드가 없습니다.\n");
        return NULL;
    } else if (x == root->key) {
        return root;
    } else if (x < root->key) {
        return search(root->left, x);
    } else {
        return search(root->right, x);
    }

}

bstree_node *find_min(bstree_node *root) {
    
    if (root == NULL) {
        printf("노드가 없습니다.\n");
        return NULL;
    } else if (root->left != NULL) {
        return find_min(root->left);
    }

    return root;
    
}

bstree_node *find_max(bstree_node *root) {

    if (root == NULL) {
        printf("노드가 없습니다.\n");
    } else if (root->right != NULL) {
        return find_max(root->right);
    }

    return root;

}

bstree_node *root_node() {
    bstree_node *root_node;
    root_node = (bstree_node *)malloc(sizeof(bstree_node));
    root_node = NULL;

    return root_node;
}

bstree_node *new_node(int x) {

    bstree_node *new_node;
    new_node = (bstree_node *)malloc(sizeof(bstree_node));
    new_node->key = x;
    new_node->left = NULL;
    new_node->right = NULL;

    return new_node;

}

void *insert(bstree_node **root_ptr, int x) {

    bstree_node *current_root = *root_ptr;

    if (current_root == NULL) {
        *root_ptr = new_node(x);
    } else if (x == current_root->key) {
        printf("동일한 값을 갖는 노드가 이미 존재합니다.\n");
    } else if (x < current_root->key) {
        insert(&(current_root->left), x);
    } else {
        insert(&(current_root->right), x);
    }

}

void *delete(bstree_node **root_ptr, int x) {

    bstree_node *current_root = *root_ptr;

    if (current_root == NULL) {
        printf("삭제 할 노드가 없습니다.\n");
    }

    if (x < current_root->key) {
        delete(&(current_root->left), x);
    } else if (x > current_root->key) {
        delete(&(current_root->right), x);
    } else {

        if (current_root->left==NULL && current_root->right==NULL) {
            *root_ptr = NULL;
            free(current_root);
        }

        else if (current_root->left==NULL || current_root->right==NULL) {
            bstree_node *temp;
            
            if (current_root->left==NULL) {
                temp = current_root->right;
            } else {
                temp = current_root->left;
            }

            *root_ptr = temp;
        }

        else {
            bstree_node *temp;

            temp = find_min(current_root->right);
            (*root_ptr)->key = temp->key;
            delete(&(current_root->right), temp->key);

        }

    }


}

void inorder(bstree_node *root) {
    if(root!=NULL) {
        inorder(root->left);
        printf(" %d ", root->key); 
        inorder(root->right);
    }
}