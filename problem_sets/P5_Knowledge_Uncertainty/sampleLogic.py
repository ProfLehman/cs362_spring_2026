# file: sampleLogic.py
# date: 
# name:
# description: sample logic using Harvard's logic class
#

#  (A ^ 'B) -> C
#  C -> D
#  A, 'B
#

from logic import *

assignment = Symbol("assignment")
procrastinate = Symbol("procrastinate")
pass_assignment = Symbol("pass_assignment")
pass_course = Symbol("pass_course")

knowledge = And(
    Implication( And(assignment, Not(procrastinate)), pass_assignment ),
    Implication( pass_assignment, pass_course ),
    assignment, Not(procrastinate)
)

# note:  assignment, procrastinate => pass_course is False
# note:  assignment, Not(procrastinate) => pass_course is True

print()
print( knowledge.formula() )
print()
print(model_check(knowledge, pass_course)) 





