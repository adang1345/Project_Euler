"""https://projecteuler.net/problem=186"""

import networkx as nx


g = nx.Graph()
g.add_nodes_from(range(1, 1_000_001))

calls = 0
s = [(100003 - 200003*k + 300007*k**3) % 1_000_000 for k in range(1, 56)]
friends = {524_287}
i = 0
while len(friends) < 990_000:
    if i >= len(s) - 1:
        s.append((s[-24] + s[-55]) % 1_000_000)
        s.append((s[-24] + s[-55]) % 1_000_000)
    if s[i] != s[i+1]:
        if s[i] in friends and s[i+1] not in friends:
            friends.update(nx.dfs_preorder_nodes(g, s[i+1]))
        elif s[i] not in friends and s[i+1] in friends:
            friends.update(nx.dfs_preorder_nodes(g, s[i]))
        g.add_edge(s[i], s[i+1])
        calls += 1
    i += 2
print(calls)
