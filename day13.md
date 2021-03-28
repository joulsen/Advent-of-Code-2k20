# Advent of Code 2020 Day 13 Part 2 Explanation

*This markdown document details my thought process behind the solution for AoC 2020 Day 13 Part 2. The file uses inline math and as such to view the document properly, a markdown viewer/editor with LaTeX math support is needed.*

Let's examine the example input

```
7,13,x,x,59,x,31,19
```

A bus $b$ departs at time $t$ if $t \text{ mod } b = 0$. This is consistent with all busses leaving at $t=0$ since $t \text{ mod } 0 = 0$. 

We denote $t_7$ a point in time at which bus 7 departs. We denote $t_{7,13}$ a time when bus 7 departs and bus 13 departs one minute after. We denote $t_{7,13,x,x,59}$ a time when bus 7 departs, followed by bus 13, followed by 2 minutes passing and bus 59 departing. This notation is further expanded to the whole input.

We realize that at $t_{7,13,x,x,59,x,31,19}$ must also occur $t_{7,13,x,x,59,x,31}, t_{7,13,x,x,59}$ and $t_{7,13}$. Furthermore, at $t_{7,13,x,x,59,x,31}$ must also occur $t_{7,13,x,x,59}$ and $t_{7,13}$. As such, if we figure out when $t=t_{7,13}$ occurs, we limit $t$. By searching this limited $t$ we may find $t_{7,13,x,x,59}$ and limit $t$ further and so on until we find the final time.

$t_{7,13}$ is not hard to find manually. Iterating $t = 7x$ for some increasing integer $x$ while checking for $(t + 1)\text{ mod } 7 = 0$ shows that the first $t_{7,13}$ occurs at $t=77$ . Below is table detailing when it happens:

| Time | Bus 7 | Bus 13 | Bus 59 | Bus 31 | Bus 19 |
| ---- | ----- | ------ | ------ | ------ | ------ |
| 76   |       |        |        |        | D      |
| 77   | D     |        |        |        |        |
| 78   |       | D      |        |        |        |
| 79   |       |        |        |        |        |

Now, how long does it take before this scenario $t_{7,13}$ occurs again? Well, bus 7 only departs every 7 minutes and bus 13, which departs one minute later, only departs every 13 minutes, so the next $t_{7,13}$ is at least $13 + 1$ minutes in the future. Looking at $t=77+13+1 = 91$ we see that:

| Time | Bus 7 | Bus 13 | Bus 59 | Bus 31 | Bus 19 |
| ---- | ----- | ------ | ------ | ------ | ------ |
| 90   |       |        |        |        |        |
| 91   | D     | D      |        |        |        |
| 92   |       |        |        |        |        |

This is sort of like $t=0$ since bus 7 and bus 13 departs at the same time. Hence we would expect $t_{7,13}$ to occur again at $t=91 + 77 = 168$:

| Time | Bus 7 | Bus 13 | Bus 59 | Bus 31 | Bus 19 |
| ---- | ----- | ------ | ------ | ------ | ------ |
| 167  |       |        |        |        |        |
| 168  | D     |        |        |        |        |
| 169  |       | D      |        |        |        |

Hence $t_{7,13} = 77 + 91x$ for some integer $x$. This value $91$ might seem arbitrary, but it is actually the least common multiple of $7$ and $13$, which is simply their product as they are both prime numbers. This makes sense: We expect $t \text{ mod } 7 = 0$ to occur every $t=7$ and  $t \text{ mod } 13 = 0$ to occur every $t=13$ and thereby $t \text{ mod } 7 = 0,\quad t \text{ mod } 13 = 0$ to occur at $t$ equals their least common multiple $t=13 \cdot 7 = 91$.

Now by iterating $t = 77 + 91x$ we can check for $(t+4) \text{ mod } 59 = 0$ and find when the first $t_{7,13,x,x,59}$ occurs:

| Time | Bus 7 | Bus 13 | Bus 59 | Bus 31 | Bus 19 |
| ---- | ----- | ------ | ------ | ------ | ------ |
| 350  | D     |        |        |        |        |
| 351  |       | D      |        |        |        |
| 352  |       |        |        |        |        |
| 353  |       |        |        |        |        |
| 354  |       |        | D      |        |        |

Just like before we expect to find the next $t_{7,13,x,x,59}$ at $350$ plus the least common multiple of $7, 13, 59$ which is $\text{lcm}(7,13,59) = 7 \cdot 13 \cdot 59 = 5369$ i.e. $t_{7,13,x,x,59} = 350 + 5369x$. At $x = 1$ we have:

| Time | Bus 7 | Bus 13 | Bus 59 | Bus 31 | Bus 19 |
| ---- | ----- | ------ | ------ | ------ | ------ |
| 5719 | D     |        |        |        | D      |
| 5720 |       | D      |        |        |        |
| 5721 |       |        |        |        |        |
| 5722 |       |        |        |        |        |
| 5723 |       |        | D      |        |        |

This may be repeated until the first $t_{7,13,x,x,59,x,31,19}$ is found thereby acquiring the algorithm:

```
t = 0
interval = 1
for next_bus in busses:
    while True:
        if (t + offset) % next_bus == 0:
            interval *= next_bus
            break
        t += interval
```

For the first iteration of the for loop *next_bus* will be 7 and the if-condition will trigger immediately setting the interval to 7. The offset value is the corresponding minute offset for each bus, which in the example should be the list:

```
offsets = [0,1,4,6,7]
```

since bus 7 must depart 0 minutes from $t$, bus 13 must depart 1minute from $t$, bus 59 must depart 4 minutes and so on. This may be generated in Python by:

```python
>> import numpy as np
>> lines = np.array([7,13,"x","x",59,"x",31,19])
>> np.argwhere(lines != "x")
array([[0],
       [1],
       [4],
       [6],
       [7]], dtype=int64)
```

