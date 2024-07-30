def outed(meet, boss):
    if meet is not None:
        return 'Get Out Now!' if ((sum(meet.values()) + meet.get(boss) * 2 - meet.get(boss)) / len(
            meet)) <= 5 else 'Nice Work Champ!'


def outed(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss] ) / len(meet) <= 5 else 'Nice Work Champ!'