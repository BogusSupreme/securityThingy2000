import os
import stat
import hashlib

password = input("Enter a password: ")

special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"

spec = False
noUpper = False
repeatChar = False
short = False

index = 0
score = 0

if len(password) < 8:
    short = True
for char in password:
    if char in special_chars:
        spec = True
    if not char.isupper():
        noUpper = True
    if index > 0:
        if password[index] == password[index-1]:
            repeatChar = True
    index += 1

if short:
    print("Your password should be at least 8 characters long.")
    score += 1
if repeatChar:
    print("You should avoid using the same character twice in a row or more.")
    score += 1
if not spec:
    print("You should add some special characters into your password.")
    score += 1
if not noUpper:
    print("You should try to have at least 1 captialized letter.")
    score += 1

print("\n||| OVERALL ASSESMENT |||")
match score:
    case 0:
        print("Your password is strong. Good Work!\n")
    case 1:
        print("Your password is moderately strong.\n")
    case 2:
        print("Your password is a little weak\n")
    case 3:
        print("Your password is weak.\n")
    case 4:
        print("Your password is vey weak.\n")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\n||| PASSWORD HASH |||")
print(hashed_password,"\n")

def check_world_writable(path):
    print('Security scanner running...')

    if not os.path.exists(path):
        print(f"{path} does not exist.")
        return

    file_stat = os.stat(path)
    if file_stat.st_mode & stat.S_IWOTH:
        print(f"{path} is world-writable. Maybe change that?")
    else:
        print(f"{path} permissions look safe.")

files_to_check = []

while True:
    newInput = input("\nIs there a file you want to check for security issues? (Y/N)").strip().lower()

    if newInput == 'n':
        break

    if newInput == 'y':
        fpInput = input("\nGive the path of a file you want to check for security issues: ")
        files_to_check.append(fpInput)
        print("\n Keep adding files until you are done...")
    else:
        print("\nI am assuming this means no.")
        break

for file in files_to_check:
    check_world_writable(file)