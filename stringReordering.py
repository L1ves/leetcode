lst = [{'4': 'dog' }, {'2': 'took'}, {'3': 'his'},{'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}]
def sentence(lst):
    #1)пройти по списку
    #2)отсортировать от меньшего к большому по ключу
    #3) напечатать значения отсортированного списка со словарем
    kv_pairs = [(int(k),v) for i in lst for k,v in i.items()]
    new_list = sorted(kv_pairs)
    true_list = [str(v) for k,v in new_list]
    return ' '.join(true_list)