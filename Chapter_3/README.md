## EX 3-1
```
friends = ['Kristi', 'Dima', 'Vadik', 'Sasha', 'Nastia']
print(friends[0])
print(friends[1])
print(friends[-3])
print(friends[-2])
print(friends[-1])
```
>Kristi

>Dima

>Vadik

>Sasha

>Nastia

# EX 3-2
```
friends = ['Kristi', 'Dima', 'Vadik', 'Sasha', 'Nastia']
message = "My friend's name is " + friends[0] + "."
print(message)

message = "My friend's name is " + friends[1] + "."
print(message)

message = "My friend's name is " + friends[2] + "."
print(message)

message = "My friend's name is " + friends[-3] + "."
print(message)

message = "My friend's name is " + friends[-2] + "."
print(message)

message = "My friend's name is " + friends[-1] + "."
print(message)
```
>My friend's name is Kristi.

>My friend's name is Dima. 

>My friend's name is Vadik.

>My friend's name is Vadik.

>My friend's name is Sasha.

>My friend's name is Nastia.

# EX 3-3
```
food = ['shaurma', 'barbecue', 'steak', 'burger']
message = "I would like to eat " + food[0] + "."
print(message)

message = "I would like to eat " + food[1] + ", " + food[2] + " and " + food[3] + "."
print(message)
```
>I would like to eat shaurma.

>I would like to eat barbecue, steak and burger.

# EX 3-4
```
visitors = ['Vadik', 'Sveta', 'Kristi']
message = visitors[0] + ", please, visit my lunch. See you!"
print(message)

message = visitors[1] + ", please, visit my lunch. See you!"
print(message)

message = visitors[2] + ", please, visit my lunch. See you!"
print(message)
```
>Vadik, please, visit my lunch. See you!

>Sveta, please, visit my lunch. See you!

>Kristi, please, visit my lunch. See you!

# EX 3-5
```
visitors = ['Vadik', 'Sveta', 'Kristi']
print(visitors[0])

visitors[0] = 'Dima'
print(visitors)

message = visitors[0] + ", please visit my lunch!"
print(message)

message = visitors[1] + ", please visit my lunch!"
print(message)

message = visitors[2] + ", please visit my lunch!"
print(message)
```
>Vadik

>['Dima', 'Sveta', 'Kristi']

>Dima, please visit my lunch!

>Sveta, please visit my lunch!

>Kristi, please visit my lunch!

# EX 3-6
```
visitors = ['Vadik', 'Sveta', 'Kristi']
message = visitors[0] + ", " + visitors[1] + ", " + visitors[2] + ", our guest list will be expanded! See you!"
print(message)

visitors.insert(0, 'Dima')
visitors.insert(2, 'Nastia')
visitors.append('Sasha')

message = visitors[0] + ", please visit my lunch!"
print(message)

message = visitors[1] + ", please visit my lunch!"
print(message)

message = visitors[2] + ", please visit my lunch!"
print(message)

message = visitors[3] + ", please visit my lunch!"
print(message)

message = visitors[4] + ", please visit my lunch!"
print(message)

message = visitors[5] + ", please visit my lunch!"
print(message)
```
>Vadik, Sveta, Kristi, our guest list will be expanded! See you!

>Dima, please visit my lunch!

>Vadik, please visit my lunch!

>Nastia, please visit my lunch!

>Sveta, please visit my lunch!

>Kristi, please visit my lunch!

>Sasha, please visit my lunch!

# EX 3-7
```
visitors = ['Vadik', 'Sveta', 'Kristi']
visitors.insert(0, 'Dima')
visitors.insert(2, 'Nastia')
visitors.append('Sasha')

message = "Dear guests, only two people can visit my lunch, I'm sorry :("
print(message)

minus_1 = visitors.pop()
message = minus_1 + ", I'm sorry I need to cancel your invitation."
print(message)

minus_2 = visitors.pop()
message = minus_2 + ", I'm sorry I need to cancel your invitation."
print(message)

minus_3 = visitors.pop()
message = minus_3 + ", I'm sorry I need to cancel your invitation."
print(message)

minus_4 = visitors.pop()
message = minus_4 + ", I'm sorry I need to cancel your invitation."
print(message)

message = visitors[0] + ", your invitation is in force, see you!"
print(message)

message = visitors[1] + ", your invitation is in force, see you!"
print(message)

del visitors[0]
del visitors[0]
print(visitors)
```
>Dear guests, only two people can visit my lunch, I'm sorry :(

>Sasha, I'm sorry I need to cancel your invitation.

>Kristi, I'm sorry I need to cancel your invitation.

>Sveta, I'm sorry I need to cancel your invitation.

>Nastia, I'm sorry I need to cancel your invitation.

>Dima, your invitation is in force, see you!

>Vadik, your invitation is in force, see you!

>[]

# EX 3-8
```
countries = ['Ukraine', 'Great Britain', 'Poland', 'Germany', 'Ireland']
print(countries)

print(sorted(countries))

print(countries)

print(sorted(countries, reverse=True))

print(countries)

countries.reverse()

print(countries)

countries.reverse()

print(countries)

countries.sort()

print(countries)

countries.sort(reverse=True)

print(countries)
```
>['Ukraine', 'Great Britain', 'Poland', 'Germany', 'Ireland']

>['Germany', 'Great Britain', 'Ireland', 'Poland', 'Ukraine']

>['Ukraine', 'Great Britain', 'Poland', 'Germany', 'Ireland']

>['Ukraine', 'Poland', 'Ireland', 'Great Britain', 'Germany']

>['Ukraine', 'Great Britain', 'Poland', 'Germany', 'Ireland']

>['Ireland', 'Germany', 'Poland', 'Great Britain', 'Ukraine']

>['Ukraine', 'Great Britain', 'Poland', 'Germany', 'Ireland']

>['Germany', 'Great Britain', 'Ireland', 'Poland', 'Ukraine']

>['Ukraine', 'Poland', 'Ireland', 'Great Britain', 'Germany']

# EX 3-9
```
visitors = ['Vadik', 'Sveta', 'Kristi']

visitors.insert(0, 'Dima')

visitors.insert(2, 'Nastia')

visitors.append('Sasha')

print(len(visitors))
```
>6

# EX 3-10
```
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
```
>['dog', 'cat', 'mouse', 'lion', 'crocodile']

>crocodile

>lion

>['cat', 'mouse', 'humster', 'lion', 'crocodile', 'tiger']

>['cat', 'mouse', 'humster', 'lion', 'crocodile']

>['cat', 'crocodile', 'humster', 'lion', 'mouse']

>['mouse', 'lion', 'humster', 'crocodile', 'cat']

>['crocodile', 'lion', 'humster', 'mouse', 'cat']

>['cat', 'crocodile', 'humster', 'lion', 'mouse']

>['mouse', 'lion', 'humster', 'crocodile', 'cat']

# EX 3-11
```
motorcycles = [] 
print(motorcycles[-1])
```
Traceback (most recent call last):

  File "f:\PYTHON_CRASH_COURSE_2022\Chapter_3\chapter_3.py", line 2, in <module>
    print(motorcycles[-1])
    
IndexError: list index out of range