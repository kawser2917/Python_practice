def func1(*mylist):
    for num in mylist:
        print(num)

print("This is first parametter:")
func1(10,20,30)

print("This is second parameter:")
func1(10,12)

print("This is Third parameter:")
func1(5,15,25,35,45,55,65,75,85,95)