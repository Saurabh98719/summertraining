#include<iostream>
using namespace std;
int main(){
    int a = 10;
    int b = 20;
    int c = a++ + ++b;
    int d = ++a + b++;

    cout<<a<<' ';
    cout<<b<<' ';
    cout<<c<<" ";
    cout<<d<<endl;
}
