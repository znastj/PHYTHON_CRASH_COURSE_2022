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


