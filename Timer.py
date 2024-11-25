from time import sleep
timer = int(input("What time would you like to set? "))
for x in range(timer, 0, -1):
    print(x)
    sleep(1)
    if x == 0:
        break
print("Times Up!")
