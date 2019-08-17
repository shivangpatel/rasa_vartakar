import json
from itertools import combinations


def findMaxLength(lst):
    maxList = max(lst, key=lambda i: len(i))
    maxLength = len(maxList)

    # return maxList, maxLength
    return maxLength

count = 0
# Now read the file back into a Python list object
with open('test.txt', 'r') as f:
    a = json.loads(f.read())
    output = sum([list(map(list, combinations(a, i))) for i in range(len(a) + 1)], [])
    maxLengthListSize = findMaxLength(output)

    with open('story.md', 'a') as sfile:
        for item in output:
            item_output = sum([list(map(list, combinations(item, i))) for i in range(len(item) + 1)], [])
            if 1 < len(item) < maxLengthListSize:
                for listI in item_output:
                    if len(listI) > 1:
                        sfile.write("\n\n## It's a new conversation..." + str(count))
                        count += 1
                        for listII in listI:
                            sfile.write(listII.replace('*', '\n* ').replace('-', '\n    - '))
            elif len(item) == maxLengthListSize:
                for listI in item_output:
                    if len(listI) > 1:
                        sfile.write("\n\n## It's a new conversation..." + str(count))
                        count += 1
                        for listII in listI:
                            sfile.write(listII.replace('*', '\n* ').replace('-', '\n    - '))
                        sfile.write("\n    - action_restart")
