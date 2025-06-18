# while roop

"""
A program that calculates 5! with loop and stores its result in
redBox when it terminates
"""
redBox = 1 # used to store the result of 5!
blueBox = 1 # used as a loop variable
while blueBox < 5 or blueBox == 5:
    """
    The two assignments are done while blueBox
    is less than or equal to 5.
    """
    redBox = redBox * blueBox # Store the product in redBox
    blueBox = blueBox + 1 # Increment the loop var
print('redBox: ' + str(redBox))
print('blueBox: ' + str(blueBox))


# Variables and assignments

myName = 'Yuta Suanagawa'
myAge = 24
myStudentNo = 2510096
print('My name is ' + myName + '.')
print('I am ' + str(myAge) + ' years old.')
print('My student number is ' + str(myStudentNo) + '.')


# for (loop) statements ver 1

s = 'JAIST'
r = ''
for c in s:
    r = c + r
print('The reverse of ' + s + ' is ' + r + '.')


# for (loop) statements ver 2

s = 'JAIST'
r = ''
for c in s:
    r = c + r
    print('The reverse of ' + s + ' is ' + r + '.')


# if (conditional) statements

v0 = 100
for i in range(v0):
    if i * i > v0:
        v1 = i - 1
        break
print('sr(', v0, ') = ', v1)


# if (conditional) statements

v0 = 100
v1 = 0
v2 = v0
while v1 != v2:
    if (v2-v1)%2 == 0:
        v3 = v1+(v2-v1)//2
    else:
        v3 = v1+(v2-v1)//2+1
    if v3*v3 > v0:
        v2 = v3-1
    else:
        v1 = v3
print('sr(', v0, ') = ', v1)


# if (conditional) statements

v0 = 20000000000000000
v1 = 0
#count = 0
for i in range(v0):
    if i * i > v0:
        v1 = i - 1
        break
    #count += 1
print('sr(', v0, ') = ', v1)
#print("count:", count)


# if (conditional) statements

v0 = 20000000000000000
v1 = 0
v2 = v0

#count = 0
while v1 != v2:
    if (v2-v1)%2 == 0:
        v3 = v1+(v2-v1)//2
        #print("flag1")
        #print("v3", v3)
    else:
        v3 = v1+(v2-v1)//2+1
        #print("flag2")
        #print("v3", v3)
    if v3*v3 > v0:
        v2 = v3-1
        #print("flag3")
        #print("v3", v3)
        #print("v2", v2)
    else:
        v1 = v3
        #print("flag4")
        #print("v3", v3)
        #print("v1", v1)
    #count += 1
    #print("count:", count)
print('sr(', v0, ') = ', v1)