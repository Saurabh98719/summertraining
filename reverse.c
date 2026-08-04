#include <stdio.h>
int main(){
    int a[] = {11,12,13,6};
    int n = sizeof(a)/sizeof(a[0]);
    int count = 0, sum = 0;
    for(int i = 0; i < n; i++){
        if(a[i] % 2 == 0) {
            sum = sum + a[i];
            count++;
        }
    }
    if(count > 0) {
        int avg = sum / count;
        printf("average is %d\n", avg);
    } else {
        printf("no even numbers\n");
    }
    return 0;
}