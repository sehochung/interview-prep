'''
In your school, two lines of students are formed A and B, with each line having exactly N students. 
The two lines of students will face each other. 
The Physical Education teacher wants the heights of all students standing across from each other to be equal. 
To do this, students may be swapped from one line to another. 
Any student in one line can be swapped with any student in the other line. 
Each swap counts as one operation, and each operation costs the minimum height in the swap. 
Reordering the students within one line has no cost. 
Determine the minimal cost to achieve the desired result. 
If it is impossible, return -1.


Example
arrA = [4, 2, 2, 2]
arrB = [1, 4, 1, 2]

If the arrays are sorted descending, then arrA = [4, 2, 2, 2] and arrB = [4, 2, 1, 1]. 
Swap a 2 in arrA with a 1 in arrB for a cost of min(1, 2) = 1. 
This is the only swap that must occur, so the answer is 1.

Function description
Complete the function rearrangeStudents. 

The function has the following parameters:
int arrA[n] #the heights of the children in line A
int arrB[n] #the heights of the children in line B

Returns
long, the minimal cost to rearrange the students or -1

Constraints
1 <= n <= 2 x 10^5
1 <= arrA[i], arrB[i] <= 10^9

'''

def rearrange_students(arrA, arrB):
    N = len(arrA)
    
    freqA = { arrA[i]: 0 for i in range(N) }
    freqB = { arrB[i]: 0 for i in range(N) }
    
    for i in range(N):
        freqA[arrA[i]]+=1
        freqB[arrB[i]]+=1

    c = {i : freqA.get(i,0) + freqB.get(i,0) for i in set(freqA).union(freqB)}   
    c1 = []
    c2 = []
    for k,v in c.items():

        if v % 2 != 0:
            return -1
        freqAc = freqA.get(k,0)
        freqBc = freqB.get(k,0)

        if freqAc == freqBc:
            continue
        if freqAc > freqBc:
            for i in range((freqAc - freqBc) // 2):
                c1.append(k)
        else:
            for i in range((freqBc - freqAc) // 2):
                c2.append(k)
    c1 = sorted(c1)
    c2 = sorted(c2, reverse=True)
    ans = 0
    min_v = min (arrA+arrB)
    for v1,v2 in zip(c1,c2):
        ans += min(v1, v2, min_v*2)
    return ans

print(rearrange_students([4, 6, 2, 1],[6, 4, 1, 2]))