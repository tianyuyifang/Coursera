
#no data point will exceed 1e9

class disjoint_set:
    def __init__(self, data):
        MAX = 100
        self.size = len(data)
        #set parent and rank to be a list of size MAX
        self.parent = [None]*MAX
        self.rank = [None]*MAX
        for point in data:
            self.MakeSet(point)
    def MakeSet(self, value):
        self.parent[value] = value
        self.rank[value] = 0
        self.size += 1
    def Find(self, value):
        #consider the case where value is not in the sets
        if self.parent[value] == None:
            return "Not Found"
        paths = []
        while value != self.parent[value]:
            paths.append(value)
            value = self.parent[value]
        for node in paths:
            self.parent[node] = value
        return value
    def Union(self, v1, v2):
        id_1 = self.Find(v1)
        id_2 = self.Find(v2)
        if "Not Found" in [id_1, id_2]:
            return
        if id_1 == id_2:
            return
        rank_1 = self.rank[id_1]
        rank_2 = self.rank[id_2]
        if rank_1 > rank_2:
            self.parent[id_2] = id_1
        elif rank_2 > rank_1:
            self.parent[id_1] = id_2
        else:
            self.parent[id_1] = id_2
            self.rank[id_2] += 1  



