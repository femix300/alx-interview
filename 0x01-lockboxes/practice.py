'''
get the first set of available keys
put them in a set
I won't add a key that is higher than the length of boxes or a duplicate key
loop through the other boxes to get more keys
I'll have i and curr_key
i will be 0
curr_key will be setofkeys[i] so that I can loop through my set of keys
and get more keys by doing boxes[setofkeys[i]]
although I'll have to loop through setOfkeys[i] so that i can add all they keys in the inner list
''' 

def canUnlockAll(boxes):
    if len(boxes) <= 1:
        return True

    available_keys = []
    temp_collection = []
    needed_keys = []

    for i in range(len(boxes)):
        needed_keys.append(i+1)
    
    needed_keys.pop()
    print(needed_keys)


    for key in boxes[0]:
        if key not in available_keys and key <= (len(boxes) - 1):
            available_keys.append(key)
    
    i = 0
    count = 0
    curr_key = available_keys[i]

    while count < (len(boxes) - 1):
        for key in boxes[curr_key]:
            if key not in available_keys and key <= (len(boxes) - 1) and key > 0:
                available_keys.append(key)
            if key > (len(boxes) - 1):
                temp_collection.append(key)
        i+=1
        if i <= (len(available_keys) - 1):

            curr_key = available_keys[i]
        
        count += 1

        print('What available keys looks like: ', available_keys)
        
    
    contents = [element for sublist in boxes for element in sublist]

    contents = set(contents)
    needed_keys = set(needed_keys)

    collected_contents = set(available_keys)

    if 0 in collected_contents:
        collected_contents.remove(0)
    
    print(collected_contents)
    print(needed_keys)


    if collected_contents == needed_keys:
        return True
    return False


    print(curr_key)
    print((len(available_keys) - 1))
    print(available_keys)






'''
[ [0, 4, 1], [3]]
'''




boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

