// //create these function
// insert
// remove 
// display 
// isfull
// isempty
// number of ele,ent present in the stack
// contain element is present or not!
// need element present at  
#include <iostream>
using namespace std;

class Stack {
private:
    int* arr;
    int size;
    int top;

public:
    Stack(int s) {
        size = s;
        arr = new int[size];
        top = -1;
    }

    ~Stack() {
        delete[] arr;
    }

    void insert(int value) {
        if (isFull()) {
            cout << "Stack is full" << endl;
            return;
        }
        arr[++top] = value;
    }

    void remove() {
        if (isEmpty()) {
            cout << "Stack is empty" << endl;
            return;
        }
        top--;
    }

    void display() {
        if (isEmpty()) {
            cout << "Stack is empty" << endl;
            return;
        }

        cout << "Stack elements: ";
        for (int i = top; i >= 0; i--) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    bool isFull() {
        return top == size - 1;
    }

    bool isEmpty() {
        return top == -1;
    }

    int numberOfElements() {
        return top + 1;
    }

    bool contains(int value) {
        for (int i = top; i >= 0; i--) {
            if (arr[i] == value) {
                return true;
            }
        }
        return false;
    }

    int findPosition(int value) {
        for (int i = top; i >= 0; i--) {
            if (arr[i] == value) {
                return i;   // position from bottom
            }
        }
        return -1;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty" << endl;
            return -1;
        }
        return arr[top];
    }
};

int main() {
    Stack s(5);

    s.insert(10);
    s.insert(20);
    s.insert(30);

    s.display();

    cout << "Top element: " << s.peek() << endl;
    cout << "Number of elements: " << s.numberOfElements() << endl;
    cout << "Contains 20? " << s.contains(20) << endl;
    cout << "Position of 20: " << s.findPosition(20) << endl;

    s.remove();
    s.display();

    return 0;
}