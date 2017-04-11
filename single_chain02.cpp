#include<iostream>
using namespace std;

class Node{
    friend class Chain;
    public:
    int data;
    Node* next;
};

// 使用尾指针表示单链循环表，序号1表示开头，0表示结尾
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
    Node *rear; //save the last element and pointer the head
};

Chain::Chain(){
    len = 0;
    head = new Node;
    head->next = head;
    rear= head; // rear pointer the last node
}

Node* Chain::find( int elem){
    //if find the element return the node arear
    Node* p=rear;
    for(int i=0; i<len; i++){
        if(elem==p->next->data) return p;
        p = p->next;
    }
    return 0;
}

Node* Chain::locate(int pos){
// return the pos before input
    if(pos>len) return 0;
    Node *p=rear;
    for(int i=0; i<pos; i++) p=p->next;
    return p;
}

bool Chain::insert( int elem, int pos){
    Node* p=locate(pos);
    if(0==p) return false;
    Node* tmp = new Node;
    tmp->data = elem;
    tmp->next = p->next;
    p->next = tmp;
    if(tmp->next == head){
        rear = tmp;
    }
        
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
    Node* p=rear->next;
    p = p->next;
    for(int i=0; i<len; i++){
        cout<< p->data << ' ';
        p=p->next;
    }
    cout << endl;
}

int main(){
    Chain stack;
    cout << "---- single chain test: with rear point ----\n";
    for(int i=0; i<6; i++) 
        stack.insert(i);
    cout << "insert 0~5 into the stack: ";
    cout << "the last element is: "<< stack.rear->data <<endl;
    stack.disp_all();
    cout << "insert 2 at the pos 1: ";
    stack.insert(2, 0);
    cout << "the last element is: "<< stack.rear->data <<endl;
    stack.disp_all();
    cout  << "remove 3 from the stack: ";
    stack.remove(3);
    cout << "the last element is: "<< stack.rear->data <<endl;
    stack.disp_all();
    return 0;
}






