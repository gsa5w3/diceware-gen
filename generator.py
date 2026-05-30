import secrets #more random than random lib
from pathlib import Path


def generate_password(word_count, answer1):

    BASE_DIR = Path(__file__).parent

    word_list_v6 = {}
    #diceware v6 dict
    with open(BASE_DIR / "word_lists/dicewarev6_list.txt", "r") as f:
        for line in f:
            number, word = line.split()
            word_list_v6[number] = word

    word_list_regular = {}
    #diceware regular dict
    with open(BASE_DIR / "word_lists/eff_large_wordlist.txt", "r") as f:
        for line in f:
            number, word = line.split()
            word_list_regular[number] = word

    words = []

    if answer1 == "1" :
        for i in range(word_count):
            word_num = ""
            for z in range(5):
                
                a= secrets.randbelow(6) + 1
                word_num += str(a)
            words.append(word_list_regular[word_num])

    else:
        for i in range(word_count):
            word_nums = ""
            for z in range(6):
                
                b = secrets.randbelow(6) + 1
                word_nums += str(b)
            words.append(word_list_v6[word_nums])

    password = "-".join(words)
    return password
