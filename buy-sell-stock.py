# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


#---------------------------------O(N)^2---------------------------------------

def buy_and_sell_stock(list):
    max_profit = 0
    for i in range(0, len(list)-1):
        for j in range(i+1, len(list)):
            profit = list[j]-list[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

#initialize max_profit at 0
#iterate through the list starting at index 0 and ending 1 before the end
#while doing that, also iterate one ahead of the current index until the end of the list
#profit is the difference between the number at index j and index i
#if a profit is greater than the max profit, set max profit equal to that profit
#keep going until the end of the list


print(buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
print(buy_and_sell_stock([7, 6, 4, 3, 1]))


#----------------------------------O(N)-------------------------------------------

import sys

def o_of_n_stocks(list):
    min_price = sys.maxsize
    max_profit = 0
    for i in range(0, len(list)):
        if list[i] < min_price:
            min_price = list[i]
        elif list[i] - min_price > max_profit:
            max_profit = list[i] - min_price
    return max_profit

#initialize min_price as the largest integer python can store
#intialize max_profit at 0
#iterating through the list starting at index 0 and ending at the end of the list,
#if the number at index i is less than the largest integer python can store (it would always be on first iteration)
# set min_price equal to that number at index i --> sets min_price to the lowest number
#if the number at index i minus the minimum price is greater than the max profit:
# set max_profit equal to number at index i minus minimum price
# return max profit


print(o_of_n_stocks([7, 1, 5, 3, 6, 4]))
print(o_of_n_stocks([7, 6, 4, 3, 1]))

#-----------------------------O(N) OPTION 2------------------------------------------------

def find_max_profit(list):
    
    profit = 0
    max_profit = 0
    # if len(list) == 0:
    #     return 0
    min_price = list[0]

    for i in range(len(list)):
        
        min_price = min(min_price, list[i])
        
        profit = list[i] - min_price
        max_profit = max(max_profit, profit)

    return max_profit

#initialize profit at 0 and max_profit at 0
#initialize min_price at index 0 of the list
#for each number in the list:
#set the min_price equal to the minimum value of the min_price compared to list[i]
#set profit equal to the value of list[i] minus min_price
#set max_profit equal to the maximum value of profit compared to profit

print(find_max_profit([7, 1, 5, 3, 6, 4]))
print(find_max_profit([7, 6, 4, 3, 1]))

# Understanding the Python min() Method And for finding the minimum value among a set of items, 
# we can directly pass all of them to the min() function separated by commas(“, “).
