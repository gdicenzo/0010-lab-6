name = input("Please enter your name: ")
other = input("Please enter another word: ")

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(len(name) - 2, -1, -1):
    if name[i] in vowels:
        port = name[:i + 1]
        break

for i in range(1, len(other) - 1):
    if other[i] in vowels:
        manteau = other[i + 1:]
        break

print(port + manteau)