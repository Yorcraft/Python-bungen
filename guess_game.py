count_try = 3
secret = 4
count_try2 = count_try
while count_try > 0:
    guess = int(input("Raten Sie eine Zahl zwischen 0 und 9"))
    if guess == secret:
        count_try = 0

    else:
        print("unlucky try again fucker")
        count_try -= 1
        count_try2 -= 1
        print(f'Sie haben noch {count_try} Versuche übrig')

if guess == secret:
    count_try2 = 3 - count_try2
    print("Herzlichen Glückwunsch das war richtig")
    print(f'Du hast nur {count_try2} Versuche gebraucht.')
else:
    print("Keine Versuche übrig Sie ficker")