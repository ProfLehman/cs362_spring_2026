# MinesKnowlegeModel_Lehman.py
# prof. lehman
# spring 2024 (updated class examples spring 2026)
# CS 262 AI and Machine Learning
#
# Knowledge model to determine mine locations
# and locations to open
#
# Code iterates through knowlege model simpifying model
# by identifying mines, and spaces that are clear to open
# progam iterates until no further knowledge can be derived
#
# Project idea based on project description from
#   https://cs50.harvard.edu/ai/2024/projects/1/minesweeper/
#
# Code written by hand (no AI) except for lookup for how to
# convert lists to sets
#
# Knowledge model uses Python dictionary
# storing list of cells and count
# - one entry for each number (unless there are duplicates)
# - cells must be listed in alphabetical order
#

# knowledge model
km = {}


# Sample Board and Knowlege Model
# (show your sample board in same format)
# 
# abcd
# 1121
#

km["a,b"] = 1
km["a,b,c"] = 1
km["b,c,d"] = 2
km["c,d"] = 1


# -------------------------------------------------------

# Handout Example - board 1 of 2

# ab1
# c21
# d1
# e1

"""
km["b"] = 1
km["a,b,c,d"] = 2
km["c,d,e"] = 1
km["d,e"] = 1
"""

# mines: ['b']
# open:  ['c']
#   km:  {'a,d': 1, 'd,e': 1}

# Handout Example - board 2 of 2

# ab1
# 221
# c1
# d1
"""
km["b"] = 1
km["a,b"] = 2
km["a,b,c"] = 2
km["c,d"] = 1
"""
# mines:  ['a', 'b']
# open:  ['c']
#   km:  {}


# Handout Example - board 2 of 2 - Alternate

# if since we learned the position of a previous
# mine, we can mark the mine and reduce the numbers
# around the mine
# 
# am0
# 110
# b1 
# c1
"""
km["b,c"] = 1
km["a,b"] = 2
"""
# mines:  ['a', 'b']
# open:  ['c']
#   km:  {}
   
# -------------------------------------------------------
# Class Example 12 February 2026 - board 1 of 2

# abcd
# 112e
#   1f
#   1g

"""
km["a,b"] = 1
km["a,b,c"] = 1
km["b,c,d,e,f"] = 2
km["e,f,g"] = 1
km["f,g"] = 1
"""


# Class Example 12 February 2026 - board 2 of 2

# ab1c
# 1121
#   1d
#   1e
"""
km["a,b"] = 1
km["d,e"] = 1
km["b,c,d"] = 2
km["c,d"] = 1
km["b,c"] = 1
"""

mines = []
clear = []

print( "--- start ---" )
print( "mines: ", mines )
print( " open: ", clear )
print( "   km: ", km )
print()

changes = True
round = 1

while changes == True:
   
    print(f"--- round: {round} ---")
    
    changes = False
    
    new_mines = []
    new_clear = []
    new_km = {}
          
    # process all items in knowledge model
    for key, value in km.items():
               
        # get key and convert to list
        temp = key.split(",")
        
        # not a mine, can open spot
        if value == 0:    
            for i in temp:
                new_clear.append( i )
            changes = True
        
        # is a mine
        elif len(temp) == value:
            for i in temp:
                new_mines.append( i )
            changes = True
            
        else:
            # not a mine or open spot
            
            # remove mines
            for m in mines:
                if m in temp:
                    temp.remove(m)
                    changes = True
                    value = value - 1
            
            # remove values not mines
            for c in clear:
                if c in temp:
                    temp.remove(c)
                    changes = True
            
            # if update adjust key
            if changes == True:
                new_key = ""
                for i in temp:
                    new_key = new_key+str(i) + ","
                key = new_key[:-1] #remove last ,
             
            # save sentence
            if len(key) > 0:
                new_km[key] = value
               
    # check for subsets in knowledge model
    for key1, value1 in km.items():
        for key2, value2 in km.items():
            if key1 != key2:
                s1 = set(key1.split(","))
                s2 = set(key2.split(","))
                
                if s1.issubset(s2):
                    changes = True
                    new_set = s2 - s1
                    new_list = list(new_set)
                    new_list.sort()
                    new_key = ""
                    for i in new_list:
                        new_key = new_key+str(i) + ","
                    new_key = new_key[:-1]
                    new_value = value2 - value1
                    new_km[ new_key ] = new_value
                    #print( f"{s2} - {s1}  {new_key} => {new_value}" )
                    
    # update mines list
    for m in new_mines:
        if m not in mines:
            mines.append(m)
            
    # update clear list
    for c in new_clear:
        if c not in clear:
            clear.append(c)
    
    # update km
    km = new_km
    
    round = round + 1
    
    #loop
  
    # indented to see how knowledge model changes each round
    # undent this section to limit output to final answer
    print()
    print( "mines: ", mines )
    print( " open: ", clear )
    print( "   km: ", km )
    print()


