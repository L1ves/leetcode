def difference_in_ages(ages):
    # your code here
    old_yong = []
    old = max(ages)
    yong = min(ages)
    diff = old - yong
    old_yong.append(yong)
    old_yong.append(old)
    old_yong.append(diff)
    return tuple(old_yong)

def difference_in_ages(ages):
    # your code here
    return (min(ages) , max(ages) , max(ages) - min(ages))