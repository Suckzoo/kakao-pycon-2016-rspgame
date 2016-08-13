import player1
import player2

r1 = []
r2 = []

for i in range(1000):
    h1 = player1.show_me_the_hand(r2)
    h2 = player2.show_me_the_hand(r1)
    if h1 == h2:
        print('match %d of 1000: tie' % i)
        r = 0
    elif (h1 == 'gawi' and h2 == 'bo') or (h1 == 'bawi' and h2 == 'gawi') or (h1 == 'bo' and h2 == 'bawi'):
        print('match %d of 1000: p1 win' % i)
        r = 1
    else:
        print('match %d of 1000: p2 win' % i)
        r = -1
    r1.append((h1, r))
    r2.append((h2, -r))