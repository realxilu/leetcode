from functools import cmp_to_key


class Solution:
    def reorder_log_files(self, logs):
        letter_list, digit_list = [], []

        for x in logs:
            if x[-1].isdigit():
                digit_list.append(x)
            else:
                letter_list.append(x)

        letter_list = sorted(letter_list, key=cmp_to_key(self.comp))

        return [*letter_list, *digit_list]

    # KEY
    def comp(self, a, b):
        a_index, b_index = a.index(' '), b.index(' ')

        a_rest, b_rest = a[a_index:], b[b_index:]
        if a_rest > b_rest:
            return 1
        if a_rest < b_rest:
            return -1

        a_first, b_first = a[:a_index], b[:b_index]
        if a_first > b_first:
            return 1
        else:
            return -1
