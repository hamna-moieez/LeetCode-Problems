height = [1,8,6,2,5,4,8,3,7]
# WORKS BUT EXCEEDS TIME LIMIT - DIRTY SOLUTION
max_area = 0
for i in range(len(height)):
    for j in range(i, len(height)):
        width = abs(j-i)
        area = min(height[i], height[j]) * width
        if area > max_area:
            max_area = area
print(max_area)

# BETTER SOLUTION - RUNNING POINTERS
i = 0
j = len(height) - 1
max_area = 0
while True:
    width = abs(j-i)
    area = min(height[i], height[j]) * width
    if area > max_area:
        max_area = area
    if height[i] <= height[j]:
        i += 1
    else:
        j -= 1
    if i == j:
        break
print(max_area)


    