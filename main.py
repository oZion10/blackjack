import random, os
from collections import Counter
os.system("cls")
running = True


def get_points(cards):
    points = 0
    if type(cards) == str: cards = [cards] # This is to fix any potential bugs for when the amount of cards is 1
    
    for card in cards:
        if not card[:-1].isnumeric():
            if card[:-1] != "A": points += 10 # If card is either 10, J, Q or K

        else: points += int(card[:-1]) # If card is numeric

        if card[:-1] == "A": # If card is Ace
            if points + 11 <= 21: points += 11
            else: points += 1
    
    return points

def find_pair(mylist):
    return [el for el, n in Counter(item[:-1] for item in mylist).items() if n > 1]



class Player():
    def __init__(self):
        self.cards = []
        self.cards_split = []
        self.split_mode = False
        self.money = 0
        self.bet = 0
    
    def place_bet(self):
        while True:
            try:
                self.money = int(input("How much money do you have? $"))
                if self.money <= 4: print("You don't have enough money to play!")
                else: break
            except:
                print("Incorrect money amount!")
        
        while True:
            try:
                self.bet = int(input("Place bet (MIN:$5): $"))
                if self.bet <= 4: print("Incorrect betting amount!")
                elif self.money < self.bet: print("You don't have that much money available to bet!")
                else: break
            except:
                print("Incorrect betting amount!")
        
        self.money -= self.bet

    def decide(self):
        while True:
            self.decision = input("Would you like to [H]it, [S]tand, [D]ouble down or s[P]lit? ").lower()
            if self.split_mode:
                while True:
                    try:
                        print("Hand 1:", self.cards*)
                        self.hand = int(input("or hand 1:", self.cards_split* + "? "))
                        if self.hand in range(1, 3):
                            break
                        else:
                            print("Incorrect hand!")
                    except ValueError:
                        print("Incorrect hand!")
            if self.decision == "h":
                self.hit(self.hand)
                break
            
            elif self.decision == "s":
                self.stand(self.hand)
                break
            
            elif self.decision == "d":
                if self.money - self.bet*2 > 0:
                    self.double(self.hand)
                    break
                else:
                    print("You don't have enough money to double!")

            elif self.decision == "p":
                if get_points(self.cards[0]) == get_points(self.cards[1]):
                    if self.money - self.bet*2 > 0:
                        self.split(self.hand)
                        break
                    else:
                        print("You don't have enough money to split!")
                else:
                    print("You can only split when your cards are of the same value!")

            else:
                print(f"Invalid choice, try again!")
        
    def hit(self):
        self.cards.append(cards.deck.pop(random.randint(0, len(cards.deck)-1)))
        print(f"Card obtained: {self.cards[-1]}")
        print("Your cards:", *player.cards, f"| Points: {get_points(player.cards)} | Dealer: {dealer.cards[0]} ??\n")

    def stand(self):
        print(f"You: stand!")

    def double(self):
        self.bet *= 2
        self.cards.append(cards.deck.pop(random.randint(0, len(cards.deck)-1)))
        print(f"You: double down!")

    def split(self): # TODO
        self.bet *= 2
        self.split_mode = True
        self.cards_split.append(self.cards.pop[1])
        self.cards_split.append(cards.deck.pop(random.randint(0, len(cards.deck)-1)))
        self.cards.append(cards.deck.pop(random.randint(0, len(cards.deck)-1)))
        print(f"You: split!")
        pass

    def state(self):
        if get_points(self.cards) > 21:
            print("*** You busted! ***")
            print(f"Balance  : ${self.money}")
            print(f"You lost : ${self.bet}")
            gameover()

        elif get_points(self.cards) == 21 and get_points(dealer.cards) != 21: # Blackjack for player
            print("*** You got blackjack! ***")
            self.money += self.bet*1.5
            print(f"Reward : ${round(self.bet*1.5, 2)}")
            print(f"Balance  : ${self.money}")
            gameover()

        elif get_points(dealer.cards) == 21 and get_points(self.cards) != 21: # Blackjack for dealer
            print("*** The dealer has blackjack! ***")
            print(f"You lost : ${self.bet}")
            print(f"Balance  : ${self.money}")
            gameover()
        
        elif get_points(dealer.cards) == get_points(self.cards) and get_points(self.cards) in range(17, 22): # Push
            print("*** Push! (dealer and you) ***")
            print(f"Balance  : ${self.money}")
            gameover()
        
        else:
            for bot in bots:
                if get_points(bot.cards) == get_points(self.cards) and get_points(bot.cards) == 21:
                    print(f"*** Push! (You and bot {bot.num})***")


