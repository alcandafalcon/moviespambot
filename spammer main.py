import time
import pyautogui

while True:
    user_input = input("Which movie would you like to spam with? Type in the number. 1. Bee Movie, 2. Shrek 3. Shrek 2: ").lower().strip()
    try: 
        user_input = int(user_input)
        if user_input != int:
            break
    except:
        print("Invalid input, please type in the number for the movie you want!")
        continue 

movie_dict = { 1: "beemovie.txt", 2: "shrek.txt", 3: "shrek2.txt"}

fh = open(movie_dict[user_input], "r")

print("Ok, quickly put your cursor in some input box!")
time.sleep(10)
for word in fh: 
    pyautogui.typewrite(word)
    pyautogui.press("enter")

    
