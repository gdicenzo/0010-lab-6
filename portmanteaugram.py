name = input("Please enter your name: ")
other = input("Please enter another word: ")

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(len(name) - 2, -1, -1):
    if name[i] in vowels:
        port = name[:i + 1]
        break