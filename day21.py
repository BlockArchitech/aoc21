from itertools import cycle, product
from collections import Counter, defaultdict

data = """\
Player 1 starting position: 6
Player 2 starting position: 2
"""

def wrap10(n):
    return n % 10 or 10

def practice(p1, p2, goal=1000, rolls=3):
    dd = cycle(range(1, 101))
    s1 = s2 = 0
    rollcount = 0
    while True:
        p1 = wrap10(p1 + sum(next(dd) for _ in range(rolls)))
        s1 += p1
        rollcount += 3
        if s1 >= goal:
            break
        p2 = wrap10(p2 + sum(next(dd) for _ in range(rolls)))
        s2 += p2
        rollcount += 3
        if s2 >= goal:
            break
    return min(s1, s2) * rollcount


part_1 = practice(6, 2)
print('part_1 =', part_1)

## Part 2

possible_moves = [sum(x) for x in product((1, 2, 3), repeat=3)]
move_counts = sorted(Counter(possible_moves).items())

def move_a(verse):
    nextverse = defaultdict(int)
    for ((ascore, apos, bscore, bpos), vcount), (move, movecount) in product(verse.items(), move_counts):
        apos = wrap10(apos + move)
        ascore += apos
        nextverse[(ascore, apos, bscore, bpos)] += vcount * movecount
    return nextverse

def move_b(verse):
    nextverse = defaultdict(int)
    for ((ascore, apos, bscore, bpos), vcount), (move, movecount) in product(verse.items(), move_counts):
        bpos = wrap10(bpos + move)
        bscore += bpos
        nextverse[(ascore, apos, bscore, bpos)] += vcount * movecount
    return nextverse

def cull_winners(verse, completed):
    for k in list(verse):
        (ascore, apos, bscore, bpos) = k
        if ascore >= 21 or bscore >= 21:
            completed.append((ascore, bscore, verse[k]))
            del verse[k]


verse = {(0, 6, 0, 2): 1}
completed = []
while verse:
    verse = move_a(verse)
    cull_winners(verse, completed)
    verse = move_b(verse)
    cull_winners(verse, completed)

part_2  = max(sum(c for (a, b, c) in completed if a >= 21),
              sum(c for (a, b, c) in completed if b >= 21))

print('part_2 =', part_2)
