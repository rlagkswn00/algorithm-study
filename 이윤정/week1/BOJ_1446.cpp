#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define endl '\n'
#define MAX 10000

int dist[MAX + 1];
bool confirmed[MAX + 1] = { 0, };
int main(void) {
	int N, D;
	cin >> N >> D;
	int cnt = N;
	vector<vector<pair<int, int>>> roadsFrom(MAX + 1);

	while (cnt--) {
		int start, end, dist;
		cin >> start >> end >> dist;
		roadsFrom[start].push_back({ end, dist });
	}

	for (int i = 0; i <= MAX; i++) {
		dist[i] = MAX;
		if (i == 0) dist[i] = 0;
		if (i != MAX) roadsFrom[i].push_back({ i + 1, 1 });
	}

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
	pq.push({ 0, 0 });
	while (!pq.empty()) {
		int curMinDist = pq.top().first;
		int curMin = pq.top().second;
		pq.pop();
		if (confirmed[curMin]) continue;
		confirmed[curMin] = true;

		for (auto& road : roadsFrom[curMin]) {
			if (confirmed[road.first]) continue;
			if (dist[road.first] < curMinDist + road.second) continue;
			dist[road.first] = curMinDist + road.second;
			pq.push({ dist[road.first], road.first });
		}
	}

	cout << dist[D];
}
