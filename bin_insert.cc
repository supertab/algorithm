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
