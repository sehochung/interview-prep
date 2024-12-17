'''
===TikTok Viral Challenge===
In the competitive world of social media, especially on platforms like TikTok, 
creators are constantly battling to produce viral content. 
The stakes are high-every video segment counts. 
As a data analyst working for TikTok, 
you've been tasked with a critical mission: 
    to help creators optimize their videos by identifying the most 
    promising segments that could lead to viral success.

Each segment of a TikTok video has an engagement attribute, which reflects its potential to go viral. 
This attribute is represented as an integer array engagementArray of size 26, 
corresponding to the letters of the alphabet ('a' to 'z). 
Each element in this array is either "1' (indicating a viral segment) or '0' (indicating a non-viral segment).

The goal is to count all possible viral content combinations. 

A TikTok video is considered viral
if the number of non-viral segments in any substring of the video does not exceed a given threshold k.

The video is represented by a string of length n.

===Given===
A string video of length n.
An integer k, the maximum allowed number of non-viral segments in a viral TikTok video.
An integer array engagementArray of size 26, where each element is either '1' (viral) or '0' (non-viral).
Find the number of unique non-empty substrings of the video that qualify as viral content.

===Input Format for Custom Testing===
Input from stdin will be processed as follows and passed to the function.
The first line contains a string, video,
The next line contains an size 26 engagementArray.
The next line contains an integer, k.

===Function Description===
Complete the function countViralCombinations in the editor below.

countViralCombinations has the following parameter(s):
string video: A string representing the lineup of TikTok segments, 
where each character corresponds to a segment's unique attribute or engagement level.
int engagementArray[n]: 
    An array of integers where each element is either '1' (indicating a viral segment) or 
    '0' (indicating a non-viral segment). 
    This array aligns with the English alphabet; for instance, a corresponds to the first element.
int k: 
    An integer denoting the maximum number of non-viral segments allowed 
    in any content formation to consider it viral.

Returns int: 
    an integer denoting the number of unique content formations 
    that meet the criteria of having no more than k non-viral segments, 
    ensuring each formation is considered viral.

===Constraints===
1 ≤ n ≤ 1500.
1 ≤ k ≤n.
engagementArray[i] € {0, 1}

===Sample case===
stream video = "stream"
engagementArray size = 26
                  [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
engagementArray = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 2
Output = 14
===Explanation===
"s","t","r","e","a","m", - 1 weak (viral), 1 weak (viral), 1 weak (viral), 0 weak (viral), 1 weak (viral), 1 weak (viral)

"st", - 2 weak (viral)
"tr", - 2 weak (viral)
"re", - 1 weak (viral)
"ea", - 1 weak (viral)
"am", - 2 weak (viral)

"str", - 3 weak (not-viral)
"tre", - 2 weak (viral)
"rea", - 2 weak (viral)
"eam", - 2 weak (viral)

"stre", - 3 weak (not-viral)
"trea", - 3 weak (not-viral)
"ream", - 3 weak (not-viral)

"strea", - 4 weak (not-viral)
"tream", - 4 weak (not-viral)

"stream" - 5 weak (not-viral)

===Another test case===
video= "abc"
                  [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
engagementArray = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 2
Output: 5

===Explanation===
"a" - 1 weak player (viral)
"b" - 0 weak player (viral)
"c" - 1 weak player (viral)
"ab" - 1 weak player (viral)
"bc" - 1 weak player (viral)
"abc" - 2 weak player (viral)

===Another test case===
video = "aabc"
                  [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
engagementArray = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 2

===Explanation===
"a","b","c", - 1 weak player (viral), 0 weak player (viral), 1 weak player (viral), 
"aa", "aab", "aabc", - 2 weak player (viral), 2 weak player (viral), 3 weak player (not-viral)
"ab", "abc", - 1 weak player (viral), 2 weak player (viral)
"bc", - 1 weak player (viral)
'''

def count_viral_combinations(video, engagement_array, k):
    # Initialize dp with zeros. Size is n x n where n is the length of the video
    n = len(video)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # Fill the diagonal of dp with counts for single characters
    for i in range(n):
        dp[i][i] = 0 if engagement_array[ord(video[i]) - ord('a')] else 1  # 1 for non-viral, 0 for viral

    print("===initial dp===")
    for row in dp:
        print(''.join(map(str, row)))

    # Fill the rest of dp by counting non-viral segments
    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = dp[i][j-1] + (0 if engagement_array[ord(video[j]) - ord('a')] else 1)

    print("===calculated dp===")
    for row in dp:
        print(''.join(map(str, row)))

    # Use a set to collect unique viral substrings
    st = set()
    for i in range(n):
        curr = ''
        for j in range(i, n):
            curr += video[j]
            if dp[i][j] > k:
                break
            print(curr)
            st.add(curr)

    return len(st)

# Main function to test the implementation
if __name__ == "__main__":
    # Python uses lists instead of Vectors
    engagement_array = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(count_viral_combinations("abc", engagement_array, 2))