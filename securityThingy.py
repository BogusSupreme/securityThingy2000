import os
import stat
import hashlib

userInput = input("Enter a password: ")

special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"

spec = False
noUpper = False
repeatChar = False
short = False

index = 0
score = 0

if len(userInput) < 8:
    short = True
for char in userInput:
    if char in special_chars:
        spec = True
    if not char.isupper():
        noUpper = True
    if index > 0:
        if userInput[index] == userInput[index-1]:
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

hashed_password = hashlib.sha256(userInput.encode()).hexdigest()

print("\n||| PASSWORD HASH |||")
print(hashed_password,"\n")

def check_world_writable(path):
    print('Security scanner running...')

    if not os.path.exists(path):
        print(f"[INFO] {path} does not exist.")
        return

    file_stat = os.stat(path)
    if file_stat.st_mode & stat.S_IWOTH:
        print(f"[WARNING] {path} is world-writable!")
    else:
        print(f"[OK] {path} permissions look safe.")

# Example files to check
files_to_check = [
    "config.txt",
    ".env",
    "settings.json"
]

fpInput = input("Give the path of a file you want to check for security issues: ")
files_to_check.append(fpInput)

for file in files_to_check:
    check_world_writable(file)