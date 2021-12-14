from collections import defaultdict

with open('inputs/p1/input.txt') as input:
  rows = [x for x in input.read().strip().split("\n")]
  input.close()

adj = defaultdict(list)

for row in rows:
    a, b = row.split("-")
    adj[a].append(b)
    adj[b].append(a)

def paths(cur: str, seen, dup):
    if cur == 'end':
        return 1
    if cur == "start" and seen:
        return 0
    if cur.islower() and cur in seen:
        if dup is None:
            dup = cur
        else:
            return 0
    seen = seen | {cur}
    out = 0
    for thing in adj[cur]:
        out += paths(thing, seen, dup)
    return out

out = paths("start", set(), None)

print(out)