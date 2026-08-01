// dynamic memory allocation.
// memory is created at runtime.
// malloc, calloc , realoc,free
// int a = (int*)malloc(sizeof(int));

#include <iostream>
using namespace std;


struct Node {
    int data;
    Node* next;
};

Node* head = NULL; 

void insert(int val) {
    Node* newNode = new Node();
    newNode->data = val;
    newNode->next = NULL;

    if(head == NULL) {
        head = newNode;
    } else {
        Node* temp = head;
        while(temp->next!= NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void display() {
    Node* temp = head;
    while(temp!= NULL) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

void deleteBegin() {
    if(head == NULL) {
        cout << "List is empty" << endl;
        return;
    }
    Node* temp = head;
    head = head->next;
    delete temp;
}

int main() {
    insert(10);
    insert(20);
    insert(30);

    cout << "List: ";
    display(); 

    deleteBegin();
    cout << "After deleting first node: ";
    display(); 

    return 0;
}