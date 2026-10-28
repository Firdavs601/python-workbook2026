def is_int(s):
    if not s:
        return False
    start = 0
    if s[0] in ('+', '-'):
        start = 1
        if len(s) == 1:
            return False
    for i in range(start, len(s)):
        if not ('0' <= s[i] <= '9'):
            return False     
    return True