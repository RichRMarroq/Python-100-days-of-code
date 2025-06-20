import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item) #the append was done after the for loop.
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

#Assuming the issue is b_list is not the same length as a_list
