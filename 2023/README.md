# Day 1
Part two threw a spanner in the works with substrings like "eightwo" which ended up requiring a hacky solution.
# Day 2
Easy day today.
# Day 3
I initially got caught by an edge case that wasn't present in the test data - a part number against the right-hand edge of the engine schematic. Interestingly, this would have been easily handled by my initial plan of padding the schematic with a border of '.' characters to avoid having to handle the edge cases, but I think in general an approach which avoids editing the input data is preferred for Advent of Code problems.
# Day 4
Today the pattern of harder/easier continues. Another uncomplicated day.
# Day 5
While the logic for part two is obvious in retrospect, I missed it the first time through and had to see others' solutions prior to implementing my own.
# Day 6
A welcome reprieve after day 5, which allowed me to put in to practice some new Python I have learned:
```
times, records = [ list(map(int,line[9:].split()))
                    for line in data.splitlines() ]
```
Both the method of converting a list of strings to integers via a map function (rather than in a loop) as well as this recently-unbeknownst to me formatting of a for loop are very useful.
# Day 7
Easier than expected given the pattern seen so far. My solution has a lot of code duplication, but it was the easiest way to the answer.
# Day 8
I initially dismissed the LCM solution due to the possibilities of multiple end-points within each loop, but after I was unable to come up with a more elegent solution I went to reddit and saw that the input data is crafted in such a way as to have only one exit node per loop. An LCM algorithm being build into numpy makes the hardest part of the problem trivial.
# Day 9
Another unexpectedly easy day.
# Day 10
I was surprised to see that others had doubled the size of the map and then used a flood-fill algorithm for part two. I think that counting vertical bars is easier.
This is the first day of this year that I've been able to use a function from my "aoc_tools" helper library - forge_grid:
```
def forge_grid(l: list[str], t=int, sep=False) -> dict[tuple:type]:
    grid = {}
    for y, line in enumerate(l):
        if sep: line = line.split(sep)
        for x, element in enumerate(line):
            grid[x,y] = t(element)
    return grid
```
# Day 11
Another simple day.
# Day 12
I had to re-do my solution for part 1 when I saw part 2 in order to make the result cacheable in a useful way. I learned another useful trick, today and it is one that I've been particularly looking for):
```
return 1 if "#" not in input else 0
```
# Day 13
Short day today, but it has highlighted to me that I really need to write a good "Grid" class in my aoc_tools library. Not only would column/row getters be useful, but axes of symmetry could be useful in the future, too.
# Day 14
I was running into silly bugs in my initial implementation, so took this day as an opportunity to make a grid class:
```
class Grid:
    def __init__(self, input=[[]], t=int, sep=False):
        self.data = []
        for row in input:
            self.data.append([])
            if sep: row = row.split(sep)
            for element in row: self.data[-1].append(t(element))
            
    def __iter__(self):
        self.itvar = 0
        self.itreturn = self.data[0][0]
        return self
    
    def __next__(self):
        x = self.itreturn
        self.itvar += 1
        try: self.itreturn = self.data[self.itvar//len(self.data[0])][
            self.itvar%len(self.data[0])]
        except: raise StopIteration
        return x
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)
        
    def hashable(self) -> tuple:
        return tuple(map(tuple,self.data))
    
    def __hash__(self):
        return hash(self.hashable())
    
    def rows(self) -> list[list]:
        return self.data
        
    def columns(self) -> list[list]:
        return [[row[x] for row in self.data] for x in range(len(self.data[0]))]
        
    def row(self, y: int) -> list:
        return self.data[y]
        
    def column(self, x: int) -> list:
        return [row[x] for row in self.data]
        
    #fix to use .insert
    def add_rows(self, y:int, n=1, fill=None):
        new_data = []
        for data_y, row in enumerate(self.data):
            if data_y == y:
                for i in range(n): new_data.append([fill]*len(self.data[0]))
            new_data.append(row)
        if y >= len(self.data):
            for i in range(n): new_data.append([fill]*len(self.data[0]))
        self.data = new_data
    
    def append_rows(self, n=1, fill=None):
        self.add_rows(len(self.data),n,fill)
        
    def remove_rows(self, y=-1, n=1):
        for i in range(n): self.data.pop(y)
        
    # fix to use .insert
    def add_columns(self, x=-1, n=1, fill=None):
        for y, row in enumerate(self.data):
            new_row = []
            for data_x, value in enumerate(row):
                if data_x == x:
                    for i in range(n): new_row.append(fill)
                new_row.append(value)
            if x >= len(row):
                for i in range(n): new_row.append(fill)
            self.data[y] = new_row
        
    def append_columns(self, n=1, fill=None):
        self.add_columns(len(self.data[0]),n,fill)
        
    def remove_columns(self, x=-1, n=1):
        for i in range(len(self.data)):
            for j in range(n): self.data[i].pop(x)
        
    def get(self, x: int, y: int):
        return self.data[y][x]
        
    def set(self, x: int, y: int, value):
        self.data[y][x] = value
        return value
```
There are obviously some optimisations to be made, and a few more functions to add, but it should make future grid-based problems much easier.
I initially tried to solve this problem using a cache, but realised finding the loop would computationally better than running a billion times through a cached spin function.
# Day 15
Another simple day, which is a suprise this far into the month. I am expecting difficulty to start ramping tomorrow.
# Day 16
Another delay to the difficulty spike. I could do lots of optimisation to my solution (i.e. not using a global variable as the dictionary, requiring .reset() calls etcetera, but it works.
# Day 17
Not the most optimised solution, but it finishes in a couple of seconds. I was initially caught out by not including direction and length of time going in same direction as part of the states passed into the algorithm which was a slightly annoying fix. I will spend some time thinking about the optimal way to make a custom Dijkstra solution to put in my helper library that will be customisable enough to deal with problems like this. It will likely need verticies to be tuples and will need to accept at least two functions - one that determines the edges from a vertex and another that determines the weight.
# Day 18
Relatively straightforward with the shoelace formula, but the logic of having to remove half of the perimeter from the shoelace result to get the actual interior area due to the fact that the encricling trench is 1m wide took me some time. Implementing shoelace for part 1 made part 2 free.
