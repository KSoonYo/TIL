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

