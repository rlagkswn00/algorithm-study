#include <bits/stdc++.h>

using namespace std;

int arr[1000007];

int main() {
    int x;
    cin >> x;
 
    arr[0] = 0;
    arr[1] = 0;
    
    for(int i=2; i<=x; i++) {
        arr[i] = arr[i-1] + 1;
        if(i % 2 == 0) {
            arr[i] = min(arr[i-1] + 1, arr[i/2] + 1);
        }
        if(i % 3 == 0) {
            arr[i] = min(arr[i], arr[i/3] + 1);
        }
    
    }
    cout << arr[x];
}