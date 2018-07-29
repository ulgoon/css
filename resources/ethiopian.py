#define the process of halve, double, even
def halve(x):
    return x // 2

def double(x):
    return x * 2

def even(x):
    return not x % 2

print("=================================")
print("    Ethiopian Multiplication     ")
print("=================================")

#userinput of numberset
numberset = [int(item) for item in input("enter two numbers with space(ex. 12 5): ").split()]

#main function
def ethiopian(first, second):
    result = 0
    while first >= 1:
        if even(first):
            print("%4d %7d struck" % (first, second))

        else:
            print("%4d %7d keep" % (first, second))
            result += second

        first = halve(first)
        second = double(second)
    
    print("The result is {}".format(result))

#run ethiopian multiplication
ethiopian(numberset[0], numberset[1])
