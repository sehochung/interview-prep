import collections 
def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adjMap = collections.defaultdict(list)
    # create adjMap of courses and its prereqs
    for course in range(numCourses):
        for prereq in prerequisites:
            if course == prereq[0]:
                adjMap[course].append(prereq[1])
    print(adjMap)

    visited = set()
    cycle = set()

    answer = []

    def dfs(course):
        if course in visited:
            return True
        if course in cycle:
            return False
        print('Before Add-Cycle :', cycle)
        cycle.add(course)
        print('After Add-Cycle :', cycle)
        for prereq in adjMap[course]:
            if not dfs(prereq):
                return False
        
        answer.append(course)
        print('answer appended:',answer)
        visited.add(course)
        
        print('Before remove-Cycle :', cycle)
        cycle.remove(course)
        print('After remove-Cycle :', cycle)
        return True
            
    for i in range(numCourses):
        if not dfs(i):
            return []
    return answer

answer = findOrder(2, [[1,0]])  
print(answer)