'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106

'''
import collections
def bus_routes(routes,source, target):
    # create a defaultdict with empty list as its default value
    stop_to_buses = collections.defaultdict(list)
    # enumerate through routes, where route is the index of routes and stops is the list of stops for that index
    for route, stops in enumerate(routes):
        # iterate through list of stops
        for stop in stops:
            # add each stop as a key to the defaultdict and add the route the stop is a part of to its list
            stop_to_buses[stop].append(route)
    # check if source or target exists in the dict
    # 
    if source == target:
        return 0
    if source not in stop_to_buses or target not in stop_to_buses:
        return -1

    queue = collections.deque([])
    stops_visited = set()
    buses_taken = set()
    answer = 0

    queue.append(source)

    while queue:
        answer+=1
        stops_to_process = len(queue)         
        for _ in range(stops_to_process):
            stop = queue.popleft()
            # Check buses passing through the current stop
            for bus_id in stop_to_buses[stop]:
                if bus_id in buses_taken:
                    continue
                buses_taken.add(bus_id) 

                # Check stops reachable from the current bus
                for next_stop in routes[bus_id]:
                    if next_stop in stops_visited:
                        continue
                    # If the target is reached, return the answer
                    if next_stop == target:
                        return answer
                        
                    queue.append(next_stop)
                    stops_visited.add(next_stop)
                    
    return -1   

a = [[1,2,7],[3,6,7],[2,6,8]]
b = 1
c = 6

print(bus_routes(a,b,c))
