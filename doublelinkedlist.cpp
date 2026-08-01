
    #include <iostream>
using namespace std;


struct Node {
    int data;
    Node* prev;
    Node* next;
};

Node* head = NULL;

void insert(int val) {
    Node* newNode = new Node();
    newNode->data = val;
    newNode->next = NULL;
    
    if(head == NULL) {
        newNode->prev = NULL;
        head = newNode;
        return;
    }
    
    Node* temp = head;
    while(temp->next!= NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
    newNode->prev = temp;
}


void displayForward() {
    Node* temp = head;
    cout << "Forward: ";
    while(temp!= NULL) {
        cout << temp->data << " <-> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

void displayBackward() {
    if(head == NULL) return;
    
    Node* temp = head;
    // go to last node
    while(temp->next!= NULL) {
        temp = temp->next;
    }
    
    cout << "Backward: ";
    while(temp!= NULL) {
        cout << temp->data << " <-> ";
        temp = temp->prev;
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
    if(head!= NULL) {
        head->prev = NULL;
    }
    delete temp;
}

int main() {
    insert(10);
    insert(20);
    insert(30);

    displayForward();  
    displayBackward(); 

    deleteBegin();
    cout << "After deleting first node:" << endl;
    displayForward();  

    return 0;
}
