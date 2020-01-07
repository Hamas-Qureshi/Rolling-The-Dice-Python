import random #to generate random numbers
def roll_dice():
    min = 1
    max = 6
    roll_again = 'yes'
    while roll_again.strip() == 'yes' or roll_again.strip() == 'y':
        print ('Rolling the dices...')
        print ('Here it comes ....')
        print (random.randint(1,6)) #assuming there are two players
        print (random.randint(1,6))
        roll_again = input('Roll the dices again? ')

if __name__ == "__main__":
    roll_dice()
