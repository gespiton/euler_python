"""

  a  High Card
  b  One Pair
    Two Pairs
    Three of a Kinds of the sa
    Straight:
    Flush
    Full House
    Four of a Kind
    Straight Flush
  j  Royal Flush

"""
trans = dict()
for i in range(1, 10):
    trans[str(i)] = '0' + str(i)

trans.update({'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'})
# print(trans)


" make the function call another"


class hand():
    """docstring for hand"""

    def __init__(self, card):
        self.rank = []
        self.card = card
        self.abort = False                                    # for abortion
        self.card = self.card.split(sep=' ')
        self.card = sorted([trans[i[0]] + i[1] for i in self.card])
        self.RoyalFlush()
        self.fill()

    def fill(self):
        for i in range(len(self.rank), 10):
            self.rank.append('0')

    def RoyalFlush(self):
        color = self.card[0][2]
        s = str()
        for c in self.card:
            s += c[:2]
            if c[2] != color:
                self.abort = True
                self.rank.append('0')
                self.StraightFlush()
                return
        if s == '1011121314':
            self.rank.append('1')                    # 0 if not, 1 if yes
        else:
            self.rank.append('0')
            self.StraightFlush()

    def StraightFlush(self):
        color = self.card[0][2]
        card_li = list()
        for i in self.card:
            if i[2] != color:
                self.rank.append('0')
                self.four_of_a_Kind()
                return
            card_li.append(i[:2])
        if int(card_li[4]) - int(card_li[0]) == 4 and len(set(card_li)) == 5:
            self.rank.append('1' + self.card[4][:2])
            self.abort = True
        else:
            self.rank.append('0')
            self.four_of_a_Kind()

    def four_of_a_Kind(self):
        card_li = [i[:2] for i in self.card]
        card_set = set(i[:2] for i in self.card)
        if len(card_set) <= 2:
            if card_li.count(card_li[0]) == 1:
                self.rank.append('1' + self.card[1][:2] + self.card[0][:2])
            # >= 4 because we might get 5 card with the same value
            elif card_li.count(card_li[0]) >= 4:
                self.rank.append('1' + self.card[1][:2] + self.card[4][:2])
                self.abort = True
            else:
                self.rank.append('0')
                self.full_house()
        else:
            self.rank.append('0')
            self.full_house()

    def full_house(self):
        card_li = [i[:2] for i in self.card]
        card_set = set(i[:2] for i in self.card)
        if len(card_set) != 2:
            self.rank.append('0')
            self.flush()
        else:
            if card_li.count(card_li[0]) == 2:
                self.rank.append('1' + card_li[4] + card_li[0])
                self.abort = True
            else:
                self.rank.append('1' + card_li[0] + card_li[4])
                self.abort = True

    def flush(self):  # 5
        card_color = set(i[2] for i in self.card)
        if len(card_color) == 1:
            self.abort = True
            self.rank.append('1' + ''.join([ii[:2] for ii in self.card[::-1]]))
            # for i in range(1, 6):
            #    if i == 1:
            #        ref[4] += card_li[i - 1]
            #    else:
            #        if ref[4][len(ref[4]) - 2:] != card_li[i - 1]:
            #            ref[4] += card_li[i - 1]
        else:
            self.rank.append('0')
            self.straight()

    def straight(self):
        card_li = [i[:2] for i in self.card]
        if int(card_li[4]) - int(card_li[0]) == 4 and len(set(card_li)) == 5:
            self.rank.append('1' + self.card[4][:2])
            self.abort = True
        else:
            self.rank.append('0')
            self.three()

    def three(self):
        card_li = [i[:2] for i in self.card]
        card_set = set(i[:2] for i in self.card)
        if card_li.count(card_li[2]) == 3:
            buf = card_li[2]
            while card_li.count(buf) != 0:
                card_li.remove(buf)
            self.rank.append('1' + buf + ''.join(card_li[::-1]))
        else:
            self.rank.append('0')
            self.two_pairs()

    def two_pairs(self):
        card_li = [i[:2] for i in self.card]
        card_set = set(i[:2] for i in self.card)
        if len(card_set) == 3:
            self.abort == True
            for i in range(5):
                if card_li.count(card_li[i]) == 1:
                    buf = card_li.pop(i)
                    break
            card_li.pop(0)
            card_li.pop(2)
            card_li.insert(0, buf)
            self.rank.append('1' + ''.join(card_li[::-1]))
        else:
            self.rank.append('0')
            self.pair()

    def pair(self):
        card_li = [i[:2] for i in self.card]
        card_set = set(i[:2] for i in self.card)
        if len(card_set) == 4:
            self.abort = True
            for i in range(5):
                if card_li.count(card_li[i]) == 2:
                    buf = card_li.pop(i)
                    break
            card_li.remove(buf)
            self.rank.append('1' + buf + ''.join(card_li[::-1]))
        else:
            self.rank.append('0')
            self.high()

    def high(self):
        card_li = [i[:2] for i in self.card]
        self.rank.append(''.join(card_li[::-1]))


# ha = hand('5h 5c 6s 7s Kd')
# ha = hand('3C 3D 3S 9S 9D')
# ha = hand('9H 7E 9H 9H 9H')
# ha = hand('9H 7E 7H 9H 9H')  # full_house
# ha = hand('9H 7E 7H 7H 9H')  # full_house
# ha = hand('9H 3H 7H AH AH')  # flush
# ha = hand('6H 4H 3H 4E 4H')  # three
# ha = hand('4H 6H 3H 4E 4H')  # three
# ha = hand('4H 6H 3H 4E 3H')  # two pairs
# ha = hand('4H 6H 7H AE 3H')  # pair


# ha.RoyalFlush()
# ha.StraightFlush()
# ha.four_of_a_Kind()
# ha.full_house()
# ha.flush()
# ha.straight()
# ha.three()
# ha.two_pairs()
# ha.pair()
# ha.high()
# print(ha.rank)
# print(ha.card)


player1 = 0

with open('poke.txt', 'rt') as file:
    line = file.readline().rstrip()
    while line:
        if ''.join(hand(line[:14]).rank)>''.join(hand(line[15:]).rank):
            player1+=1
            #print(file.line)
        line = file.readline().rstrip()
print (player1)    
