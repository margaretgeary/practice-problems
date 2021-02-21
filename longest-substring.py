# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:

# Input: s = ""
# Output: 0

# ------------------MY ANSWER---------------------

def find_longest_substring(string):
    count = 1
    left_pointer = 0
    right_pointer = 1
    while left_pointer < right_pointer:
        if string[left_pointer] != string[right_pointer]:
            count += 1
            left_pointer +=1
            right_pointer += 1
    return count


print(find_longest_substring("abcabcbb"))
print(find_longest_substring("bbbbb"))
print(find_longest_substring("pwwkew"))

#-------------------O(n^3)-----------------------

def find_longest_substring(string):
    n = len(string)
    result = 0
    for i in range(n):
        for j in range (i, n):
            if (areDistinct(string, i, j)):
                result = max(result, j - i + 1)
    return result

#-------------------O(n)------------------------


def find_longest_substring(string):
    
    #initialize the last index as -1, -1 is used to store last index of every character
    last_index = [-1] * 256

    len_of_string = len(string)
    result = 0
    i = 0

    for j in range(0, len_of_string):
        #find the last index of string[j]
        #update i (starting index of current window) as maximmum of current value of i and last index + 1
        i = max(i, last_index[ord(string[j])] + 1)

        #update result if we get a larger window
        result = max(result, j - i + 1)

        #update last index of j
        last_index[ord(string[j])] = j

    return result
