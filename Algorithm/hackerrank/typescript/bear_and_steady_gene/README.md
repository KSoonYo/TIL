# 문제 설명
https://www.hackerrank.com/challenges/bear-and-steady-gene/problem

# 풀이
- two pointer 접근법
  - 각각의 염기 서열의 최대 개수는 문제 조건에 따라 `(n / 4)` 개
  - 입력받은 gene의 `A`, `C`, `T`, `G`  개수를 각각 기록
  - right pointer가 한 칸씩 오른쪽으로 움직이면서 가리키고 있는 염기 서열의 개수 - 1.
  - 현재 table에 저장된 모든 염기서열의 개수가 최대 개수 이하인지 check
    - maximum을 넘는 염기 서열의 일부를 부족한 염기서열로 변환하여 개수를 채우므로 maxmimum을 넘는 염기서열이 없다면 곧 현재 유전자가 steady함을 보장
    - 모두 이하라면 left pointer는 한 칸씩 오른쪽으로 움직이면서 가리키고 있는 염기 서열의 개수 + 1.   
    - check를 계속 하면서 `left <= right` 까지 반복
    - 반복하면서 최소 길이 갱신

```typescript
type tableType = {
  [index: string]: number
}


function steadyGene(gene:string): number {
  let answer:number = Infinity;
  const n = gene.length;
  const maximum = Math.floor(n / 4);  

  const countTable:tableType = {'A': 0, 'G': 0, 'C': 0, 'T': 0};
  for(let i = 0; i < n; i++){
    const g = gene[i];
    countTable[g]++;
  }

  if(check(countTable, maximum)){
    return 0;
  }

  let left = 0;
  for(let right = 0; right < n; right++){
    countTable[gene[right]]--;
    while(left <= right){
      if(!check(countTable, maximum)){
        break;
      }
      answer = Math.min(answer, right - left + 1);
      countTable[gene[left]]++;
      left++;
    }
  }
  return answer;
}

function check(table:tableType, maximum:number){
  for(let key in table){
    if(table[key] > maximum){
      return false
    }
  }
  return true
}

```