class Bot():
    def __init__(self, bet, num):
        self.cards = []
        self.bet = bet
        self.num = num
        self.strategy = { # https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/b/Blackjack.htm
            "hard_totals":[
                ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"], #            0
                ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"], #            1
                ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"], #            2
                ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"], #            3
                ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"], #            4
                ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"], #            5
                ["D", "D", "D", "D", "D", "D", "D", "D", "D", "H"], #            6
                ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"], #            7
                ["H", "D", "D", "D", "D", "H", "HH", "H", "H", "H"], #           8
                ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"] #             9
            ],
            "soft_totals":[
                ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"], #            0
                ["S", "S", "S", "S", "D", "S", "S", "S", "S", "S"], #            1
                ["D", "D", "D", "D", "D", "S", "S", "H", "H", "H"], #            2
                ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"], #            3
                ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"], #            4
                ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"] #             5
            ],
            "pairs":[
                ["SP", "SP", "SP", "SP", "SP", "SP", "SP", "SP", "SP", "SP"], #  0
                ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"], #            1
                ["SP", "SP", "SP", "SP", "SP", "S", "SP", "SP", "S", "S"], #     2
                ["SP", "SP", "SP", "SP", "SP", "SP", "SP", "SP", "SP", "SP"], #  3
                ["SP", "SP", "SP", "SP", "SP", "SP", "H", "H", "H", "H"], #      4
                ["SP", "SP", "SP", "SP", "SP", "H", "H", "H", "H", "H"], #       5
                ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"], #            6
                ["H", "H", "H", "SP", "SP", "H", "H", "H", "H", "H"], #          7
                ["SP", "SP", "SP", "SP", "SP", "SP", "H", "H", "H", "H"] #       8
            ],
            "hard_totals_hand":[
                [18, 19, 20], # 0
                [17], #         1
                [16], #         2
                [15], #         3
                [13, 14], #     4
                [12], #         5
                [11], #         6
                [10], #         7
                [9], #          8
                [5, 6, 7, 8] #  9
            ],
            "soft_totals_hand":[
                [20], #         0
                [19], #         1
                [18], #         2
                [17], #         3
                [15, 16], #     4
                [13, 14] #      5
            ],
            "pairs_hand":[
                ["A"], #        0
                ["10"], #       1
                ["9"], #        2
                ["8"], #        3
                ["7"], #        4
                ["6"], #        5
                ["5"], #        6
                ["4"], #        7
                ["3", "2"] #    8
            ]
        }
        self.choice = ""

    def decide(self):
        # Getting self.choice
        if [card[:-1] for card in self.cards].count("A") == 1: # Soft totals
            for i, row in enumerate(self.strategy["soft_totals_hand"]):
                if get_points(self.cards) in row:
                    self.choice = self.strategy["soft_totals"][i][get_points(dealer.cards[0])-2]
        else:        
            for i, row in enumerate(self.strategy["pairs_hand"]): # Pairs
                if find_pair(self.cards) in row:
                    self.choice = self.strategy["pairs"][i][get_points(dealer.cards[0])-2]
            
            for i, row in enumerate(self.strategy["hard_totals_hand"]): # Hard totals
                if get_points(self.cards) in row:
                    self.choice = self.strategy["hard_totals"][i][get_points(dealer.cards[0])-2]

        print(f"bot {self.num}: {self.choice}")

        if self.choice == "S":
            self.stand()
        elif self.choice == "H":
            self.hit()
        elif self.choice == "D":
            self.double()
        elif self.choice == "SP":
            self.split()

    def hit(self):
        self.cards.append(cards.deck.pop(random.randint(0, len(cards.deck)-1)))
        print(f"bot {self.num}(${self.bet}): hit!")

    def stand(self):
        print(f"bot {self.num}(${self.bet}): stand!")

    def double(self):
        self.bet *= 2
        self.cards.append(cards.deck.pop(random.randint(0, len(cards.deck)-1)))
        print(f"bot {self.num}(${self.bet}): double down!")

    def split(self): # TODO
        print(f"bot {self.num}: split!")
        pass
    
    def state(self):
        if get_points(self.cards) > 21:
            print(f"*** bot {self.num} busted! ***")
            gameover()

        elif get_points(self.cards) == 21 and get_points(dealer.cards) != 21: # Blackjack for self
            print(f"*** bot {self.num} got blackjack! ***")
            gameover()

        elif get_points(dealer.cards) == 21 and get_points(self.cards) != 21: # Blackjack for dealer
            print("*** The dealer has blackjack! ***")
            print(f"You lost : ${self.bet}")
            print(f"Balance  : ${self.money}")
            gameover()
        
        elif get_points(dealer.cards) == get_points(self.cards) and get_points(self.cards) in range(17, 22): # Push
            print(f"*** Push! (dealer and bot {self.num})***")
            gameover()
        
        else:
            for bot in bots:
                if get_points(bot.cards) == get_points(bots[self.num].cards) and get_points(bot.cards) == 21:
                    print(f"*** Push! (bot {bot.num} and bot {self.num})***")
            
                elif get_points(bot.cards) == get_points(player.cards) and get_points(bot.cards) == 21:
                        print(f"*** Push! (You and bot {self.num})***")
        

