# *****
# Name     : Julian Noeske
# Pledge   : I pledge my honor that I have abided by the Stevens Honor System.
# *****

class Term:
    '''
    Class to represent a monomial (aka term) k*x^n
    '''
    # TODO
    def __init__(self, k=1, n=0):  # myTerm = Term(...)
        '''
        Term(k, n) creates a new term, representing k*x^n
        '''
        self.coef = k
        self.exp = n
        

    def __str__(self):  # print(myTerm)
        '''
        Return a human-friendly string for this term
        '''
        return str(self.coef) + '*x^' + str(self.exp)

   # TODO
    def __repr__(self):  # eval(myTerm)
        '''
        Return a string representation of the term
        '''
        return f"Monomial: {self.coef}*x^{self.exp}"

   # TODO
    def __eq__(self, other):  # myTerm == other
        '''
        Return True if two terms are equal to each other,
        that is, if they have the same coeffiecient and exponent
        '''
        if self.coef == other.coef and self.exp == other.exp:
            return True
        else:
            return False

    # TODO
    def __call__(self, val):  # myTerm(x)
        '''
        Evaluate the term k*x^n for x=val
        E.g., Term(2,4)(3) = 2*3^4 = 162
        '''
        print(self.coef)
        print(self.exp)
        self.val = val
        ans = self.coef*(self.val**self.exp)
        #print(ans)
        return ans

    # TODO
    def __neg__(self):  # otherTerm = -myTerm
        '''
        Return a new term, with same exponent but opposite coeffient
        '''
        if self.coef > 0:
            self.coef = -self.coef
        elif self.coef < 0:
            self.coef = -self.coef
        return self.coef

    # TODO
    def copy(self):  # myCopy = myTerm.copy()
        '''
        Make a term with the same values as this object
        '''
        copy_object = Term(self.coef,self.exp)
        return copy_object
        

# LinkedPolynomial
# Adapted in java by Antonio Nicolosi from
# https://introcs.cs.princeton.edu/java/92symbolic/LinkedPolynomial.java, (c) 2000-2018
# Adapted to Python by Justin Barish, 2018
# Refactored by Toby Dalton, 2019


