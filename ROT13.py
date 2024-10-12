#!/usr/bin/python3

# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python

# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

# Test examples:

# "EBG13 rknzcyr." -> "ROT13 example."

# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"


from string import ascii_lowercase, ascii_uppercase
from typing import LiteralString


letters_len = len(ascii_lowercase)
letters = dict(zip(ascii_lowercase, range(letters_len)))


def is_lower(letter: str) -> bool:
    return letter == letter.lower()


def find_letter(letter: str, step: int) -> str:

    start = letters[letter.lower()]

    if start + step < letters_len:
        diff = start + step
    else:
        diff = start + step - letters_len
    if is_lower(letter):
        return ascii_lowercase[diff]
    return ascii_uppercase[diff]


def rot13(message: str) -> LiteralString:
    res = []
    step = 13

    for letter in message:
        if letter.isalpha():
            res.append(find_letter(letter, step))
        else:
            res.append(letter)

    return "".join(res)
