from random import randint
import matplotlib.pyplot as plt
import numpy as np

random_int1 = 0
random_int2 = 0
run = 0
e_total_guesses = 0
s_total_guesses = 0
e_guesses_in_one_run = 0
s_guesses_in_one_run = 0
e_guess_list = []
s_guess_list = []
e_guesses_for_comp = 0
s_guesses_for_comp = 0
e_smaller = 0
s_smaller = 0
while run <= 9999:
    while random_int1 + random_int2 != 19:
        random_int1 = 0 + randint(0, 13)
        random_int2 = 0 + randint(0, 13)
        if random_int1 + random_int2 == 19:
            print(random_int1 + random_int2)
            print('wow that is edems age')
            e_guess_list.append(e_guesses_in_one_run)
        else:
            print(random_int1 + random_int2)
            print('try again')
            e_total_guesses += 1
            e_guesses_in_one_run += 1
    while random_int1 + random_int2 != 21:
        random_int1 = 0 + randint(2, 13)
        random_int2 = 0 + randint(2, 13)
        if random_int1 + random_int2 == 21:
            print(random_int1 + random_int2)
            print('wow that is setors age')
            s_guess_list.append(s_guesses_in_one_run)
        else:
            print(random_int1 + random_int2)
            print('try again')
            s_total_guesses += 1
            s_guesses_in_one_run += 1
    run += 1
    if e_guesses_in_one_run < s_guesses_in_one_run:
        e_smaller += 1
    if s_guesses_in_one_run < e_guesses_in_one_run:
        s_smaller += 1
    else:
        pass

    e_guesses_in_one_run = 0
    s_guesses_in_one_run = 0

    print()

print(f'edem less guesses {e_smaller} / {run}')
print(f'setor less guesses {s_smaller} / {run}')
print()
print(f'list for edem guesses = {e_guess_list}')
print(f'average tries edem = {sum(e_guess_list) / len(e_guess_list)}')
print()
print(f'list for setor guesses = {s_guess_list}')
print(f'average tries setor = {sum(s_guess_list) / len(s_guess_list)}')
print(sum(np.array(s_guess_list) - np.array(e_guess_list) > 0))
