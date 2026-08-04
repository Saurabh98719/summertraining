#include <iostream>
using namespace std;

class Queue {
private:
    int arr[100];
    int front, rear, size;

public:
    Queue() {
        front = -1;
        rear = -1;
        size = 100;
    }

    void enqueue(int val) {
        if(rear == size - 1) {
            cout << "Queue Overflow\n";
            return;
        }
        if(front == -1) front = 0; 
        rear++;
        arr[rear] = val;
    }

    void dequeue() {
        if(front == -1 || front > rear) {
            cout << "Queue Underflow\n";
            return;
        }
        cout << "Deleted: " << arr[front] << endl;
        front++;
    }

    void peek() {
        if(front == -1 || front > rear) {
            cout << "Queue is Empty\n";
            return;
        }
        cout << "Front: " << arr[front] << endl;
    }

    
    void display() {
        if(front == -1 || front > rear) {
            cout << "Queue is Empty\n";
            return;
        }
        cout << "Queue: ";
        for(int i = front; i <= rear; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    Queue q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.display();
    q.peek(); 
    q.dequeue(); 
    q.display(); 
}