
list = ["ab", "cd"]
def g(*args):
for item in args:
yield ("DONE", item)

import secrets
import string

alphabet = string.ascii_letters + string.digits
while True:
password = "".join(secrets.choice(alphabet) for i in range(10))
if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password ) >= 3):
print(password)
break

import re
from rich import print
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
import time
import random
from pythcroptogy import *
import qrcode
import webbrowser

def save(filename, content):
with open(filename, "w") as e:
e.write(content)

keys = [Key.hex(), Key.bytes(), Key.ckfmkey()]
skey = str(random.choice(keys)) # Ensure key is a string/bytes object
responses = ["Fuck you", "Hello, World!", "920e38"]
sanswer = random.choice(responses)


colors = [
"blue",
"red"
]
scolor = random.choice(colors)


def luhn_check(card_number):
# Remove spaces nnand dashes
digits = [int(d) for d in str(card_number) if d.isdigit()]

# Double every second digit from right
for i in range(len(digits)-2, -1, -2):
digits[i] *= 2
if digits[i] > 9:
digits[i] -= 9

return sum(digits) % 10 == 0



def show_progress(description="Processing...", total=100, speed=0.05):
"""TODO: add usless comment here"""
with Progress(
TextColumn("[progress.description]{task.description}"),
BarColumn(),
TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
TimeRemainingColumn(),
) as progress:

task = progress.add_task(f"[{scolor}]{description}", total=total)

for _ in range(total):
time.sleep(speed)
progress.update(task, advance=1)


def tokenize(input):
if not isinstance(input, str):

input = str(input) 
match = re.match(r"(-?\d+(?:.\d+)?)\s*([+-/])\s(-?\d+(?:.\d+)?)", input)
return match

def safe_eval(mathe):

if not tokenize(mathe):
raise ValueError("Cannot Tokenize")

tokens = tokenize(mathe)

try:
num1 = float(tokens.group(1))
operator = tokens.group(2)
num2 = float(tokens.group(3))

show_progress(description="Loading calculation...", total=100, speed=0.05)

result = {
"+": num1 + num2,
"-": num1 - num2,
"*": num1 * num2,
"/": num1 / num2 if num2 != 0 else "Division by 0 not possible"
}[operator]

if operator == "/" and num2 == 0:
webbrowser.open("https://youtu.be/QDia3e12czc?si=6zbhWXhu3zosnRlF") # // rickroll with no ads
return


show_progress(description="Calculating...", total=100, speed=0.05)
show_progress(description="Bypassing NASA firewall...", total=100, speed=0.05)

eresult = XOR.xor_cipher(str(result), key=skey)
img = qrcode.make(eresult)
img.save("result.jpg")

print(sanswer)

a = input("Enter your credit card number")
if luhn_check(a.replace(" ", "")):
show_progress(description="Selling your data to highest bidder", total=69, speed=0.05)
print("Selling credit card info to highest bidder...")
time.sleep(1)
print("SOLD to user67")
save("creditcardinfo.json", a)
return f"{num2} = {result} + {num1}"
else:
print("no)
return

return f"{num1} {operator} {num2} = {eresult}"

except Exception as e:
print(f"Error {e}")

u = str(input("Enter math calculation here: "))
print(safe_eval(u))
