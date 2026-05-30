from tqdm import tqdm
import time
from analyser import analyse
from generator import generate_password

md5 = 10000000000
argon2id = 10000

while True:

    answer1 = input("Enter 1 for original Diceware gen, Enter 2 for Diceware v6(46656 words).")

    if answer1 not in ("1", "2"):
        print("Please enter 1 or 2")
    else:
        break

while True:

    word_count = input("How many words would you like your password to have? The more the stronger the password is.")
    
    try:
        word_count = int(word_count)

        if word_count < 1 or not isinstance(word_count, int):
            print("Please enter a valid number")
        else:
            break

    except ValueError:
        print("Please enter an integer")

pbar = tqdm(total=100)

pbar.set_description("Processing...")

for _ in range(50):
    time.sleep(0.05)
    pbar.update(1)

pbar.set_description("Generating...")

for _ in range(50):
    time.sleep(0.05)
    pbar.update(1)

pbar.close()

password = generate_password(word_count, answer1)
entropy, strength, md5_cost = analyse(word_count, answer1, md5)
_, _, argon2id_cost = analyse(word_count, answer1, argon2id)

md5_cost, argon2id_cost = round(md5_cost, 2), round(argon2id_cost, 2)
print(f"\nYour password is: {password}")
print(f"Entropy(bits): {entropy:.1f}, Strength: {strength}")
print(f"The cost to crack this password for weak hash is ${md5_cost:,.2f}NZD" 
      f" and for strong hash is ${argon2id_cost:,.2f}NZD")