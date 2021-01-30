from random import randint
import matplotlib.pyplot as plt

h = 0
k = 0
x = 0
y = 0
p = 0
q = 0
r = 0
a = 0
b = 0
lauf = 0
baseline = []
pnumber = 0
qnumber = 0
edemguesses = []
setorguesses = []
while lauf <= 9:
    while x + y != 19:
        x = 0 + randint(0, 13)
        y = 0 + randint(0, 13)
        if x + y == 19:
            print(x + y)
            print('wow that is my age')
            edemguesses.append(p)
            p = 0
        else:
            print(x + y)
            print('try again')
            h += 1
            p += 1
            a = p
    while x + y != 21:
        x = 0 + randint(2, 13)
        y = 0 + randint(2, 13)
        if x + y == 21:
            print(x + y)
            print("wow that is setor's age")
            setorguesses.append(q)
            q = 0
        else:
            print(x + y)
            print('try again')
            k += 1
            q += 1
            b = q
    print()
    w = min(a, b)
    if w == a:
        pnumber += 1
    elif a == b:
        pnumber += 1
        qnumber += 1
    else:
        qnumber += 1
    if h < k:
        print(f'with {h} guesses my age was easier to guess.')
    else:
        print(f"with {k} guesses setor's age was easier to guess. ")
    print()
    print(f'you have guessed both ages correctly!')
    lauf += 1
    baseline.append(lauf)
    print()
    r = k + h
print(f'the program ran {lauf} times and took a total amount of {r} guesses!')
print()
if pnumber > qnumber:
    print(f'my age was (with {pnumber} out of {lauf}) easier to guess on average!')
elif pnumber == qnumber:
    print(f'on average both ages are (with {pnumber} out of {lauf}) equal difficult to guess')
else:
    print(f"setor's age was (with {qnumber} out of {lauf}) easier to guess on average!")
print()
print(f'list for edem guesses = {edemguesses}')
print(f'average tries for correct answer in each round = {sum(edemguesses) / len(edemguesses)}')
eaverage = sum(edemguesses) / len(edemguesses)
print()
print(f'list for setor guesses = {setorguesses}')
print(f'average tries for correct answer in each round = {sum(setorguesses) / len(setorguesses)}')
saverage = sum(setorguesses) / len(setorguesses)
print()
print(baseline)
plt.plot(baseline, edemguesses, setorguesses, )
plt.show()
