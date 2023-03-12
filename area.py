def area_of_square(n1):
    result = n1*n1
    return result


a = int(input("enter 1: "))
area_of_square(a)
result = area_of_square(a)
print(result)


def area_of_rectangle(n1, n2):
    result = n1*n2
    return result


b = int(input("enter 1: "))
c = int(input("enter 1: "))
area_of_rectangle(b, c)
result = area_of_rectangle(b, c)
print(result)


def area_of_circle(n1, n2):
    result = n1*(n2*n2)
    return result

#
d = int(input("enter pi "))
e = int(input("enter radius "))
area_of_circle(d, e)
result = area_of_circle(d, e)
print(result)
