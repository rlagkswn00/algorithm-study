#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define endl '\n';

int sharkSize = 2;
int haveToEatToGrow = sharkSize;

int N;
vector<vector<int>> fishMap;
vector<vector<int>> distanceMap;
queue<pair<int, int>> Q;
int preyCandidateDistance;
int preyCandidateX;
int preyCandidateY;

void printDistanceMap() {
	cout << endl;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (distanceMap[i][j] != -1) {
				cout << ' ';
			}
			cout << distanceMap[i][j] << ' ';
		}
		cout << endl;
	}
	cout << endl;
}

void placeShark(int x, int y) {
	distanceMap = vector<vector<int>>(N, vector<int>(N, -1));
	distanceMap[x][y] = 0;
	Q = queue<pair<int, int>>();
	Q.push({ x, y });

	preyCandidateDistance = N * N;
	preyCandidateX = N;
	preyCandidateY = N;
}

void grow() {
	sharkSize++;
	haveToEatToGrow = sharkSize;
	//cout << "growed to: " << sharkSize << endl;
}
void eatAt(int x, int y) {
	haveToEatToGrow--;
	fishMap[x][y] = 0; //TS3: fishMap 업데이트 안해줌
	if (haveToEatToGrow == 0) {
		grow();
	}
	//cout << "yum! have to eat " << haveToEatToGrow << "more" << endl;
}

int32_t main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	fishMap = vector<vector<int>>(N, vector<int>(N));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> fishMap[i][j];
			if (fishMap[i][j] == 9) {
				placeShark(i, j);
				fishMap[i][j] = 0; //TS2: 상어 자리는 0
			}
		}
	}
	int survivedTime = 0;
	while (!Q.empty()) {
		int x = Q.front().first;
		int y = Q.front().second;
		Q.pop();
		//printDistanceMap();
		if (distanceMap[x][y] >= preyCandidateDistance) {
			int preyX = preyCandidateX;
			int preyY = preyCandidateY;
			survivedTime += distanceMap[preyX][preyY];
			placeShark(preyX, preyY);
			eatAt(preyX, preyY);
			continue;
		}
		int dx[] = {1, -1, 0, 0};
		int dy[] = { 0, 0, 1, -1 };
		for (int i = 0; i < 4; i++) {
			int nextX = x + dx[i];
			int nextY = y + dy[i];
			if (nextX < 0 || N <= nextX ||
				nextY < 0 || N <= nextY) {
				continue;
			}
			if (distanceMap[nextX][nextY] != -1) {
				continue;
			}
			int fishSize = fishMap[nextX][nextY];
			if (fishSize > sharkSize) {
				continue;
			}
			distanceMap[nextX][nextY] = distanceMap[x][y] + 1;
			Q.push({ nextX, nextY });
			if (fishSize != 0 &&
				fishSize < sharkSize &&
				(nextX < preyCandidateX || //TS1: 괄호 묶어주기
				(nextX == preyCandidateX && nextY < preyCandidateY))) {
				//consider eating
				preyCandidateDistance = distanceMap[nextX][nextY];
				preyCandidateX = nextX;
				preyCandidateY = nextY;
				//cout << "updated candidate to"  << " " << nextX << ", " << nextY << endl;
			}
		}
 	}
	cout << survivedTime;
}
