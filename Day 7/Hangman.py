import random
words = [
    "apple", "banana", "grape", "orange", "mango",
    "table", "chair", "window", "door", "pencil",
    "river", "mountain", "ocean", "desert", "forest",
    "cat", "dog", "tiger", "lion", "elephant",
    "car", "train", "plane", "bus", "bicycle",
    "computer", "keyboard", "mouse", "phone", "camera"
]
a=random.choice(words)
print(a)
for i in range (len(a)):
    print("_",end=" ")
print("")
while len(a)!=0:
    guess=input("Guess a letter:").lower()
    for i in a:
        if i==guess:
            print(i,end=" ")
        else:
            print("_",end=" ")
    print("")