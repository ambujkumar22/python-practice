animal = "lion"
guess_num = 0
out_of_guess = 3
guess = ""
out = False

while guess != animal and not(out):
    if guess_num < out_of_guess:
        guess = input("Enter an animal which has 4 legs: ")
        guess_num += 1
    else:
        out = True
if out:
    print("you've lost!")
else:
    print("you won!")