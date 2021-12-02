n=10        #global variable
def func1():
    print(n)

def func2():
    n=20   #Local variable 
    print(n)
    func1()
func2()