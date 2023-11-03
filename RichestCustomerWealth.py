#https://leetcode.com/problems/richest-customer-wealth/
#вычисляем сколько денег у клиента, нужно зайти в каждый список и сделать sum
accounts = [[1,2,3],[3,1,1],[1,1,1,7]]
maxWealthSoFar = []
for customer in range(len(accounts)):
    currentCustomerWealth = 0
    for bank in accounts[customer]:
        currentCustomerWealth += bank
        maxWealthSoFar.append(currentCustomerWealth)
print(max(maxWealthSoFar))

#class Solution:
#    def maximumWealth(self, accounts: List[List[int]]) -> int:
#        maxWealthSoFar = []
#        for customer in range(len(accounts)):
#            currentCustomerWealth = 0
#            for bank in accounts[customer]:
#                currentCustomerWealth += bank
#                maxWealthSoFar.append(currentCustomerWealth)
#        return max(maxWealthSoFar)