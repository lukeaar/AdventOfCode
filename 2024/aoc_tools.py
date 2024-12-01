import re, heapq, itertools
from collections import defaultdict

####################
# Input Processing #
####################

# Simple conversions / extractions #
#----------------------------------#

def find_il(s: str) -> list[int]:
    return [int(n) for n in re.findall(r'-?\d+', s)]

def retype_sl(l: list[str], t=int) -> list[type]:
    return list(map(t,l))

# Useful data structures #
#------------------------#

def forge_dict(l: list[str], kt=str, vt=int, sep=',') ->dict:
    d = {}
    for line in l:
        k, v = line.split(sep)
        d[kt(k)] = vt(v)
    return d

def forge_grid(l: list[str], t=int, sep=False) -> dict:
    grid = {}
    for y, line in enumerate(l):
        if sep: line = line.split(sep)
        for x, element in enumerate(line):
            grid[x,y] = t(element)
    return grid

#####################
# Utility Functions #
#####################

def extrapolate_next_value(sequence: list) -> int:
    differences = [sequence[i] - sequence[i-1] for i in range(1,len(sequence))]
    if any(differences):
        return sequence[-1] + extrapolate_next_value(differences)
    return sequence[-1]

#TODO - Sheolace algorithm (see 18)

###########
# Classes #
###########

