"""
    Date: 11/11/2022
    File: pass_gen.py
    Author: Rajjya Rohan Paudyal
    Description: Testing out a new idea of creating my own password generator
"""
import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
symbols = "!@#$%^&*()_+-{}[]|\/?><"
all_mix = uppercase_letters + lowercase_letters + symbols
pw_length = 10

password = "".join(random.sample(all_mix, pw_length))
print("Generated Password of length",  pw_length, "=", password)
