
#Initial variable to track game play
user_play = "y"
start_number = 0
#While we are still playing...
while user_play == "y":
    n = int(input("How many numbers"))
    for i in range(start_number, n + start_number):
        print(i)
    start_number += n
    x = input("Continue the chain (y)es or (n)o?")
    i = n

