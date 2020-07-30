# The teams and/or players Involved
class Teams(object):
    team_score = 0
    team_rolls = []
    def __init__(self, team_name):

        self.team_name = team_name

    def description(self):
        print(f'The {self.team_name} has a score of {self.team_score} points')
