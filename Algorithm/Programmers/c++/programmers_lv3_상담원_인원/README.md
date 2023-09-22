# 문제

https://school.programmers.co.kr/learn/courses/30/lessons/214288

# 풀이

- 입력 범위가 작아서 완전 탐색으로 풀이 가능
- k개의 타입 별로 한 명씩 배치하고, 남은 멘토(n - k)를 재배치하는 방법을 탐색
  - 각각의 배치 case에 대해 최솟값 갱신
  - priority_queue 사용

```c++
#include <string>
#include <vector>
#include <limits>
#include <iostream>
#include <queue>

using namespace std;

int answer;

// 상담 시간 정보에 대한 자료형 정의
struct Info{
    int start;
    int ing;
    Info(int S, int I) : start(S), ing(I){}
};

// 우선순위 큐 비교 연산자
// 최소힙 유지
struct cmp{
    bool operator()(Info a, Info b){
        return a.start + a.ing > b.start + b.ing;
    }
};


/**
 * table: 타입 별 상담 신청 정보 기록 테이블
 * rest: 배치 가능한 전체 상담원 수
 * k: 배치 가능한 타입 유형 수
 * allow: 현재 배치된 상담원 수
 * waiting: 누적 대기 시간
 * typ: 현재 상담 유형
 */
void search(vector<vector<Info>> &table, int rest, int k, int allow, int waiting=0, int typ=1){

    if(k == 0){
        answer = min(answer, waiting);
        return;
    }
    for(int extra = 0; extra < rest + 1; extra++){
        priority_queue<Info, vector<Info>, cmp> pq;
        int temp = 0;
        for(Info info : table[typ]){
            int start = info.start; int ing = info.ing;
            while(!pq.empty() && (pq.top().start + pq.top().ing) <= start){
                pq.pop();
            }

            if(pq.size() < (allow + extra)){
                pq.push(Info(start, ing));
            } else{
                int prev_e = pq.top().start + pq.top().ing;
                int extend = (prev_e - start);
                pq.pop();

                temp += extend;
                pq.push(Info(start + extend, ing));
            }
        }
        search(table, rest - extra, k - 1, 1, waiting + temp, typ + 1);
    }
}

int solution(int k, int n, vector<vector<int>> reqs) {
    answer = numeric_limits<int>::max();

    vector<vector<Info>> table(k + 1);

    for(vector<int> req : reqs){
        int start = req[0]; int ing = req[1]; int typ = req[2];
        Info info(start, ing);
        table[typ].push_back(info);
    }
    int rest = n - k;
    search(table, rest, k, 1);
    return answer;
}

```
