department_scores = {
    "accounts": 1,
    "finance": 2,
    "canteen": 10,
    "regulation": 3,
    "trading": 6,
    "change": 6,
    "IS": 8,
    "retail": 5,
    "cleaning": 4,
    "pissing about": 25
}


def boredom(staff):
    # Initialize the total boredom score
    total_score = 0

    # Iterate through the staff dictionary
    for department in staff.values():
        # Add the boredom score of the department to the total
        total_score += department_scores[department]

    # Determine the sentiment based on the total score
    if total_score <= 80:
        return 'kill me now'
    elif total_score < 100:
        return 'i can handle this'
    else:
        return 'party time!!'



def boredom(staff):
    # Initialize the total boredom score

    # Iterate through the staff dictionary
    total_score = sum(department_scores[scores] for scores in staff.values())
        # Add the boredom score of the department to the total

    # Determine the sentiment based on the total score
    if total_score <= 80:
        return 'kill me now'
    elif total_score < 100:
        return 'i can handle this'
    else:
        return 'party time!!'

