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
