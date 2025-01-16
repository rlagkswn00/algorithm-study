#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n;
vector<vector<int>> forest;
vector<vector<int>> maxDists;

const int dx[] = { 0, 0, 1, -1 };
const int dy[] = { 1, -1, 0, 0 };

void printMaxDists() {
    cout << "--------------------" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << maxDists[i][j] << ' ';
        }
        cout << endl;
    }
}

void calculateMax(int x, int y) {
    maxDists[x][y] = 1;

    //cout << x << ", " << y << "called" << endl;
    //printMaxDists();

    for (int k = 0; k < 4; k++) {
        int newX = x + dx[k];
        int newY = y + dy[k];
        if (newX < 0 || newY < 0 || newX >= n || newY >= n) continue;
        if (forest[newX][newY] <= forest[x][y]) continue;
        if (maxDists[newX][newY] == 0) {
            calculateMax(newX, newY);
        }
        if (maxDists[x][y] < maxDists[newX][newY] + 1) {
            maxDists[x][y] = maxDists[newX][newY] + 1;
        }
    }
    //cout << x << ", " << y << "return" << endl;
    //printMaxDists();
}


int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    forest = vector<vector<int>> (n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> forest[i][j];
        }
    }

    maxDists = vector<vector<int>> (n, vector<int>(n, 0));
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (maxDists[i][j] == 0) calculateMax(i, j);
            if (ans < maxDists[i][j]) ans = maxDists[i][j];
        }
    }

    cout << ans;
}