# Clock shows h hours, m minutes and s seconds after midnight.
#
# Your task is to write a function which returns the time since midnight in milliseconds.
#
# Example:
#
# h = 0
# m = 1
# s = 1
#
# result = 61000

def past(h, m, s):
    # Good Luck!
    MS_IN_S = 1000
    MS_IN_M = 60000
    MS_IN_H = MS_IN_M * 60
    return ((MS_IN_H * h) +  (MS_IN_M * m) + (MS_IN_S * s))