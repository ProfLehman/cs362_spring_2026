#        file: testLogic.py
#        date: 
#        name:
# description: sample logic using Harvard's logic class
#

from logic import *

a = Symbol("a")
b = Symbol("b")
c = Symbol("c")


knowledge = And(
    Implication( a, b ),
    Implication( b, c ),
    a
)

print()
print( knowledge.formula() )
print()
print(model_check(knowledge, c)) 





