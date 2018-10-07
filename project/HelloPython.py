#!/usr/bin/env/ python 3.6
def in_fridge():
    """This is the fun Doc"""
    try:
        count = fridge[wanted_food];
    except KeyError:
        count = 0;
    return count;

fridge = {"apple":10, "orange":3, "milk":2};

wanted_food = "apple";
print(in_fridge());

wanted_food = "milk";
print(in_fridge());

print(in_fridge.__doc__)

print(len(fridge));

class Fridge :
    """This is the object of Fridge"""

f = Fridge();





