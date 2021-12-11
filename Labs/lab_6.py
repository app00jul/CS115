####################################################################################
# Name: Julian Noeske
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
####################################################################################
# Lab 6: Recursion 2
# Demonstrate recursion as an algorithm design technique for the problem of 
# computing the (length of the) longest common subsequence of two given strings
#
# Note: Using anything other than recursion will result in a penalty
#####################################################################################

##############################################################################
# Example: The longest common subsequence of "helllowo_rld" and "!helloabcworld!"
# is "helloworld", and it has a length of 10.
#
# Therefore LLCS("helllowo_rld", "!helloabcworld!") returns 10, and
# LCS("helllowo_rld", "!helloabcworld!") returns "helloworld"
##############################################################################

def LLCS(S1, S2):
    if S1 == '' or S2 == '':
        return 0
    elif S1[-1] == S2[-1]:
        return 1 + LLCS(S1[:-1],S2[:-1])
    else:
        return max(LLCS(S1,S2[:-1]), LLCS(S1[:-1],S2))

str_1 = "helllowo_rld"
str_2 = "!helloabcworld!"

print(LLCS(str_1,str_2))

##############################################################################
# Instead of returning the length of the longest common substring, this task
# asks you to return the string itself.
##############################################################################
# Tip: You may find it helpful to copy your solution to LLCS and edit it
# to solve this problem
##############################################################################


def LCS(S1, S2):
    if S1 == '' or S2 == '':
        return ''
    elif S1[0] == S2[0]:
        return S1[0] + LCS(S1[1:],S2[1:])
    else:
        use_it = LCS(S1,S2[1:])
        lose_it = LCS(S1[1:],S2)
        #return max(LCS(S1,S2[1:]), LCS(S1[1:],S2))
        if len(use_it) > len(lose_it):
            return use_it
        else:
            return lose_it

print(LCS(str_1,str_2))
