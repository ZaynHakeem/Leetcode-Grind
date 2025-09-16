def maxProfit(prices):
    left = 0
    right = 1
    best = 0
    

    while right < len(prices):
        if prices[right] >= prices[left]:
            best = max(best, prices[right] - prices[left])
        else:
            left += 1
        
        right += 1

    return best

print(maxProfit([7,1,5,3,6,4]))