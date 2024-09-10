animals = ["dog", "cat", "rabbit", "snake", "rat", "fish", "lizard", "ferret", "bird"]
for animal in animals:
    print(f"A {animal} would make a great pet.")

print("Any of these animals would make a great pet.")

print("The first three items in the list are:")
for animal in animals[:3]:
    print(animal)

print("The next three items in the list are:")
for animal in animals[3:6]:
    print(animal)

print("The last three items in the list are:")
for animal in animals[6:9]:
    print(animal)