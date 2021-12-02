list=[]

print("Enter your values . Press 0 for stop: ")

while True:
    element = int(input())
    list.append(element)
    if element == 0:
        break
print(list)