class LinkedPolynomial:
    '''
    Class to represent a polynomial c_0 + c_1 x + c_2 x^2 + ... + c_m x^m

    The data is kept as a list of Term's, sorted in (strictly)
    descending order of exponent and with no zero coefficients
    '''

    def __init__(self, polyList=[]):  # myPoly = LinkedPolynomial(...)
        '''
        Create a new LinkedPolynomial
        '''
        self.polyList = polyList.copy()  # deep copy of a list

    # TODO
    def addTerm(self, t):  # myPoly.addterm(Term(coef, exp))
        '''
        Append a given Term to the list for this LinkedPolynomial
        Assume (without checking) that the Term has non-zero coefficient,
        and it comes in the proper spot with respect to exponent order.
        '''
        self.polyList.append(t)

    # myPoly2; myPoly2.createListFromNumber(...)
    # TODO
    def createFromNumbers(self, numList):
        '''
        Create a polynomial given a list of (k, n) tuples
        Assume the list to be in the form [(coef1, exp1), (coef2, exp2)...]
        with exponents in descending order and no 0 coefficients. '''
        for i in range (0, len(numList)):
            t = Term(numList[i][0], numList[i][1])
            self.polyList.append(t)

    # TODO
    def __len__(self):  # len(myPoly)
        ''' Returns the length of the polynomial (number of nonzero term)'''
        return len(self.polyList)

    def __str__(self):  # print(myPoly)
        '''
        Return a string representation of the polynomial
        '''
        if len(self) == 0:
            ans = "0"
        else:
            ans = str(self.polyList[0])
            for i in range(1, len(self)):
                coef = self.polyList[i].coef
                if coef > 0:
                    ans += " + " + str(self.polyList[i])
                elif coef < 0:
                    ans += " " + str(self.polyList[i])
        return ans

    def __add__(self, otherPoly):  # addPoly = myPoly + otherPoly
        '''
        Return a polynomial representing the sum of self and otherPoly 
        Note: If both inputs are properly ordered, so will the outcome be!
        '''
        result = LinkedPolynomial()  # Our sum polynomial
        i = 0  # Tracks where in self we are
        j = 0  # Tracks where in otherPoly we are

        while i < len(self) or j < len(otherPoly):  # Continue until both
            # term lists are exhausted

            if i == len(self):  # self is exhausted: take a term from other
                y = otherPoly.polyList[j]
                result.addTerm(y.copy())
                j += 1
                continue

            if j == len(otherPoly):  # other is exhausted: take a term from self
                x = self.polyList[i]
                result.addTerm(x.copy())
                i += 1
                continue

            # If we get here, there are terms in both lists
            x = self.polyList[i]
            y = otherPoly.polyList[j]

            if x.exp == y.exp:  # Same exponents? Combine!
                coef = x.coef + y.coef
                if (coef != 0):  # Only add if not 0 !
                    result.addTerm(Term(coef, x.exp))
                i += 1
                j += 1
            elif x.exp < y.exp:  # Add only larger exp otherwise
                result.addTerm(y.copy())
                j += 1
            else:
                result.addTerm(x.copy())
                i += 1

        return result

    # TODO
    def __eq__(self, other):  # myPoly == other
        '''
        Check if 2 polynomials are equal.
        Assume that no polynomials have 0-coefficient terms.
        Hint: If two LP are equal, then they will be identical in every way 
        '''
        ans = True
        if len(self.polyList) == len(other.polyList):
            for i in range(len(self)-1):
                if self.polyList[i] != other.polyList[i]:
                    ans = False
                    break
            return ans
        else:
            ans = False
            return ans

    # TODO
    def __call__(self, val):  # myPoly(val)
        '''
        Evaluate self at x=val - should use Term's __call__
        '''
        result = 0
        lst = self.polyList
        add = 0
        for i in range(0,len(lst)):
            add = Term(lst[i].coef,lst[i].exp)
            new_num = add(val)
            result += new_num
        return result


    # TODO
    def __neg__(self):  # negPoly = -myPoly
        '''
        Return a *new* LinkedPolynomial representing -1 * self
        (Do NOT modify self while doing this!!)

        Hint: use Term's __neg__
        '''
        lst = self.polyList
        result = LinkedPolynomial()
        for i in range(0,len(lst)):
            temp = LinkedPolynomial()
            new_var = Term(lst[i].coef,lst[i].exp)
            new_term = -new_var
            temp.addTerm(new_var)
            result += temp
        return result

    # TODO
    def __sub__(self, other):  # subPoly = myPoly - other
        '''
        Return a *new* LinkedPolynomial representing self - other
        (Do NOT modify self or other while doing this!!)

        Hint: use __add__ !
        '''
        other = -other
        result = self + other
        return result

    # Extra Credit (15 pts)
    def __mul__(self, otherPoly):  # mulPoly = myPoly * otherPoly
        '''
        Multiply two polynomials together
        Return a new polynomial, properly ordered,
        without changing self & otherPoly
        Hint: do it on paper first!
        '''
        my = self.polyList
        other = otherPoly.polyList
        result = LinkedPolynomial()
        for i in range(0, len(my)):
            temp = LinkedPolynomial()
            for j in range (0, len(other)):
                temp.addTerm(Term(my[i].coef * other[j].coef, my[i].exp + other[j].exp))
            result += temp
        return result

myPoly = LinkedPolynomial()
myPoly.createFromNumbers([(7,2),(5,1)]) 
print(myPoly)
otherPoly = LinkedPolynomial()
otherPoly.createFromNumbers([(2,2), (-3, 1)])
print(otherPoly)
result =myPoly*otherPoly
print(result)
print(myPoly == otherPoly)
print(myPoly(3)) #2_10|3_21
print(-otherPoly)
print(myPoly+otherPoly)
print(myPoly-otherPoly)
