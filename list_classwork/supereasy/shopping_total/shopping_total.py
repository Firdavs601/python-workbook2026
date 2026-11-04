def total(prices):
    total_sum = 0
    for i in prices:
        total_sum += i
    return total_sum
def can_afford(prices, money):
    
    if money >= total(prices):
        return "yes" 
    else:
        return "no"