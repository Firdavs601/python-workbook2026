def positives(nums):
    result = []
    for i in nums:
        if i > 0:
            result.append(i)
    return result
def has_negative(nums):
    for n in nums:
        if n < 0:
            return True
        
    return False 
