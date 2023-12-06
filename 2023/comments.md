# Day 1
Part two threw a spanner in the works with substrings like "eightwo" which ended up requiring a hacky solution.
# Day 2
Easy day today.
# Day 3
I initially got caught by an edge case that wasn't present in the test data - a part number against the right-hand edge of the engine schematic. Interestingly, this would have been easily handled by my initial plan of padding the schematic with a border of '.' characters to avoid having to handle the edge cases, but I think in general an approach which avoids editing the input data is preferred for Advent of Code problems.
# Day 4
Today the pattern of harder/easier continues. Another uncomplicated day.
# Day 5
I am going to come back to day 5, as part two is giving me some headaches.
# Day 6
A welcome reprieve after day 5, which allowed me to put in to practice some new Python I have learned:
```
times, records = [ list(map(int,line[9:].split()))
                    for line in data.splitlines() ]
```
Both the method of converting a list of strings to integers via a map function (rather than in a loop) as well as this recently-unbeknownst to me formatting of a for loop are very useful.
