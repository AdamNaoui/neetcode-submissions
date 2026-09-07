from typing import List


class UnionFind:
    def __init__(self, n: int):
        # parent[i] est le parent du sommet i
        self.parent = list(range(n + 1))

        # Taille de l'ensemble dont i est le représentant
        self.size = [1] * (n + 1)

    def find(self, x: int) -> int:
        # Compression de chemin
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        # Même représentant : ajouter cette arête créerait un cycle
        if root_x == root_y:
            return False

        # Union by size : on attache le plus petit arbre au plus grand
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union_find = UnionFind(n)

        for a, b in edges:
            # Si la fusion échoue, a et b sont déjà connectés
            if not union_find.union(a, b):
                return [a, b]

        return []