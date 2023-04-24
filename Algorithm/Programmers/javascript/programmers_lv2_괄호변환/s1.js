function check(w) {
  const stack = [];
  for (let i = 0; i < w.length; i++) {
    if (stack.length == 0 && w[i] == ")") {
      return false;
    }
    if (w[i] == "(") {
      stack.push("(");
    } else {
      stack.pop();
    }
  }
  if (stack.length > 0) {
    return false;
  }
  return true;
}

function reverse(w) {
  let reversed = "";
  reverse_table = { "(": ")", ")": "(" };
  for (const char of w) {
    reversed += reverse_table[char];
  }
  return reversed;
}

function main(p) {
  var result = "";
  if (check(p)) {
    return p;
  }
  const table = new Map();
  table.set("(", 0);
  table.set(")", 0);
  let i = 0;
  let [u, v] = [null, null];
  while (i < p.length) {
    table.set(p[i], table.get(p[i]) + 1);
    if (table.get("(") === table.get(")")) {
      u = p.slice(0, i + 1);
      v = p.slice(i + 1);
      break;
    }
    i++;
  }
  if (check(u)) {
    return u + main(v);
  }
  return "(" + main(v) + ")" + reverse(u.slice(1, i));
}

function solution(p) {
  var answer = main(p);
  return answer;
}

// best solution
function reverse(str) {
  return str
    .slice(1, str.length - 1)
    .split("")
    .map((c) => (c === "(" ? ")" : "("))
    .join("");
}

function solution(p) {
  if (p.length < 1) return "";

  let balance = 0;
  let pivot = 0;
  do {
    balance += p[pivot++] === "(" ? 1 : -1;
  } while (balance !== 0);

  const u = p.slice(0, pivot);
  const v = solution(p.slice(pivot, p.length));

  if (u[0] === "(" && u[u.length - 1] == ")") return u + v;
  else return "(" + v + ")" + reverse(u);
}
