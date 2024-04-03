def all_continents(lst): 
    #'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
    for country in lst:
        counter = 0
        # your code here
        if country['continent'] == 'Africa':
            counter += 1
        if country['continent'] == 'Asia':
            counter += 1
        if country['continent'] == 'Americas':
            counter += 1
        if country['continent'] == 'Europe':
            counter += 1
        if country['continent'] == 'Africa':
            counter += 1
    if counter == 5:
        return True
    else:
        return False


def all_continents(lst):
    #'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
    required_continent = {'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'}
    developer_continent = {developer['continent'] for developer in lst}
    return required_continent.issubset(developer_continent)
def all_continents(lst):
    return len(set(x["continent"] for x in lst)) == 5