class Grid:
    def __init__(self, input=[[]], t=int, sep=False):
        self.data = []
        for row in input:
            self.data.append([])
            if sep: row = row.split(sep)
            for element in row:
                if element != None: self.data[-1].append(t(element))
                else:               self.data[-1].append(element)
        self.row_length = len(self.data[0])
        self.column_length = len(self.data)
            
    @staticmethod
    def new(x:int, y:int, value=None):
        g = []
        for i in range(y): g.append([value]*x)
        return Grid(g, type(value))
            
    def __iter__(self):
        self.itvar = 0
        self.itreturn = self.data[0][0]
        return self
    
    def __next__(self):
        x = self.itreturn
        self.itvar += 1
        if self.itvar < self.row_length * self.column_length:
            self.itreturn = self.data[self.itvar//self.row_length][
            self.itvar%self.row_length]
        elif self.itvar > (self.row_length * self.column_length):
            raise StopIteration
        return x
    
    def __len__(self):
        return self.column_length * self.row_length
    
    def __str__(self):
        output = ""
        for row in self.data:
            for c in row: output += str(c) + ' '
            output = output[:-1] + '\n'
        return output[:-1]

    def __repr__(self):
        return repr(self.data)
        
    def hashable(self) -> tuple:
        return tuple(map(tuple,self.data))
    
    def __hash__(self):
        return hash(self.hashable())
    
    def __copy__(self):
        cpy = Grid()
        cpy.data = self.data
        cpy.row_length = self.row_length
        cpy.column_length = self.column_length
        return cpy
    
    def __getitem__(self, key: tuple):
        x, y = key
        if x >= self.row_length or x < 0: x = x % self.row_length
        if y >= self.column_length or y < 0: y = y % self.column_length
        return self.data[y][x]
    
    def __setitem__(self, key: tuple, value):
        x, y = key
        self.data[y][x] = value
        
    def __contains__(self, value):
        for row in self.data:
            if value in row: return True
        return False
    
    def __eq__(self, value):
        return hash(self) == hash(value)
    
    def __ne__(self, value):
        return hash(self) != hash(value)
    
    def __bool__(self):
        return bool(self.data)
    
    def row_len(self) -> int:
        return self.row_length

    def column_len(self) -> int:
        return self.column_length
    
    def rows(self) -> list[list]:
        return self.data
        
    def columns(self) -> list[list]:
        return [[row[x] for row in self.data] for x in range(self.row_length)]
        
    def row(self, y: int) -> list:
        return self.data[y]
        
    def column(self, x: int) -> list:
        return [row[x] for row in self.data]

    def add_rows(self, y:int, n=1, fill=None):
        for i in range(n): self.data.insert(y,[fill]*self.row_length)
        self.column_length += n
    
    def append_rows(self, n=1, fill=None):
        self.add_rows(len(self.data),n,fill)
        
    def remove_rows(self, y=-1, n=1):
        for i in range(n): self.data.pop(y)
        self.column_length -= n
    
    def add_columns(self, x=-1, n=1, fill=None):
        for y in range(self.column_length):
            for i in range(n): self.data[y].insert(x,fill)
        self.row_length += n
        
    def append_columns(self, n=1, fill=None):
        self.add_columns(len(self.data[0]),n,fill)
        
    def remove_columns(self, x=-1, n=1):
        for i in range(len(self.data)):
            for j in range(n): self.data[i].pop(x)
        self.row_length -= n
        
    def count(self, value) -> int:
        cnt = 0
        for row in self.data: cnt += row.count(value)
        return cnt
    
    def clear(self):
        self.data = [[]]
        self.row_length = 0
        self.column_length = 0
        
    def index(self, value) -> tuple:
        for y in range(self.column_length):
            for x in range(self.row_length):
                if self.data[y][x] == value: return (x,y)
        raise ValueError
    
    def enum_to_coords(self, enum: int) -> tuple:
        return (enum%self.row_length,enum//self.row_length)
    
    def coords_to_enum(self, coords: tuple) -> int:
        return coords[1] * self.row_length + coords[0]
    
    def adjacent_coords(self, coords: tuple) -> list:
        output = []
        x,y = coords
        if x > 0:                       output.append((x-1,y))
        if x < self.row_length-1:       output.append((x+1,y))
        if y > 0:                       output.append((x,y-1))
        if y < self.column_length-1:    output.append((x,y+1))
        return output
    
    def dijkstra(self, start=(0,0), end=None,
                 neighbours=adjacent_coords, weight=__getitem__) -> list:
        weights = defaultdict(lambda :float('inf'))
        weights[start] = 0
        previous = defaultdict(lambda :None)
        queue = [(0,) + start]
        heapq.heapify(queue)
        while len(queue):
            current = heapq.heappop(queue)
            current_weight = current[:1]
            current = current[1:]
            for neighbour in neighbours(current):
                new_weight = current_weight + weight(neighbour)
                if new_weight < weights[neighbour]:
                    weights[neighbour] = new_weight
                    previous[neighbour] = current
                    heapq.heappush(queue,(new_weight,)+neighbour)
        return [weights,previous]
    
    #untested
    def held_karp(self):
        if self.row_len() != self.column_len(): raise ValueError("Not square")
        n = self.row_len()
        dp = {}
        for i in range(n):
            if self[i,i] != 0: raise ValueError("Diagonal not 0")
            if i == 0: continue
            dp[(frozenset([0,i]), i)] = self[0,i]
        for subset_size in range(2, n):
            for subset in itertools.combinations(range(1,n), subset_size):
                subset = frozenset(subset) | {0}
                for end in subset:
                    if end == 0: continue
                    dp[(subset, end)] = min(
                        dp[(subset - {end}, prev)] + self[prev,end]
                        for prev in subset if prev != end and prev != 0
                    )
        subset = frozenset(range(n))
        return min(dp[(subset, end)] + self[end,0] for end in range(1, n))
    
    def held_karp_anystartend_reversed(self):
        if self.row_len() != self.column_len(): raise ValueError("Not square")
        n = self.row_len()
        dp = {start: {} for start in range(n)}
        for start in range(n):
            if self[start,start] != 0: raise ValueError("Diagonal not 0")
            dp[start][(frozenset([start]), start)] = 0
            for i in range(n):
                if i == start: continue
                dp[start][(frozenset([i]), i)] = float('-inf')
                dp[start][(frozenset([start,i]),i)] = self[start,i]
        for subset_size in range(2, n+1):
            for subset in itertools.combinations(range(n), subset_size):
                subset = frozenset(subset)
                for start in range(n):
                    if start not in subset: continue
                    for end in subset:
                        dp[start][(subset,end)] = max(
                            dp[start].get((subset - {end}, prev), float('-inf')) + self[prev,end]
                            for prev in subset if prev != end
                        )
        max_cost = float('-inf')
        subset = frozenset(range(n))
        for start in range(n):
            for end in range(n):
                if start == end: continue
                max_cost = max(max_cost, dp[start][(subset,end)])
        return max_cost
    
    def held_karp_anystartend(self):
        if self.row_len() != self.column_len(): raise ValueError("Not square")
        n = self.row_len()
        dp = {start: {} for start in range(n)}
        for start in range(n):
            if self[start,start] != 0: raise ValueError("Diagonal not 0")
            dp[start][(frozenset([start]), start)] = 0
            for i in range(n):
                if i == start: continue
                dp[start][(frozenset([i]), i)] = float('inf')
                dp[start][(frozenset([start,i]),i)] = self[start,i]
        for subset_size in range(2, n+1):
            for subset in itertools.combinations(range(n), subset_size):
                subset = frozenset(subset)
                for start in range(n):
                    if start not in subset: continue
                    for end in subset:
                        dp[start][(subset,end)] = min(
                            dp[start].get((subset - {end}, prev), float('inf')) + self[prev,end]
                            for prev in subset if prev != end
                        )
        min_cost = float('inf')
        subset = frozenset(range(n))
        for start in range(n):
            for end in range(n):
                if start == end: continue
                min_cost = min(min_cost, dp[start][(subset,end)])
        return min_cost
    

#################################
# Advent of Code initialisation #
#################################

def initialise(year):
    year = str(year)
    for i in range(1,26):
        day = str(i)
        filename = day + ".py"
        if len(filename) == 4: filename = '0' + filename
        f = open(filename, 'w')
        f.write("# " + year + " Day " + day + "\n\n" +
                "import aoc_tools as aoc\n" +
                "from aocd import get_data, submit\n\n" +
                "data = get_data(day=" + day + ", year=" + year + ")\n\n" +
                "def part_a():\n" +
                "    answer = 0\n\n" +
                "    return answer\n\n" +
                "def part_b():\n" +
                "    answer = 0\n\n" +
                "    return answer\n\n" +
                "submit(part_a(), part=\"a\", day=" + day + ", year=" + year + ")\n" +
                "#submit(part_b(), part=\"b\", day=" + day + ", year=" + year + ")")
        f.close()
    f = open("example", 'w')
    f.write("")
    f.close()