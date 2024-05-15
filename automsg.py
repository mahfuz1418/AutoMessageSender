import pyautogui
import time

message = input("Enter your message: ")
msgnumber = int(input("Enter your how much time you want to run: "))
time.sleep(5)


while msgnumber > 0:
    pyautogui.write(message)
    time.sleep(1)  # Additional delay after typing the message
    pyautogui.press('enter')  # Press Enter key to send the message
    msgnumber -= 1

print("All messages sent successfully!")
