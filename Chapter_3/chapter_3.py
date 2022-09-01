animals = ['dog', 'cat', 'mouse', 'lion', 'crocodile']
print(animals)

print(animals[-1])

print(animals[3])

animals.insert(3, 'humster')

animals.append('tiger')

del animals[0]
print(animals)

animals.pop()
print(animals)

print(sorted(animals))

print(sorted(animals, reverse=True))

animals.reverse()
print(animals)

animals.sort()
print(animals)

animals.sort(reverse=True)
print(animals)