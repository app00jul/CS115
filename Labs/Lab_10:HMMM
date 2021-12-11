# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Julian Noeske
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
0   read r1
1   read r2
2   sub r3 r1 r2
3   jeqzn r3 6
4   jgtzn r3 8
5   jltzn r3 10
6   write r3
7   halt
8   write r1
9   halt
10  write r2
11  halt
"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 >= 0
Power = """
00 read r1
01 read r2
02 setn r3 1
03 setn r6 1
04 nop
05 jeqzn r2 11
06 mul r6 r6 r1
07 sub r2 r2 r3
08 jgtzn r2 04
09 write r6
10 halt
11 write r3
12 halt
"""

# Fibonacci
#  Write a hmmm function that gets one number,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 >= 0
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 read r1
01 setn r2 0
02 setn r3 1
03 sub r4 r1 r3
04 setn r5 1
05 jgtzn r4 7
06 jeqzn r4 12
07 add r6 r2 r3
08 copy r2 r3
09 copy r3 r6
10 sub r4 r4 r5
11 jumpn 5
12 write r6
13 halt
"""



# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Fibonacci  # Change to the function you want to run
doDebug = True # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


