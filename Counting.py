## Name:Shahmir Alam    

def myCount(L):
    count, sorted_L = count_and_sort(L)
    return count, sorted_L
'''
Todo: Write an algorithm that solves the counting inversion problem.
Input:
List[int] L: a non-empty array of distinct integers
Output:
(inversions, sortedArray): A pair of the following elements in the exact
order:
inversions: number of inversions in L - int
sortedArray: a sorted array containing the elements of L - List[int]
'''

def merge_and_count(left, right):
    merged = []
    count = 0
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return count, merged

def count_and_sort(L):
    if len(L) <= 1:return 0, L
    middle = len(L) // 2
    left_count, left_sorted = count_and_sort(L[:middle])
    right_count, right_sorted = count_and_sort(L[middle:])
    merge_count, merged_sorted = merge_and_count(left_sorted, right_sorted)
    total_count = left_count + right_count + merge_count
    return total_count, merged_sorted

L = [6, 1, -4, 10, 2, 7]
count, sorted_L = myCount(L)
print(count, sorted_L)

def myMinDistance(P):
    P.sort()
    min_dist = min_distance(P)
    return min_dist
    
'''
Todo: Write an algorithm that solves the closest pair of points problem.
Input:
List[Tuple(int, int)] P: an array of Points. Points contain the fields x
and y, with (x, y)
representing a point in the Cartesian plane.
Output:
An int representing the square of the minimum distance between two of the
given points. - int
'''
def euclidean(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def min_distance(P):
    n = len(P)
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                dist = euclidean(P[i], P[j])
                min_dist = min(min_dist, dist)
        return min_dist
    middle = n // 2
    mid_point = P[middle]
    left_min = min_distance(P[:middle])
    right_min = min_distance(P[middle:])
    min_dist = min(left_min, right_min)
    strip = []
    for point in P:
        if abs(point[0] - mid_point[0]) < min_dist:
            strip.append(point)
    strip_min = min_dist
    strip_len = len(strip)
    for i in range(strip_len):
        for j in range(i + 1, min(i + 7, strip_len)):
            dist = euclidean(strip[i], strip[j])
            strip_min = min(strip_min, dist)
    return min(min_dist, strip_min)

P = [(0, 1), (-5, 3), (4, 2), (2, 0)]
print(myMinDistance(P))

