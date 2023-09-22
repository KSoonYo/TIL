#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings);

int main(){
  vector<string> players = {"mumu", "soe", "poe", "kai", "mine"};
  vector<string> callings = {"kai", "kai", "mine", "mine"};
  vector<string> result =  solution(players, callings);
 
  return 0;
}

vector<string> solution(vector<string> players, vector<string> callings) {
    map<string, int> table;
    
    int N = players.size();
    for(int i = 0; i < N; i++){
        string player = players[i];
        table.insert({player, i + 1});
    }
       
    for(string calledPlayer : callings){
        int prev_rank = table[calledPlayer];
        int next_rank = prev_rank - 1;
        string changedPlayer = players[prev_rank - 2];
        
        // swap
        string temp = calledPlayer;
        players[prev_rank - 1] = changedPlayer;
        players[next_rank - 1] = temp;
        
        table[changedPlayer] = prev_rank;
        table[calledPlayer] = next_rank;
    }

    return players;
}

