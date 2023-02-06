import random
trials = 0
avg = 0
total = 0
while(trials < 1000):
    rolls = 0
    counter = 0
    while True:
        counter = counter + 1
        rolls = random.randint(1, 6)
        rolls += 1
        if rolls == 6:
            print ("It took ", counter , " times before you rolled a 6")
            total = (total + counter)
            avg =  (total) / 1000
            break
        print(counter)
    

    trials += 1

print("The total was", total)
print("The average of all rolls was", avg)