import statistics
s = [102, 37, 92, 222, 221]

def find_max(a):
    n = len(a)
    max_s = a[0]
    for i in range(1, n):
        if a[i] > max_s:
            max_s = a[i]
    return max_s

 

def find_min(a):
    n = len(a)
    min_s = a[0]
    for i in range(1, n):
        if a[i] < min_s:
            min_s = a[i]
    return min_s

sum_s = sum(s)
ave = statistics.mean(s)

print('최댓값은 ')
print(find_max(s))

print(' ')

print('최솟값은 ')
print(find_min(s))

print(' ')

print('합계는 ')
print(sum_s)

print(' ')
print('평균값은 ')
print(f'{ave}')
