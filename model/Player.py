class Player:
    def __init__(
        self,
        name="",
        score_point=0,
        lifes=3,
        account=0,
        temp_point=0
    ):
        self.name = name
        self.score_point = score_point
        self.lifes = lifes
        self.account = account
        self.temp_point = temp_point

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_lifes(self):
        return self.lifes

    def get_temp_point(self):
        return self.temp_point

    def add_point(self):
        self.score_point += self.temp_point

    def remove_point(self):
        self.score_point -= self.temp_point

    def remove_lifes(self):
        self.lifes -= 1

    def add_temp_point(self):
        self.temp_point += 1

    def to_print(self):
        print("Player: " ,self.name)
        print("Score point: ", self.score_point)
        print("{Player} have {Lifes}".format(Player=self.name, Lifes=self.lifes))