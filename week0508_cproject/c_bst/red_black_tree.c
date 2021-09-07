// 레드-블랙 트리
// 이진탐색트리의 일종
// SEARCH, INSERT, DELETE 연산은 최악의 경우에도 O(logn) 복잡도를 갖는다.

// 노드 : key, left, right, parent
// 자식 노드가 존재하지 않을 경우 NIL 노드라고 부르는 특수한 노드가 있다고 가정한다.
// 모든 리프 노드 : NIL
// 루트 부모 노드 : NIL
// 내부 노드와 NIL 노드로 구성된다.

// 조건
// 1) 각 노드는 레드와 블랙이다.
// 2) 루트 노드는 블랙이다.
// 3) 모든 리프 노드는 블랙이다.
// 4) 레드 노드의 자식들은 모두 블랙이다. (레드 노드는 연속적으로 등장하지 않는다.)
// 5) 모든 노드에 대해서 그 노드로부터 자손인 리프노드에 이르는 모든 경로에는 동일한 개수의 블랙 노드가 존재한다.

// 레드-블랙 트리의 높이 (복잡도 계산)
// 노드 x의 높이 h(x)는 자신으로부터 리프 노드까지의 가장 긴 경로에 포함된 edge의 개수
// 노드 x의 블랙-높이 bh(x)는 x로부터 리프 노드까지의 경로상의 블랙 노드의 개수
// bh(x)>=h/2의 관계가 성립된다.
// 노드 x를 루트로 하는 임의의 부트리는 적어도 2**bh(x)-1개의 내부 노드를 포함한다.
// n개의 내부 노드를 가지는 레드블랙 트리의 높이는 2log(n+1) 이하이다.

// 기본 연산
// Left-Rotation, Right-Rotation
// Node[x] = Left[a], Right[y] / Node[y] = Left[b], Right[r]
// -> Left Rotate
// Node[y] = Left[x], Right[r] / Node[x] = Left[a], Right[b]
// -> Right Rotate
// Node[x] = Left[a], Right[y] / Node[y] = Left[b], Right[r] 

// 삽입
// 이진탐색트리와 동일하게 노드를 삽입한다.
// 1) 새롭게 삽입된 노드는 레드 노드로 설정한다.
// 2) RB-INSERT-FIXUP을 호출한다.

    // RB-INSERT-FIXUP 호출이란
    // Red-Red Violation 문제가 발생한 경우를 해결하기 위함
    // 위반될 가능성이 있는 조건들을 체크함
        // 조건
        // 1) 각 노드는 레드와 블랙이다. (OK)
        // 2) 루트 노드는 블랙이다. (만약 삽입 위치가 루트였다면 위반)
        // 3) 모든 리프 노드는 블랙이다. (OK)
        // 4) 레드 노드의 자식들은 모두 블랙이다. (만약 삽입 위치의 부모 노드가 레드라면 위반)
        // 5) 모든 노드에 대해서 그 노드로부터 자손인 리프노드에 이르는 모든 경로에는 동일한 개수의 블랙 노드가 존재한다. (OK)
        // 2번과 4번의 조건에서 문제가 발생할 수 있다.
        // 2번은 노드의 색상만 바꾸면 되기 때문에 큰 문제가 되지 않는다.
        // 4번은 Red-Red Violation으로 복잡한 연산이 수반 된다.
    // Loop Invariant
        // 삽입 노드는 레드 노드
        // 오직 하나의 위반만이 존재 (조건2, 조건4)
    // Loop 종료 조건
        // 부모 노드가 블랙 노드인 경우 종료
        // 조건 2가 위반인 경우 색상을 블랙으로 바꾸고 종료
    // 경우의 수는 총 6가지
        // 1, 2, 3의 경우의 수 : 부모 노드가 할아버지 노드의 왼쪽 자식인 경우
        // 4, 5, 6의 경우의 수 : 부모 노드가 할아버지 노드의 오른쪽 자식인 경우
        // 1, 2, 3과 4, 5, 6은 서로 대칭적
    // 경우의 수 1번
        // 삼촌 노드도 레드인 경우 (삽입 노드, 부모 노드 , 삼촌 노드 모두 레드)
        // 부모 노드와 삼촌 노드를 블랙으로 변경하고 할아버지 노드는 레드로 변경
        // 레드로 변경된 할아버지 노드를 새로운 focus 노드로 설정
        // Binary Search Tree의 조건은 변경되지 않으나 Red-Black의 조건만 체크하면 됨
            // 조건 2와 4 이외의 조건들은 여전히 OK
            // 단 할아버지 노드와 할아버지 부모 노드를 체크해야 함 -> 이런 식으로 계속 올라감
    // 경우의 수 2, 3번
        // 삼촌 노드가 블랙인 경우 (삽입 노드, 부모 노드만 레드)
        // 경우의 수 2번
            // 삽입 노드가 부모 노드의 왼쪽 자식인 경우
            // 할아버지 노드를 중심으로 right-rotation 진행
            // 부모 노드는 할아버지 노드 위치로, 할아버지 노드는 삼촌 노드 위치로 변경
            // 부모 노드는 블랙으로, 할아버지 노드는 레드로 색상 변경
        // 경우의 수 3번
            // 삽입 노드가 부모 노드의 오른쪽 자식인 경우
            // 부모 노드에 대하여 left-rotation을 진행
            // 경우의 수 2번 형태로 변경
        // 모든 조건 해결
        

