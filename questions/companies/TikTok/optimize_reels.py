'''
Problem Description:
A content creator is taking on a challenge to get really good at TikTok. 
Instead of regular activities, they decide to focus on a playlist of n TikTok reels. 
To master TikTok, they set a goal to watch the reels a total of m times. 
But they want to do this in the least amount of time possible. 

Here's how it works:
First Time Watching 
The creator must watch each reel in the playlist completely the first time. 
The time it takes is initialWatch[i] + repeatWatch[i] for the i-th reel.

Sequential Viewing
When watching the playlist for the first time, they must watch the reels in order, from the first to the last.

Rewatching
After the first complete watch, they can rewatch any reel in any order. 
For rewatching, they only spend repeatWatch[i] minutes per reel.

Total Viewings
The total number of viewings (including first-time and rewatching) across all reels must add up to m.

Optimization Goal
The creator aims to minimize the total time spent watching the reels while fulfilling the above constraints. 
This involves strategically planning which reels to repeat and how often, given the reduced time for repeat viewings.

Function Description:
Complete the function optimizeTikTokWatchTime in the editor below.

optimizeTikTokWatchTime has the following parameter(s):
int m: an integer denoting the total number of reel viewings the creator aims to complete.
int initialWatch[n]: an integer array denoting the minutes to watch the i-th reel for the first time.
int repeatWatch[n]: an integer array denoting the minutes to rewatch the i-th reel.

Returns:
int: an integer denoting the minimum total minutes required for the creator to reach their target (m) count of reel viewings.

Example:
Input:
m = 4
initialWatch = [1, 5, 9, 11]
repeatWatch = [2, 7, 10, 11]

Output:
9

Explanation:
One of the optimal strategies can be:
The creator watches the 0-th reel. As they are watching it for the first time, 
the time taken is initialWatch[0] + repeatWatch[0] = 1 + 2 = 3 minutes.
The creator then rewatches the 0-th reel 3 times. So, the time taken is repeatWatch[0] * 3 = 2 * 3 = 6 minutes.
Thus, the total time taken is 3 + 6 = 9 minutes.


Constraints:
1 <= n <= 10^5
1 <= m <= 10^9
1 <= initialWatch[i], repeatWatch[i] <= 10^9

Sample Input 0:
m = 5
initialWatch = [6, 8, 9]
repeatWatch = [4, 2, 10]

Sample Output 0:
26

Explanation 0:
One of the optimal strategies is:

The creator watches the 0-th reel. Since it’s the first time watching, the time taken is:
initialWatch[0] + repeatWatch[0] = 6 + 4 = 10 minutes.


The learner watches the 1st video. As he is watching it for the first time, the time taken is:
firstWatch[1] + repeatWatch[1] = 8 + 2 = 10 minutes.


The learner then rewatches the 1st video 3 times. So, the time taken is:
repeatWatch[1] * 3 = 2 * 3 = 6 minutes.


Thus, the total time taken is:
10 + 10 + 6 = 26 minutes.
'''

def optimize_tiktok_watch_time(initial_watch, repeat_watch, m):
    n = len(initial_watch)
    min_repeat = float('inf')
    answer = float('inf')
    current = 0
    left = m

    for i in range(n):
        current += initial_watch[i] + repeat_watch[i]
        left -= 1
        min_repeat = min(repeat_watch[i], min_repeat)
        answer = min(current+(left*min_repeat), answer)
    
    return answer

# Test cases
print(optimize_tiktok_watch_time([1, 5, 9, 11], [2, 7, 10, 11], 4))  # Output: 9
print(optimize_tiktok_watch_time([6, 8, 9], [4, 2, 10], 5))      