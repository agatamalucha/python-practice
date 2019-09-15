
a=0
b=2
while a < 4:
    print ("=====")
    a +=1
    b -=1
    try:
        a/b
    except ZeroDivisionError:
        print ("{0}, {1} - division by 0".format (a,b))
        continue
    finally:
        print("{0}, {1} - always execute".format (a,b))

    print("{0}, {1} - main loop".format (a,b))





i = 5
while i <5:
    print (i)
    i +=1

min_lenght = 2
name= input("Please enter your name:")

while not(len(name) >= min_lenght and name.isprintable() and name.isalpha()):
        name= input("Please enter your name:")

print ("hello, {0}".format(name))

# how to break infinite loop, if requirement is true that is when loop is stopped
min_lenght = 2

while True:
    name = input("Please enter your name:")
    if (len(name) >= min_lenght and name.isprintable() and name.isalpha()):
        break

print ("hello, {0}".format(name))

#continue loop is

a= 0

while a <10:
    a +=1
    if a % 2 == 0:
        continue
    print (a)

l = [1,2,3]
val =10


# try ....except....finally

a= 10
b=1
try:
    a/b
except ZeroDivisionError:
    print('division by 0')

finally:
    print('this always executes')