// x에 대한 left-rotation 순서
// 1) x의 오른쪽 노드를 y로 지정한다.
// 2) x의 오른쪽 노드에 y의 왼쪽 노드를 대입한다.
// 3) y의 왼쪽 노드가 NULL이 아닐 때, 부모 노드를 x로 변경한다.

// 4) y의 부모 노드를 x의 부모 노드로 변경한다.
// 4-1) x의 부모 노드가 NULL이라면 y를 루트 노드로 지정한다.
// 4-2) x가 부모 노드의 왼쪽 자식이라면 해당 위치에 y를 대입한다.
// 4-3) x가 부모 노드의 오른쪽 자식이라면 해당 위치에 y를 대입한다.

// 5) y의 왼쪽 자식 노드로 x를 대입한다.
// 6) x의 부모 노드를 y로 변경한다.

#include <stdio.h>
#include <stdlib.h>

// 열거형을 이용하여 노드의 색상을 상수로 선언
enum COLOR {
    Red,
    Black
};

// 노드 구조체 생성 (5개의 멤버)
typedef struct rbtree_node {
    int key;
    struct rbtree_node *parent;
    struct rbtree_node *left_child;
    struct rbtree_node *right_child;
    enum COLOR color;
} RbtreeNode;

// 트리 구조체 생성 (2개의 멤버)
typedef struct rbtree {
    RbtreeNode *root;
    RbtreeNode *NIL;
} Rbtree;

// 노드 생성 함수
RbtreeNode *create_node(int key) {
    RbtreeNode *new_node = (RbtreeNode *)malloc(sizeof(RbtreeNode));

    if (new_node == NULL) {
        fprintf(stderr, "메모리 할당 에러\n");
        exit(1);
    }

    new_node->key = key;
    new_node->parent = NULL;
    new_node->left_child = NULL;
    new_node->right_child = NULL;
    new_node->color = Red;

    return new_node;
}

// 트리 생성 함수
Rbtree *new_Rbtree() {
    Rbtree *t = (Rbtree *)malloc(sizeof(Rbtree));
    RbtreeNode *nil_node = (RbtreeNode *)malloc(sizeof(RbtreeNode));

    nil_node->key = 0;
    nil_node->parent = NULL;
    nil_node->left_child = NULL;
    nil_node->right_child = NULL;
    nil_node->color = Black;

    t->NIL = nil_node;
    t->root = t->NIL;

    return t;
}

// left_rotate 함수
void left_rotate(Rbtree *t, RbtreeNode *x) {

    // 1) x의 오른쪽 노드를 y로 지정한다.
    RbtreeNode *y = x->right_child;

    // 2) x의 오른쪽 노드에 y의 왼쪽 노드를 대입한다.
    x->right_child = y->left_child;

    // 3) y의 왼쪽 노드가 NULL이 아닐 때, 부모 노드를 x로 변경한다.
    if (y->left_child != t->NIL) {
        y->left_child->parent = x;
    }

    // 4) y의 부모 노드를 x의 부모 노드로 변경한다.
    y->parent = x->parent;
    // 4-1) x의 부모 노드가 NULL이라면 y를 루트 노드로 지정한다.
    // 4-2) x가 부모 노드의 왼쪽 자식이라면 해당 위치에 y를 대입한다.
    // 4-3) x가 부모 노드의 오른쪽 자식이라면 해당 위치에 y를 대입한다.
    if (x->parent == t->NIL) {
        t->root = y;
    } else if (x == x->parent->left_child) {
        x->parent->left_child = y;
    } else if (x == x->parent->right_child) {
        x->parent->right_child = y;
    }

    // 5) y의 왼쪽 자식 노드로 x를 대입한다.
    y->left_child = x;
    // 6) x의 부모 노드를 y로 변경한다.
    x->parent = y;
}

