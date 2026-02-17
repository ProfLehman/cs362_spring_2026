#        file: harryLogic.py
#        date: spring 2026
#        name: prof. lehman
# description: sample logic using Harvard's logic class
#

from logic import *

rain = Symbol("rain") # It is raining
hagrid = Symbol("hagrid") # Harry visits Hagrid
dumbledore = Symbol("dumbledore") # Harry visits Dumbledore

# if it is not raining, Harry will visit Hagrid
# Harry visited Hagrid or Dumbledore but not both


knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print()
print( knowledge.formula() )
print()
print("Is it raining?")
print(model_check(knowledge, rain)) # Is it raining?





