''' Advent of Code 2021 Day 19 solution 
    Big props to several Redditors for help on this mess, esp. p88h
'''

import itertools
from collections import Counter

def try_align(aligned, candidate):
    """ Try out a potential alignment and return the results """
    ret = []
    dl = []
    dp = None
    dpp = None

    # Check each dimension

    for dim in range(3):
        x = [pos[dim] for pos in aligned]

        # Check each direction and sign
        # This was such a mess all day long until I asked for help

        for (d,s) in [(0,1),(1,1),(2,1),(0,-1),(1,-1),(2,-1)]:
            if d == dp or d == dpp:
                continue
            t = [pos[d] * s for pos in candidate]
            w = [b - a for (a,b) in itertools.product(x, t)]
            c = Counter(w).most_common(1) # This library is a godsend
            if c[0][1] >= 12:
                break
        if c[0][1] < 12:
            return None
        (dpp, dp) = (dp, d)
        ret.append([v - c[0][0] for v in t])
        dl.append(c[0][0])
    return (list(zip(ret[0], ret[1], ret[2])), dl)

def main():
    """ driver for solution to puzzle """

    # Read in input and make array of scanners

    lines = open("19.txt").read().splitlines()
    scanners = []
    cur = None
    for l in lines:
        if l == "":
            continue
        elif l[0:3] == "---":
            cur = []
            scanners.append(cur)
        else:
            cur.append(tuple(map(int, l.split(","))))

    # set up main driver loop

    done = set()
    next = [ scanners[0] ]
    rest = scanners[1:]
    shifts = [(0,0,0)]

    # main driver loop, keep looping until next is empty

    while next:
        aligned = next.pop()
        tmp = []
        for candidate in rest:
            r = try_align(aligned, candidate)
            if r:
                (updated, shift) = r
                shifts.append(shift)
                next.append(updated)
            else:
                tmp.append(candidate)
        rest = tmp
        done.update(aligned)

    # 19a was terrible, 19b was very easy because it was just extracting a data piece from my 19a solution

    print("19a -> ",len(done))
    sxs = itertools.product(shifts,shifts)
    print("19b -> ",max(sum(abs(a-b) for (a,b) in zip(l,r)) for l,r in sxs))

if __name__ == "__main__":
    main()

