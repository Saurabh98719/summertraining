#include <iostream>
using namespace std;

int main() {
    int a[] = {11, 12, 13, 14, 15, 16, 17};
    int n = sizeof(a) / sizeof(a[0]);
    int count = 0, sum = 0;

    for(int i = 0; i < n; i++) {
        if(a[i] % 2 == 0) { 
            sum = sum + a[i];
            count++;
        }
    }

    if(count > 0) { // avoid divide by 0
        int avg = sum / count;
        cout << "Average is " << avg << endl;
    } else {
        cout << "No even numbers found" << endl;
    }

    return 0;
}