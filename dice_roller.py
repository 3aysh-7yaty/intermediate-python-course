# main function
import random
from teams import Teams

def main():

    team = Teams(input('Name player 1:'))
    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are th dice? '))
    dice_sum = 0

    for i in range(0, dice_rolls):
        roll = random.randint(1, dice_size)
        dice_sum += roll
        team.team_score += roll
        if (roll == 1):
            print(f'You rolled a {roll}! Critical Fail.')
        elif (roll == dice_size):
            print(f'You rolled a {roll}! Critical Success!.')
        else:
            print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}!')
    team.description()
    input('Press any key to Exit')


if __name__ == "__main__":
    main()
