MAX_CLUE_LEN = 21


def trim_to_size(clue):
    if len(clue) <= 21:
        return [clue]
    else:
        return [clue[:19] + '-'] + trim_to_size('  ' + clue[19:])


def parse_clue_list(clue_list_element):
    parsed_list = []

    list_items = clue_list_element.find_elements_by_tag_name('li')
    for list_item in list_items:
        labels = list_item.find_elements_by_tag_name('label')
        label = labels[0].text.replace('\n', ' ')
        label_list = trim_to_size(label)
        parsed_list.extend(label_list)
    return parsed_list
