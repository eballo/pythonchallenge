# http://www.pythonchallenge.com/pc/return/cow.html
# hmm. it's a male.
# http://www.pythonchallenge.com/pc/return/bull.html
# len(a[30]) = ?
# user: 'huge'
# pass: 'file'

#  sequence : a = [1, 11, 21, 1211, 111221,
# look and say: one, one-one, one-two one-one, one-one one-two two-one, three-one two-two one-one, ...

# 1      : 11
# 11     : 21
# 21     : 1211
# 1211   : 111221
# 111221 : 312211

# size X number
look_and_say = {
    ("1", "1", "1"): "31",  # three-one
    ("1", "1"): "21",  # two-one
    ("1"): "11",  # one-one
    ("2", "2", "2"): "32",  # three-two
    ("2", "2"): "22",  # two-two
    ("2"): "12",  # one-two
    ("3", "3", "3"): "33",  # three-three
    ("3", "3"): "23",  # two-three
    ("3"): "13",  # one-three
    ("4", "4", "4"): "34",  # three-four
    ("4", "4"): "24",  # two-four
    ("4"): "14",  # one-four
}

# is the length + value for the same value consecutive

elements = "1"
new_elements = ''


def get_times_for_element_before_next_element(elements, start_position):
    same_number = 0
    index = start_position
    while index < len(elements):
        if elements[start_position] == elements[index]:
            # print("same number")
            same_number += 1
            index += 1
        else:
            # print("not the same number")
            break
    return same_number


for i in range(0, 30):
    j = 0
    new_elements = ''
    while j < len(elements):
        times = get_times_for_element_before_next_element(elements, j)
        # print(times)
        new_elements = new_elements + str(times) + str(elements[j])
        j = j + times
    print("--")
    elements = new_elements
    print(new_elements)

print("len(a[30]) = ?: " + len(new_elements))
