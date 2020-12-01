def two_add(input, target, exclude):
    start = 0
    end = len(input)-1
    while start < end:
        head = input[start]
        tail = input[end]
        if head == exclude: 
            start += 1
            continue
        if tail == exclude:
            end -= 1
            continue
        if head + tail == target:
            return head * tail
        elif head + tail < target:
            start += 1
        else:
            end -= 1
    raise

def three_add(nums, target):
    for num in nums:
        try:
            return num * two_add(nums, target - num, num)
        except:
            continue
        

with open('input.txt') as fp:
    lines = fp.read()
    lines = [int(i) for i in lines.split()]
    lines.sort()
    print(three_add(lines, 2020))