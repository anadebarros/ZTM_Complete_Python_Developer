import random


def guess_number(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                return True
    except TypeError:
        return False
    else:
        print('hey bozo, I said 1~10')
        return False


answer = random.randint(1, 10)

if __name__ == "__main__":
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if guess_number(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue
