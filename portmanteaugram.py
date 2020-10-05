def getalpha(prompt: str) -> str:
    while True:
        string = input(prompt)
        if not string.isalpha(): print("Invalid input. Please only enter English letters.")
        else: break
    return string

name = getalpha("Please enter your name: ").lower()
other = getalpha("Please enter another word: ").lower()

vowels = ['a', 'e', 'i', 'o', 'u']
port = ""
manteau = ""

for i in range(len(name) - 2, -1, -1):
    if name[i] in vowels:
        port = name[:i + 1]
        break
if port == "": port = name
        
for i in range(1, len(other) - 1):
    if other[i] in vowels:
        manteau = other[i + 1:]
        break
if manteau == "": manteau = other

print((port + manteau).capitalize())