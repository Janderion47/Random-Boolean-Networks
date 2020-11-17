# dynamic n Nodes; static 3 Dendrites
# Nodes in this version are able to read themselves
from random import choice, randrange
from time import sleep

# Variables for play
num_nodes = 70
num_dendrites = 17
delay = 0

dict_of_iterations = {} # Creates the master dictionary of the iterations of the program
def create_node(): # Returns a random node
    output = [choice([True, False])]
    for i in range(num_dendrites):
        output.append(randrange(num_nodes))
    return output
def bool_to_bit(bowl: bool): # Input boolean, output 0 or 1, corresponding to the boolean
    if bowl == True:
        return 1
    else:
        return 0
# The following dictionary is the logic that every node follows; this is determined at the beginning of the running of the code
dict_of_logic = {}
for i in range(2**num_dendrites):
    a = str(bin(i)).replace('0b','')
    while len(a) < num_dendrites:
        a = '0' + a
    dict_of_logic[a] = choice([True, False])
print(dict_of_logic)

iteration = 0

set_nodes = []
for i in range(num_nodes):
    set_nodes.append(create_node())
dict_of_iterations[str(iteration)] = set_nodes
print(set_nodes)
iteration +=1
while True:
    prev_iter = dict_of_iterations[str(iteration-1)]
    new_iter = []
    str_result = ''
    for i in prev_iter:
        toggle = 1
        toggle2 = 1
        logic_str = ''
        
        for k in range(num_dendrites):
            eep = prev_iter[i[toggle]][0]
            logic_str += str(bool_to_bit(eep))
            
        to_new_iter = [dict_of_logic[logic_str]]
        for lol in range(num_dendrites):
            to_new_iter.append(i[toggle2])
        new_iter.append(to_new_iter)
        str_result += str(bool_to_bit(dict_of_logic[logic_str]))
    dict_of_iterations[str(iteration)] = new_iter
    #print(str_result)
    print(hex(int(str_result,2)))
    iteration +=1
    sleep(delay)
