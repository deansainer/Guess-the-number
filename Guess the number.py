from random import randint

count=0
while True:
    randnum = randint(1, 5)
    mynum = int(input('-----------------------------\nPlease type your number (1-5): '))
    count += 1
    amiwinner = False
    if randnum == mynum:
        amiwinner = True
        print(f'Congratulations, you guessed our number!')
        print(f'Your number is: {mynum}\nOur number is: {randnum}')
        break
    else:
        print('Sorry, you didnt guess our number')
    print(f'Your number is: {mynum}\nOur number is: {randnum}')
    if amiwinner == False:
        if (mynum < randnum):
            print(f'Your number was {randnum - mynum} units lower than ours, try again')
        else:
            print(f'Your number was {mynum - randnum} units higher than ours, try again ')
