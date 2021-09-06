#include<stdio.h>
#include<stdlib.h> //linux에서는 stlib.h


/*구조체 선언*/
typedef struct node {
    int key;
    struct node *left, *right;
}node;
typedef struct bstree {
    struct node *root;
}bstree;
/*--------*/


/*함수의 형*/
struct bstree* new_bstree(void);
struct node* bst_insert(struct bstree* t, const int key);
void delete_bstree(struct bstree* t);
struct node* bst_find(const struct bstree* t, const int key);
struct node* bst_min(const struct bstree* t);
struct node* bst_max(const struct bstree* t);
void inorder(node* x);
int bstree_erase(struct bstree* t, struct node* p);
// int bstree_to_array(const struct bstree *t, int *arr, const size_t n);
/*------------------------------------------------------------------*/


int main(){
/* test insert */
    bstree* tree = new_bstree();
    bst_insert(tree, 8);
    bst_insert(tree, 3);
    bst_insert(tree, 10);
    bst_insert(tree, 1);
    bst_insert(tree, 6);
    bst_insert(tree, 14);
    bst_insert(tree, 13);
    bst_insert(tree, 4);
    bst_insert(tree, 7);
    printf("%d\n", tree->root->key);
    printf("%d\n", tree->root->right->key);
    printf("%d\n", tree->root->right->right->key);
    printf("%d\n", tree->root->left->key);
    printf("%d\n", tree->root->left->left->key);

/* test find */ 
    printf("%p\n", bst_find(tree, 10));
    printf("%p\n", tree->root);
    printf("%p\n", bst_find(tree, 20));
    printf("%p\n", tree->root->right);
    printf("%p\n", bst_find(tree, 30));
    printf("%p\n", tree->root->right->right);
    printf("%p\n", bst_find(tree, 5));
    printf("%p\n", tree->root->left);
    printf("%p\n", bst_find(tree, 3));
    printf("%p\n", tree->root->left->left);

// /* test min max */
    printf("%p\n", bst_min(tree));
    printf("%p\n", bst_max(tree));
    
/* 중위순회 구현 */
    inorder(tree->root);

/* erase 구현 */
    bstree_erase(tree,bst_find(tree,3));
    inorder(tree->root);
    
}


/*---------함수 원형---------*/
bstree* new_bstree(void){
    struct bstree *p = (bstree*)calloc(sizeof(bstree),1);
    return p;
}

node* bst_insert(struct bstree *t, const int key){ 
    node* newnode = (node*)malloc(sizeof(node)); 
    newnode->key = key;   // key값 갖는 node생성
    newnode->left=NULL;
    newnode->right=NULL;

    if (t->root==NULL){
        t->root=newnode;
        return t->root;
    }

    node* x=t->root;  //x는 현재위치 노드 주소 & 루트 부터 탐색시작
    while(1){
        if (x->key > key){
            if(x->left!=NULL){
                x = x->left;}   
            else {x->left=newnode;
            return t->root;}}
        else{
            if(x->right!=NULL){
                x = x->right;}
            else {x->right=newnode;
            return t->root;}
        }
    }}
 
void delete_bstree(struct bstree* t)
{
    free(t);
}

node* bst_find(const struct bstree* t, const int key){
    node* x=t->root;
    while(1){
        if (x->key > key){
            if(x->left!=NULL){
                x = x->left;}
            else{return NULL;}}
        else if (x->key < key){
            if(x->right!=NULL){
                x = x->right;}
            else{return NULL;}}
        /* else는 같을 경우 */
        else {return x;} //해당 노드 node 주소 반납
        }
    return NULL;
}

struct node* bst_min(const struct bstree* t){
    node* x=t->root;
    while(x->left!=NULL){
        x=x->left;
    }
    return x;
}

struct node* bst_max(const struct bstree* t){
    node* x=t->root;
    while(x->right!=NULL){
        x=x->right;
    }
    return x;

}

int bstree_erase(struct bstree* t, struct node* p){
    if (t->root==NULL){return 0;} //트리가 없으면 종료.
    node* x=t->root;
    node* y;  //y는 부모노드 
    while(1){   //부모찾기 반복문
        if (x->key > p->key){
            if(x->left!=NULL){ 
                y=x;
                x = x->left;}
            else{return 0;}}
        else if (x->key < p->key){
            if(x->right!=NULL){
                y=x;
                x = x->right;}
            else{return 0;}}
        /* else는 같을 경우 */
        else {break;}
        }

    if (p->left==NULL){
        node* temp =p->right;
        if (y->key > p->key){
            y->left=temp;
            free(p);
        }
        else if (y->key < p->key){
            y->right=temp;
            free(p);
        }
    }
    else if (p->right==NULL){
        node* temp=p->left;
        if (y->key > p->key){
            y->left=temp;
            free(p);
        }
        else if (y->key < p->key){
            y->right=temp;
            free(p);
        }
    }
    else {
        node* temp= p->right;
        while(temp->left!=NULL){
        temp=temp->left;}
        y->right->key = temp->key;
        bstree_erase(t,temp);
    }
    return 0;
}

void inorder(node* x){
    if(x!=NULL){
    inorder(x->left);
    printf("%d\n", x->key);
    inorder(x->right);
}
}


//나중에 필요하면 구현
// int bstree_to_array(const struct bstree *t, int *arr, const size_t n){
//     node* x=t->root;
//     void inorder(node* x);
//     return 0;
// }
