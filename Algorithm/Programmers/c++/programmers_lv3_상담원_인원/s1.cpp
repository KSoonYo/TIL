#include <string>
#include <vector>
#include <limits>
#include <iostream>
#include <queue>

using namespace std;

int answer;

struct Info{
    int start;
    int ing;
    Info(int S, int I) : start(S), ing(I){}
};

struct cmp{
    bool operator()(Info a, Info b){
        return a.start + a.ing > b.start + b.ing;
    }
};

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
