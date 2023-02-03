import random

# Lotto simulator

print("Pick six numbers.")
idx = 0
list_of_numbers = []
while idx < 6:
    num_1 = int(input("Pick a number from 1 to 49: "))
    if 1 <= num_1 <= 49 and num_1 not in list_of_numbers:
        idx += 1
        list_of_numbers.append(num_1)
        list_of_numbers.sort()
    else:
        print("You picked a number that already exist or the number is not 1 - 49!\nTry again")


print(f'Your numbers: {list_of_numbers}')

lotto = random.sample(range(1, 50), 6)
list.sort(lotto)
print(f'Lotto numbers: {lotto}')

hit_numbers = sum(el in lotto for el in list_of_numbers)
if hit_numbers < 3:
    print(f"Sorry, you hit {hit_numbers} correctly.")
else:
    print(f"Congratulations! You hit {hit_numbers} correctly!")
