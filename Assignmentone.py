class Team:
    def __init__(self, name, year, city):
        self.name = name
        self.year = year
        self.city = city
        self.wins = 0
        self.losses = 0

    def __str__(self):
        return "{} {}: {} wins, {} losses".format(self.year, self.name, self.wins, self.losses)

    def wonGame(self):
        self.wins += 1

    def lostGame(self):
        self.losses += 1

    def getWinPercent(self):
        if self.wins == 0:
            return 0
        else:
            return self.wins / (self.wins + self.losses) * 100

Class=Team("Arsenal", "2018", "London")
print(Class)
Class.wonGame()
print(Class)
Class.lostGame()
print(Class)
print(Class.getWinPercent())
