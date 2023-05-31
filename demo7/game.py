import random


def isHit(n, score=10):
    recode = 0
    hit = 0
    for i in range(30):
        r1 = random.randint(1, n)
        r2 = random.randint(1, n)
        if r1 == r2:
            recode += score
            hit += 1
    print('hit:{}'.format(hit))
    return recode


print('------------welcome to the game------------')
gamername = input('Please enter your niko\n')
while True:
    Choice = input('Please make a selection: 1.lol 2.pubg\n')
    if Choice == '1':
        print('{},welcome to LOL'.format(gamername))
        # make your hero
        heros = ['aicy', 'yasuo', 'jincx', 'kuki', 'seen', 'noxsic']
        for h in heros:
            print(h)
        hero = input('Please make your hero')
        # make game's level
        levels = ['EASY', 'NORMAL', 'HARD']
        for l in levels:
            print(l)
        level = input("make game's level")

        # play game
        if level == 'EASY':
            score = isHit(10, 5)
            print(score)
        elif level == 'NORMAL':
            score = isHit(20)
            print(score)
        elif level == 'HARD':
            score = isHit(30, 15)
            print(score)
        else:
            print('this level do not find ')
        print('complete this game')
        break

    elif Choice == '2':
        print('{},welcome to PUBG'.format(gamername))
        print("{},let's fight".format(gamername))
        coins = 0  # coins count
        level = 1  # level
        count = 0  # kills
        while True:
            r = random.randint(1, 20)
            if r % 5 == 0:
                coins += r * level
                count += 1

            if 400 >= coins >= 0:
                level = 1
            elif 1600 >= coins > 400:
                level = 2
            elif 3200 >= coins > 1600:
                level = 3
            else:
                print('complete and you kill {}'.format(count))
                break
        break
    else:
        print('Input error ! Please reenter your input:\n')
