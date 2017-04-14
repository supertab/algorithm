#include<iostream>
using namespace std;

int bin_search(int *data, int low, int high, int elem){
    int mid=0;
    while(low< high){
        cout << "low: "<<low <<' '<<"high: "<<high<<' ';
        mid = low + (high - low)/2;
        cout << "mid: "<<mid<<endl;
        if(data[mid] < elem) low = mid+1;
        else if(data[mid] > elem) high = mid-1;
        else return mid;
    }
    cout << "low: "<<low <<' '<<"high: "<<high<<endl;
    return high;
}

int main(){
    int d[11]={1, 1, 1, 4, 5, 7, 9, 12, 31, 33, 55};
    int low =0, high=10;
    int elem = 1;
    int mid = bin_search(d, low, high, elem);
    cout <<"mid: "<< mid <<' '<<"d[mid]: "<<d[mid]<<' '
         <<"elem: "<<elem<<endl;
    return 0;
}
