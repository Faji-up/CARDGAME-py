class Player:
    def __init__(self,name,playerNumber,card_1,card_2):
        self.points = 30
        self.card_1 = card_1
        self.card_2 = card_2
        self.name = name

    def get_name(self):
        return self.name
    def get_card_one(self):
        return self.card_1

    def get_card_two(self):
        return self.card_2

    def add_points(self,point):
        self.points += point

    def deduc_points(self,point):
        self.points -= point
    def player_points(self):
        return self.points