// right_rotate 함수
void right_rotate(Rbtree *t, RbtreeNode *x) {

    RbtreeNode *y = x->left_child;

    x->left_child = y->right_child;
    if (y->right_child != t->NIL) {
        y->right_child->parent = x;
    }

    y->parent  = x->parent;
    if (x->parent == t->NIL) {
        t->root = y;
    } else if (x == x->parent->left_child) {
        x->parent->left_child = y;
    } else if (x == x->parent->right_child) {
        x->parent->right_child = y;
    }

    y->right_child = x;
    x->parent = y;
}

void insertion_fixup(Rbtree *t, RbtreeNode *new_node) {
    
    // Red-Red Violation이 발생하는 경우
    while (new_node->parent->color == Red) {
        
        // 1, 2, 3의 경우의 수 : 부모 노드가 할아버지 노드의 왼쪽 자식인 경우
        if (new_node->parent == new_node->parent->parent->left_child) {
            RbtreeNode *uncle_node = new_node->parent->parent->right_child;

            // CASE 01 : 삼촌 노드가 레드인 경우
            if (uncle_node->color == Red) {
                new_node->parent->color = Black;
                new_node->parent->parent->color = Red;
                uncle_node->color = Black;
                new_node = new_node->parent->parent;
            } else {

                // CASE 02 : 삽입 노드가 부모 노드의 오른쪽인 경우
                if (new_node == new_node->parent->right_child) {
                    new_node = new_node->parent;
                    left_rotate(t, new_node);
                }

                // CASE 03 : 삽입 노드가 부모 노드의 왼쪽인 경우
                new_node->parent->color = Black;
                new_node->parent->parent->color = Red;
                right_rotate(t, new_node->parent->parent);
            }        
        }
        // 4, 5, 6의 경우의 수 : 부모 노드가 할아버지 노드의 오른쪽 자식인 경우
        else if (new_node->parent == new_node->parent->parent->right_child) {
            RbtreeNode *uncle_node = new_node->parent->parent->left_child;

            // CASE 01 : 삼촌 노드가 레드인 경우
            if (uncle_node->color == Red) {
                new_node->parent->color = Black;
                new_node->parent->parent->color = Red;
                uncle_node->color = Black;
                new_node = new_node->parent->parent;
            } else {

                // CASE 02 : 삽입 노드가 부모 노드의 오른쪽인 경우
                if (new_node == new_node->parent->left_child) {
                    new_node = new_node->parent;
                    right_rotate(t, new_node);
                }

                // CASE 03 : 삽입 노드가 부모 노드의 왼쪽인 경우
                new_node->parent->color = Black;
                new_node->parent->parent->color = Red;
                left_rotate(t, new_node->parent->parent);
            }        
        }

    }

    t->root->color = Black;
}

// 삽입 함수
void insert(Rbtree *t, RbtreeNode *new_node) {

    RbtreeNode *y = t->NIL;
    RbtreeNode *temp = t->root;

    while(temp != t->NIL) {
        y = temp;
        if (new_node->key < temp->key) {
            temp = temp->left_child;
        } else {
            temp = temp->right_child;
        }
    }

    new_node->parent = y;

    if (y == t->NIL) {
        t->root = new_node;
    } else if (new_node->key < y->key) {
        y->left_child = new_node;
    } else {
        y->right_child = new_node;
    }

    new_node->left_child = t->NIL;
    new_node->right_child = t->NIL;

    insertion_fixup(t, new_node);
}

// 인오더 함수
void inorder(Rbtree *t, RbtreeNode *n) {
    if (n != t->NIL) {
        inorder(t, n->left_child);
        printf("%d\n", n->key);
        inorder(t, n->right_child);
    }
}

// 메인 함수
int main() {

    Rbtree *t = new_Rbtree();
    RbtreeNode *a, *b, *c, *d, *e, *f, *g, *h, *i, *j, *k, *l, *m;

    a = create_node(10);
    b = create_node(20);
    c = create_node(30);
    d = create_node(100);
    k = create_node(150);
    l = create_node(110);
    e = create_node(90);
    f = create_node(40);
    g = create_node(50);
    h = create_node(60);
    i = create_node(70);
    j = create_node(80);
    m = create_node(120);

    insert(t, a);
    insert(t, b);
    insert(t, c);
    insert(t, d);
    insert(t, e);
    insert(t, f);
    insert(t, g);
    insert(t, h);
    insert(t, i);
    insert(t, j);
    insert(t, k);
    insert(t, l);
    insert(t, m);

    inorder(t, t->root);

    return 0;
}