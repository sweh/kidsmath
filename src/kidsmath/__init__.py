import random
import time
import argparse


def new_calc(max=20):
    op = '+' if random.randint(0, 1) else '-'
    if op == '+':
        result = random.randint(4, max)
        x = random.randint(0, result)
        y = result - x
    else:
        x = random.randint(4, max)
        result = random.randint(0, x)
        y = x - result
    check = None
    while check is None:
        check = input(f'{x:2d} {op} {y:2d} = ')
        try:
            check = int(check)
        except Exception:
            check = None

    if int(check) == result:
        print('  RICHTIG \033[92m✓\033[0m')
        return True
    else:
        print(f'  \033[91mFALSCH\033[0m, richtige Antwort: {result}')
        return False


def start_math(name='Robert', max=20, amount=20):
    start_time = time.time()
    x = 1
    right = 0
    wrong = 0

    while x <= amount:
        if new_calc(max):
            right += 1
        else:
            wrong += 1
        print()
        x += 1

    seconds = round(time.time() - start_time)
    if seconds <= 60:
        minutes = 0
    else:
        minutes = int(seconds / 60)
        seconds = seconds - (minutes * 60)

    print('Ergebnis:')
    print(f'        {x-1:3d} Aufgaben gelöst')
    if minutes:
        print(f'     in {minutes:3d} Minuten {seconds:3d} Sekunden')
    else:
        print(f'     in {seconds:3d} Sekunden')
    print(f'  davon \033[92m{right:3d}\033[0m richtig')
    print(f'    und \033[91m{wrong:3d}\033[0m falsch')


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'name',
        help='The kids name.',
    )
    parser.add_argument(
        '--max',
        help='The maximum number the kid can calculate with.',
        type=int,
        default=20
    )
    parser.add_argument(
        '--amount',
        help='The amount of problems the kid should solve.',
        type=int,
        default=10
    )
    arguments = parser.parse_args()

    start_math(name=arguments.name, max=arguments.max, amount=arguments.amount)


if __name__ == '__main__':
    start_math()
