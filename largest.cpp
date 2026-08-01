#include<iostream>
using namespace std;
int main(){
    int arr[] = {2,3,4,67,3};
    int n = sizeof(arr)/4;
    int mx = arr[0];
    for(int i = 1; i < n; i++) {
        if(arr[i] > mx) mx = arr[i];
    }
    cout << mx;
}