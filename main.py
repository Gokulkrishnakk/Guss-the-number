from time import sleep
num=8
print('Hey user, i have a number between 1 and 10')
sleep(1)
n1=int(input('guess the number:'))
sleep(1)
if n1==num:
    print('Oh my God. its correct. You are the luckiest person on Earth')
else:
    print('its wrong')
    sleep(1)
    print('Dont worry i will help you. I will give you some hints')
    sleep(2)
    print('its and Even number. ')
    sleep(2)
    n2=int(input('Now guess the number:'))
    if n2==num:
        print('Oh my God. it correct. You are amazing')
    else:
        print('No its not')
        sleep(2)
        print('Dont worry i will help you')
        sleep(2)
        print('its a multiple of 2')
        sleep(5)
        n3=int(input('Now guess it:'))
        sleep(1)
        if n3==num:
            print('Thats correct. You are a genious')
        else:
            print('Noooooooooooo')
            sleep(1)
            print("Don't worry i will give some more clues")
            sleep(1)
            print('its related to driving test')
            sleep(1)
            n4=int(input('Now guess it:'))
            sleep(1)
            if n4==num:
                print('Thats correct. Finally you got it')
            else:
                print('Its wroooooooooonggggggg')
                sleep(1)
                print('You have no brain')
                sleep(1)
                print('Just get lost')