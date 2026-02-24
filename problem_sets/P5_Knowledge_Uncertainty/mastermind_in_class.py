#        file: mastermind_in_class.py
#        name: prof. lehman
# description: sample logic using Harvard's logic class
#              to solve simplfied version of master mind
#              game with three choices of red, green, or blue
#              for each choice.
#

from logic import *

# function to run model check after each guess
def check_knowledge(msg):
    print("+-----------------------+")
    print( msg )
    print("+-----------------------+")
    count = 0
    for symbol in symbols:
        print(symbol, model_check(knowledge, symbol))
        count = count + 1
        if count == 3:
            print()
            count = 0
    print()


# choice 1 to 3 is either red, green, or blue
red1 = Symbol("red1")
green1 = Symbol("green1")
blue1 = Symbol("blue1")

red2 = Symbol("red2")
green2 = Symbol("green2")
blue2 = Symbol("blue2")

red3 = Symbol("red3")
green3 = Symbol("green3")
blue3 = Symbol("blue3")

symbols = [red1, green1, blue1,
           red2, green2, blue2,
           red3, green3, blue3 ]

# start with And so that we can add to
knowledge = And()


# starting knowledge
# red, green, or blue will be selected for 1, 2, 3
knowledge.add(
    And( Or(red1, green1, blue1),
         Or(red2, green2, blue2),
         Or(red3, green3, blue3) ) )

print()
print( knowledge.formula() )
print()
check_knowledge("starting ...")


# G B B  2 correct position, 2 correct colors
knowledge.add( And(
    Or(
    And(green1, blue2, Not(blue3)),
    And(Not(green1), blue2, blue3),
    And(green1, Not(blue2), blue3))))    
        
    
check_knowledge("Guess #1: G B B")


# G R B  1 correct position, 2 correct colors
# know one is the correct position, so
# must have one of three possibilities
knowledge.add( And(
               Or(
               And(green1,Not(red2),Not(blue3)),
               And(Not(green1),red2,Not(blue3)),
               And(Not(green1),Not(red2),blue3))))

check_knowledge("Guess #2: G R B") # infer that choice 2 is blue


# G B R  2 correct position, 2 correct colors
# we know 2 is blue
# thus we have to options
knowledge.add( And(
    Or(
        And(green1,blue2,Not(red3)),
        And(Not(green1),blue2,red3))))
    
check_knowledge("Guess #3: G B R")


# G B B  2 correct position, 3 correct colors
# we know 2 is blue
# we know we have the three colors
# thus we know 1 is blue and 3 is green
knowledge.add( And(blue1, green3) )

check_knowledge("Guess #4: G B B")

# Answer is G B G