while True:
    try:
        bot_amount = int(input("How many bots do you want? (1-6): "))
        if bot_amount not in range(1, 7): print("Incorrect bot amount!")
        else: break
    except:
        print("Incorrect bot amount!")

bots = [Bot(random.randint(5, 100), num) for num in range(1, bot_amount+1)] # Create bots



class Dealer():
    def __init__(self):
        self.cards = []
    
    def deal(self):
        for _ in range(2):
            for bot in bots:
                bot.cards.append(cards.deck.pop(random.randint(0, len(cards.deck)-1)))
            player.cards.append(cards.deck.pop(random.randint(0, len(cards.deck)-1)))
            self.cards.append(cards.deck.pop(random.randint(0, len(cards.deck)-1)))
    
    def reveal(self):
        pass

    def decide(self):
        pass
    


class Cards():
    def __init__(self):
        self.types = ["clubs", "diamonds", "hearts", "spades"]
        self.types_icons = ["♣", "♦", "♥", "♠"]
        self.cards = {
            "A" : "Ace",
            "2" : "2",
            "3" : "3",
            "4" : "4",
            "5" : "5",
            "6" : "6",
            "7" : "7",
            "8" : "8",
            "9" : "9",
            "10": "10",
            "J" : "Jack",
            "Q" : "Queen",
            "K" : "King",
        }
        self.deck = []
        
    def generate_deck(self):
        for card in self.cards:
            for icon in self.types_icons:
                self.deck.append(card+icon)
        
        random.shuffle(self.deck)
    
    def get_name(self, card):
        if card[:2] == "10":
            return f"10 of {card[2:]}"
        else:
            if card[:1] not in ["A", "J", "Q", "K"]:
                return f"{card[:1]} of {card[1:]}"
            else:
                if card[:1] == "A":
                    return f"Ace of {card[1:]}"
                if card[:1] == "J":
                    return f"Jack of {card[1:]}"
                if card[:1] == "Q":
                    return f"Queen of {card[1:]}"
                if card[:1] == "K":
                    return f"King of {card[1:]}"



def gameover():
    for i, bot in enumerate(bots):
        print(f"Bot {i}:       ", *bot.cards)
    print("Dealer cards:", *dealer.cards)

cards = Cards()
cards.generate_deck()
player = Player()
player.place_bet()
dealer = Dealer()
dealer.deal()



print("Cards dealt:", *player.cards, f"| Points: {get_points(player.cards)} | Dealer: {dealer.cards[0]} ??")


player.decide()
for bot in bots:
    # print("bot", bot.cards)
    bot.decide()

dealer.reveal()
dealer.decide()
player.state()
for bot in bots:
    bot.state()