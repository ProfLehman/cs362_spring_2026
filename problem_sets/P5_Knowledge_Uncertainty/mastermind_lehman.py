#        file: mastermind_lehman.py
#        name: prof. lehman
# description: sample logic using Harvard's logic class
#              to solve simplfied version of master mind
#              game with three choices of red, green, or blue
#              for each choice.
#

from logic import *

# function to run model check after each guess
def check_knowledge():
    count = 0
    for symbol in symbols:
        print(symbol, model_check(knowledge, symbol))
        count = count + 1
        if count == 3:
            print()
            count = 0
    print("-----------------")


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

# start with And so that we can add to knowledge
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


#          1 2 3
#    start R R G
# we guess G B R    0 correct position, 2 colors
check_knowledge()

# since 
knowledge.add(And(Not(green1)))
knowledge.add(And(Not(blue2)))
knowledge.add(And(Not(red3)))
              
knowledge.add(And(Or(blue1, red1)))
knowledge.add(And(Or(green2, red2)))
knowledge.add(And(Or(green3, blue3)))

check_knowledge()

# next guess
#          1 2 3
#    start R R G
# we guess G B R    0 correct position, 2 colors
# we guess B R G    2 correct position, 2 colors

knowledge.add(
    And(
    Or(blue1, red2, Not(green3)),
    Or(blue1, Not(red2), green3),
    Or(Not(blue1), red2, green3)
    ))
    
check_knowledge()                

# next guess
#          1 2 3
#    start R R G
# we guess G B R    0 correct position, 2 colors
# we guess B R G    2 correct position, 2 colors
# we guess R G R    2 correct position, 3 colors

knowledge.add(
    Or(
    And(red1, green2, red3),
    And(green1, red2, red3),
    And(red1, red2, green3)))

check_knowledge()                



