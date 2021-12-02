a={1,2.4,3,4,5,6}
b={'kawser','ahmed','kazol'}
c={'abc',5,9}

print(a)
print(b)
print(c)
print("after remove method perform")
#we use remove method for removing specific element 

a.remove(6)
b.remove('kazol')
c.remove(5)


print(a)
print(b)
print(c)

print("After perform discard method")

a.discard(1)
b.discard("kamrul") #It will execute although it has no the string 
c.discard(9)

print(a)
print(b)
print(c)

print("After pop operation we will get")

a.pop() #this operation will remove first operation from the set

print(a)
print(b)
print(c)
