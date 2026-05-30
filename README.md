# Diceware Password Generator

A kind of accurate Python CLI tool that generates Diceware style passphrases and estimates their security in terms of entropy and estimated cracking cost against different hashing algorithms.

---

## Features

- Generate Diceware passphrases (2 modes)
  - Original Diceware wordlist (7776 words)
  - Diceware v6 wordlist (46656 words), [credit](https://github.com/mandulaj/diceware-v6)
- Adjustable password length
- Password strength estimation based on entropy
- Estimated brute-force cracking cost:
  - Fast hash (MD5)
  - Slow hash (Argon2id
- Includes fake progress bar

---

## How It Works

The password is generated using simulated dice rolls(using secrets lib so truly random, not pseudo-random like random lib) to select words from a wordlist.  
Each word adds entropy, making the final passphrase more secure.

Entropy is estimated as:

- ~12.92 bits per word (7776-word list)
- ~15.51 bits per word (46656-word list)

```python
time = ((2**(entropy-1)) / hash_rate) * 3600
cost_crack = time * 1.5 * 0.157
