def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit


Q

prices = [100, 180, 260, 310, 40, 535, 695]
print(maxProfit(prices))


