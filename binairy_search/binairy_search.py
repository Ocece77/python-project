def binary_search(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print(f"This is step n°{steps} :", str(list[start:end+1]))

        steps = steps + 1
        middle = (start + end)// 2

        if target == list[middle]:
            return middle
        
        if target < list[middle]:
            end = middle - 1

        else :
            start = middle +1
    return -1
        



binary_search([1,3,6,9,11,12], 6)