#include <iostream>
#include <string>
#include <cctype> // for tolower
using namespace std;

bool isPalindrome(string s) {
    int i = 0, j = s.length() - 1;

    while(i < j) {
        // convert to lowercase for fair check: Madam = madam
        if(tolower(s[i])!= tolower(s[j])) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int main() {
    string name;
    cout << "Enter your name: ";
    getline(cin, name); // use getline so "Anna Lee" also works

    if(isPalindrome(name)) {
        cout << name << " is a Palindrome " << endl;
    } else {
        cout << name << " is NOT a Palindrome " << endl;
    }

    return 0;
}