// given array:
// int arr[] = {1,2,3,4,5,6,7,8};
// find the index of 6.
// --by linear Search
// --by Binary Search

// Find the average of all element present in the array.
// int a[] = {1,2,3,4,5};

// find the maximum sum of subarray:
// (sliding window)
// int arr[] = {5,2,1,4,9,2,3,7,8};
// int subarray_length = 3;

// find the largest element from the above array.

#include <iostream>
using namespace std;

int binarySearchRec(int arr[], int low, int high, int key) {
    if(low > high) return -1;

    int mid = low + (high - low) / 2;

    if(arr[mid] == key) return mid;
    else if(arr[mid] < key)
        return binarySearchRec(arr, mid + 1, high, key);
    else
        return binarySearchRec(arr, low, mid - 1, key);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 6;

    int index = binarySearchRec(arr, 0, n - 1, key);
    cout << "Index: " << index << endl; // 5
    return 0;
}