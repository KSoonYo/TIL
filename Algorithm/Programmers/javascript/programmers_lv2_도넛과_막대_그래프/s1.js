const MAX_LENGTH = 1000001;

const table = Array.from(new Array(MAX_LENGTH), () => [0, 0]);
const routes = Array.from(new Array(MAX_LENGTH), () => []);
var answer = [0, 0, 0, 0];

function search(start) {
  q = [start];
  visited = new Set();

  while (q.length > 0) {
    node = q.shift();

    routes[node].forEach((nextNode) => {
      const info = table[nextNode];
      if (info[0] >= 1 && info[1] === 0) {
        answer[2] += 1;
        return;
      }
      if (info[0] >= 2 && info[1] === 2) {
        answer[3] += 1;
        return;
      }

      if (visited.has(nextNode)) {
        answer[1] += 1;
        return;
      }
      q.push(nextNode);
      visited.add(nextNode);
    });
  }
}

function solution(edges) {
  edges.forEach((edge) => {
    const [source, target] = edge;
    table[source][1] += 1; // fan out
    table[target][0] += 1; // fan in

    routes[source].push(target);
  });

  let start = 0;
  for (let i = 0; i <= MAX_LENGTH; i++) {
    const info = table[i];
    if (info[0] === 0 && info[1] >= 2) {
      start = i;
      answer[0] = i;
      break;
    }
  }

  search(start);

  return answer;
}
