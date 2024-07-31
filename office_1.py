def outed(meet, boss):
    if meet is not None:
        return 'Get Out Now!' if (sum(meet.values()) + meet.get(boss) / len(meet) <= 5 else 'Nice Work Champ!'


def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss] ) / len(meet) <= 5 else 'Nice Work Champ!'

def binary_search(value, lists):
    low = 0
    high = len(lists)-1
    while low <= high:
        mid = low + high // 2
        guess = lists[mid]
        if guess == value:
            return mid
        if guess > value:
            high = mid -1
        else:
            low = mid + 1
        return None

