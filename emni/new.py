import sys

def is_lower_character(c):
    return 'a' <= c <= 'z'

def main():
    words = set()

    for line in sys.stdin:
        current = ''
        for char in line:
            c = char.lower()
            if is_lower_character(c):
                current += c
            elif current != '':
                words.add(current)
                current = ''
        if current != '':
            words.add(current)

    for word in sorted(words):
        print(word)

main()
