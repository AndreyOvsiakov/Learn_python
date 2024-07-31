# https://codechick.io/challenges/320


def count_vowels(txt):
    vowels: str = 'aeiou'

    total: int = 0
    for let in txt:
        if let.lower() in vowels:
            total += 1

    return total
