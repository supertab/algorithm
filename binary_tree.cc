#include<iostream>
using namespace std;

class BinTree;
class Node{
friend class BinTree;
public:
    Node():lchild(0), rchild(0){};
    Node(int val):data(val), lchild(0), rchild(0){};
    int data;
    Node *lchild, *rchild;
};

class BinTree{
public:
    BinTree():root(0){};
    void insert(int x){ insert(root, x);}
    void pre_order(){ pre_order(root);}
    void mid_order(){ mid_order(root);}
    void post_order(){ post_order(root);}
private:
    Node *root;
    void insert(Node *&nd, int x);
    void pre_order(Node *nd);
    void mid_order(Node *nd);
    void post_order(Node *nd);
};

void BinTree::insert(Node *&nd, int x){
    if(nd==0) 
        nd = new Node(x);
    else if(nd->data>x)
        insert(nd->lchild, x);
    else 
        insert(nd->rchild, x);
}

void BinTree::pre_order(Node *nd){
    if(nd!=0){
        cout<<nd->data<<' ';
        pre_order(nd->lchild);
        pre_order(nd->rchild);
    }
}

void BinTree::mid_order(Node *nd){
    if(nd!=0){
        mid_order(nd->lchild);
        cout<<nd->data<<' ';
        mid_order(nd->rchild);
    }
}


void BinTree::post_order(Node *nd){
    if(nd!=0){
        post_order(nd->lchild);
        post_order(nd->rchild);
        cout<<nd->data<<' ';
    }
}

int main(){
    int d[]={7, 3, 2, 4, 5, 6};
    BinTree btree;
    for(int i=0; i<6; i++)
        btree.insert(d[i]);
    cout<<"pre_order: "<<endl;
    btree.pre_order();
    cout<<"\nmid_order: "<<endl;
    btree.mid_order();
    cout<<"\npost_order: "<<endl;
    btree.post_order();
    cout << endl;
    return 0;
}

