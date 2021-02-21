# 2 sum solution!!!!

# # After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish
# the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

# To save your vacation, you need to get all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar
# the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# Before you leave, the Elves in accounting just need you to fix your expense report(your puzzle input)
# apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020
# what do you get if you multiply them together?

# Solution: take two pointers. one goes at beginning one goesat end. sort the list of numbers. go number by number. if the sum is less than 2020, advance the lefthand pointer to a larger num. 
# if the sum is greater than 2020, move the right hand pointer backwards to a smaller num. stop when the sum of the pointers is 2020. then return the sum

def find_2020(nums):

    sorted_nums = sorted(nums)
    print("sorted_nums is", sorted_nums)

    # left_pointer = sorted_nums[0]
    # right_pointer = sorted_nums[-1]

    # while left_pointer < right_pointer:
    #     if left_pointer + right_pointer == 2020:
    #         return left_pointer * right_pointer
    #     elif left_pointer + right_pointer < 2020:
    #         left_pointer ++
    #     else:
    #         right_pointer --

    left_index = 0
    right_index = len(sorted_nums) - 1
    print("right_index is", right_index)
    print("sorted_nums[right_index] is", sorted_nums[right_index])
    print("sorted_nums[-1] is", sorted_nums[-1])

    while left_index < right_index:
        if sorted_nums[left_index] + sorted_nums[right_index] == 2020:
            return sorted_nums[left_index] * sorted_nums[right_index]
        elif sorted_nums[left_index] + sorted_nums[right_index] < 2020:
            left_index += 1
        else:
            right_index -= 1
    return "no nums add to 2020"

print(find_2020([1721, 979, 366, 299, 675, 1456]))


# -------------

def find_2020_solution():
    complementary_numbers = set()

    with open('input.txt') as f:
        for line in f:
            num = int(line)

            complement = 2020-num

            if num in complementary_numbers:
                return num * complement
            
            else:
                complementary_numbers.add(complement)
                print(num)

    return "not found"

# set is faster than list.
# const time = O(1) size of input doesn't slow down process
# when you use sets you're pretty close to O(1) time
# using a set to keep track of what numbers you've seen so far is THE BEST solution
# O(n) or less is nice. we don't have to worry about data sets so large O(n) isgoing to get us in trouble
# n^2 will take too long for computer to finish