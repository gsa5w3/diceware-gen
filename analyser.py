def analyse(word_count, answer1, hash_rate):

    

    if answer1 == "1":
        diceware = True
    else:
        diceware = False

    if diceware:
        entropy = 12.93*word_count
    else:
        entropy = 15.51*word_count
    time = ((2**(entropy-1))/(hash_rate)*3600)
    cost_crack = time * 1.5 * 0.157 #power kw - 1.5, price per kwh - 0.157
    

    strength = ""
    if entropy < 20:
        strength = "Weak as hell"

    elif entropy < 40:
        strength = "Still weak"

    elif entropy < 60:
        strength = "Not bad"

    elif entropy <80:
        strength = "Strong"

    elif entropy < 100:
        strength = "Super strong"

    else:
        strength = "Now you're being silly"
    return entropy, strength, cost_crack


