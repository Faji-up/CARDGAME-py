import random
from Player import Player
class CardGame:
    def __init__(self):
        self.players = []
        self.cards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def main(self):
        numberOfPlayers = int(input("Enter Number of Players : "))

        for player in range(numberOfPlayers):
            card_1 = random.choice(self.cards)
            card_2 = random.choice(self.cards)
            name = input("Player Name: ")
            self.players.append(
                Player(name,player,card_1,card_2)
            )
        self.rumble()
        self.start_game() #start the game

    def start_game(self):
        try:
            for player in self.players:
                if self.check_win():
                    break
                if player.player_points() <= 0:
                    continue
                print("Player: ", player.get_name(), "Remaining points", player.player_points())
                print("Card 1: ", player.get_card_one())
                print("Card 2: ", player.get_card_two())
                playerChoice = input("Player`s Choice ['bet','refuse','higher','lower']: ").lower()
                if playerChoice == "refuse":
                    print("Result : Next player..")
                    continue
                while True:
                    point = int(input("Player`s input point: "))

                    if point <= player.player_points():
                        system = self.cards.index(random.choice(self.cards))
                        print("System draw`s:", self.cards[system])

                        if playerChoice.lower() == "bet":
                            if self.bet(player.get_card_one(), player.get_card_two(), system):
                                player.add_points(point)
                                print("Result: Player Wins and win points will be added to his point")
                                print("+", point)
                                break
                            else:
                                player.deduc_points(point)
                                print("Result: Player Lose points will be deducted to his point")
                                print("-", point)
                                break

                        elif playerChoice.lower() == "refuse":
                            print("Result : Next player..")
                        elif playerChoice.lower() == "higher": 
                            if self.higher(player.get_card_one(), player.get_card_two(), system):
                                print("+", point)
                                print("Result: Player Wins and win points will be added to his point")
                                break
                            else:
                                player.deduc_points(point)
                                print("Result: Player Lose points will be deducted to his point")
                                print("-", point)
                                break
                        elif playerChoice.lower() == "lower":
                            if self.lower(player.get_card_one(), player.get_card_two(), system):
                                player.add_points(point)
                                print("Result: Player Wins and win points will be added to his point")

                                print("+", point)
                                break
                            else:
                                player.deduc_points(point)
                                print("Result: Player Lose points will be deducted to his point")
                                print("-", point)
                                break
                        else:
                            print("Invalid choice")

                    else:
                        print("Invalid! your points is", player.player_points())
            self.rumble()
            self.start_game()  # start new game
        except Exception as e:
            print("*** ", e, "***")
            self.start_game()

    def check_win(self):
        if len(self.players) == 1:
            print("Player : ",self.players[0].get_name(),"Win the game")
            print("Points : ",self.players[0].player_points())
            return True
    def bet(self,card_1,card_2,system):
        lowerCard = self.cards.index(card_1) if self.cards.index(card_1) < self.cards.index(card_2) else self.cards.index(card_2)
        higherCard = self.cards.index(card_2) if self.cards.index(card_2) > self.cards.index(card_1) else self.cards.index(card_1)

        if (lowerCard <= system and higherCard >= system):
            return True
        else:
            return False

    def refuse(self,card_1,card_2,system):
        lowerCard = self.cards.index(card_1) if self.cards.index(card_1) < self.cards.index(
            card_2) else self.cards.index(card_2)
        higherCard = self.cards.index(card_2) if self.cards.index(card_2) > self.cards.index(
            card_1) else self.cards.index(card_1)
        if lowerCard > system or higherCard < system:
            return True
        else:
            return False

    def higher(self,card_1,card_2,system):
        lowerCard = self.cards.index(card_1) if self.cards.index(card_1) < self.cards.index(
            card_2) else self.cards.index(card_2)
        higherCard = self.cards.index(card_2) if self.cards.index(card_2) > self.cards.index(
            card_1) else self.cards.index(card_1)
        if lowerCard < system or higherCard < system:
            return True
        else:
            return False
    def lower(self,card_1,card_2,system):
        lowerCard = self.cards.index(card_1) if self.cards.index(card_1) < self.cards.index(card_2) else self.cards.index(card_2)
        higherCard = self.cards.index(card_2) if self.cards.index(card_2) > self.cards.index(card_1) else self.cards.index(card_1)

        if lowerCard > system or higherCard > system:
            return True
        else:
            return False

    def rumble(self):
        players = []
        while True:
            x = random.choice(self.players)
            if x not in players:
                players.append(x)
            if len(players) == len(self.players):
                break
        self.players = players

if __name__ == "__main__":
    game = CardGame()
    game.main()