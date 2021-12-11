####################################################################################
# Name: Julian Noeske
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
####################################################################################


# The binary format you'll be working with for this assignment is called R2L,
# as it is a right-to-left representation.
####################################################################################
## Ex: 8 in decimal is 1000 in standard binary (2^3),
## and represented as a list [0, 0, 0, 1] in our R2L representation.
####################################################################################

# Notice that this makes it very easy to work with binary,
# by using num[0] to grab the least significant bit (2^0)!
#
# Please fill out the following 4 functions below using recursion, as specified.

# Given an integer x >= 0, convert it to the R2L binary format.
# Take note that both [] and [0] are used to represent 0 in R2L
def decimalToBinary(x):
   if x == 0:
      result = []
   else:
      result = [x%2] + decimalToBinary(x // 2)
   return result

print(decimalToBinary(8))

# Given an R2L formatted number, return the integer it is equivalent to.
# The function should function with both [] and [0] returning 0.
def binaryToDecimal(num):
   if num == [0] or num == []:
      result = 0
   else:
      result = num[-1]*(2 ** (len(num)-1)) + binaryToDecimal(num[:-1])
   return result


print(binaryToDecimal([1,1,0,1]))


# Given an R2L formatted number, return an R2L equivalent to num + 1
# If you need to increase the length, do so. Again, watch out for 0
def incrementBinary(num):
   if num == [] or num == [0]:
      return [1]
   
   add = num[-1] + 1
   if add > 1:
      num = incrementBinary(num[:-1]) + [0]
   else:
      num[-1] = add
   return num

   
print(incrementBinary([1,1,1,1]))

# Given 2 R2L numbers, return their sum.
## You MUST implement recursively the algorithm for bit-by-bit addition as taught in class,
## you may NOT do something like decimalToBinary( binaryToDecimal(num1) + binaryToDecimal(num2) ).
# Make sure to figure out what to do when num1 and num2 aren't of the same length!
# (and be sure you can add [] and [0])
## Tip: Try this on paper before typing it up
carry = 0

def addBinary(num1, num2):
    global carry

    if num1 == [] or num1 == [0]:
        if num2 == [] or num2 == [0]:
            if carry == 0:
                return []
            elif carry == 1:
                return [1]
        elif num2[-1] == 1:
            if carry == 0:
                return [1]
            elif carry == 1:
                carry = 1
                return addBinary(num1[:-1],num2[:-1]) + [0]
    elif num2 == [] or num2 == [0]:
        if num1 == [] or num1 == [0]:
            if carry == 0:
                return []
            elif carry == 1:
                carry = 1
                return [1]
        elif num1[-1] == 1:
            if carry == 0:
                return [1]
            elif carry == 1:
                carry = 1
                return addBinary(num1[:-1],num2[:-1]) + [0]
    
    sum = num1[-1] + num2[-1]

    if carry == 0:
        if sum == 0:
            carry = 0
            return addBinary(num1[:-1],num2[:-1]) + [0]
        elif sum == 1:
            carry = 0
            return addBinary(num1[:-1],num2[:-1]) + [1]
        elif sum == 2:
            carry = 1
            return addBinary(num1[:-1],num2[:-2]) + [0]
    elif carry == 1:
        if sum == 0:
            carry = 0
            return addBinary(num1[:-1],num2[:-1]) + [1]
        elif sum == 1:
            carry = 1
            return addBinary(num1[:-1],num2[:-1]) + [0]
        elif sum == 2:
            carry = 1
            return addBinary(num1[:-1],num2[:-1]) + [1]
    
                                                                                                            

print(addBinary([1,1,1,1,1],[1,1,1,1]))

