#include<iostream>
using namespace std;

class Node{
    friend class Chain;
    int data;
    Node* next;
};

class Chain{
public:
    Chain();
    Node* locate(int pos); //找到pos的前一个位置
    Node* find(int elem); //在链中找 elem
    void disp_all();
    bool insert( int elem, int pos=0);
    bool remove(int elem);
    int len;
    Node *head;
};

Chain::Chain(){
    len = 0;
    head = new Node;
    head->next = 0;
}

Node* Chain::locate(int pos){
// return the pos before input
    if(pos>len) return 0;
    Node *p=head;
    for(int i=0; i<pos; i++) p=p->next;
    return p;
}

Node* Chain::find( int elem){
    //if find the element return the node ahead
    Node* p=head;
    for(int i=0; i<len; i++){
        if(elem==p->next->data) return p;
        p = p->next;
    }
    return 0;
}

bool Chain::insert( int elem, int pos){
    Node* p=locate(pos);
    if(0==p) return false;
    Node* tmp = new Node;
    tmp->data = elem;
    tmp->next = p->next;
    p->next = tmp;
    len++;
    return true;
}

bool Chain::remove( int elem){
    Node* p= find(elem);
    if(p==0) return false;
    Node* tmp = p->next;
    p->next = tmp->next;
    delete tmp;
    len--;
    return true; 
}

void Chain::disp_all(){
    Node* p=head->next;
    for(int i=0; i<len; i++){
        cout<< p->data << ' ';
        p=p->next;
    }
    cout << endl;
}

int main(){
    Chain stack;
    cout << "---- single chain test: with head point ----\n";
    for(int i=0; i<6; i++) stack.insert(i);
    cout << "insert 0~5 into the stack: ";
    stack.disp_all();
    cout << "insert 2 at the pos 1: ";
    stack.insert(2, 1);
    stack.disp_all();
    cout  << "remove 3 from the stack: ";
    stack.remove(3);
    stack.disp_all();
    return 0;
}

/*
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
 *
*/






