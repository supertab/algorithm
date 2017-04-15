#include<iostream>
using namespace std;

int bin_search(int *data, int low, int high, int elem){
    int mid=0, pos=0;
    while(low< high){
        mid = low + (high - low)/2;
        if(data[mid] < elem) low = mid+1;
        else if(data[mid] > elem) high = mid-1;
        else {
            if(data[mid]>=elem) pos = mid;
            else pos=mid+1;
            return pos;
        }
    }
    int tmp;
    tmp = data[low]>=data[high]? high: low;
    pos = data[tmp]>=elem? tmp: tmp+1;
    return pos;
}

void move_back(int *d, int beg, int end){
    for(int i=end; i>beg; i--)
        d[i]=d[i-1];
}

void disp(int *d, int len){
    for(int i=0; i<len; i++) cout<<d[i]<<' ';
    cout << endl;
}

int main(){
    int d1[11]={1,1,2,3,5,8,11,19,30,49,79};
    int d2[11]={3,4,2,1,3,1,23,12,51,12,31};
    int low=0, high=0;
    int pos=0, tmp=0, j=0;
    cout << "unsort:\n";
    disp(d2, 11);
    // move_back(d2, 1, 5);
    // sort
    for(int i=1; i<11; i++){
        tmp = d2[i];
        pos = bin_search(d2,low,high,tmp);
        // move backward one step
        move_back(d2, pos, i);
        d2[pos]=tmp;
        high++;
    }
    cout<<"sorted:"<<endl;
    disp(d2, 11);
    return 0;
}

