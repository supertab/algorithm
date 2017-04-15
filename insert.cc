#include<iostream>
using namespace std;

void disp(int *d, int len){
    for(int i=0; i<len; i++) cout<<d[i]<<' ';
    cout << endl;
}

int main(){
    int d[11]={3,4,2,1,3,1,23,12,51,12,31};
    int i=0, j=0, tmp=0;
    disp(d, 11);
    for(i=1; i<11; i++){
        tmp = d[i];
        for(j=i-1; j>=0&&d[j]>tmp; j--) 
            d[j+1]=d[j];
        d[j+1]=tmp;
    }
    disp(d, 11);

    return 0;
}

