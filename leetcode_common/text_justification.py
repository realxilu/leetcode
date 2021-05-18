class Solution:
    # This is a helper method used to calculate the remaining spaces needed to pad to the right side
    def remaining_spaces(self, max_width, num_chars, num_spaces):
        return str(''.join((max_width - num_chars - num_spaces) * [' ']))

    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res, cur_list, num_chars = [], [], 0
        # res:        final result
        # cur_list:   list of traversed words but not yet added to res
        # num_spaces: number of spaces that need to be inserted, the number of spaces needed is one less than the size of cur_list
        # num_chars:  number of chars of words added to the cur_list

        for word in words:
            # total number of chars in the cur_list
            # + total number of chars in the current word
            # + total number of words (minimum number of spaces between words) because one word requires at least one space
            if num_chars + len(word) + len(cur_list) - 1 >= max_width:
                num_spaces = len(cur_list) - 1 or 1

                # use round robin to pad spaces evenly in the remaining space
                for i in range(max_width - num_chars):
                    # add one space to each word in a round-robin fashion
                    cur_list[i % num_spaces] += ' '

                # note the spaces have already been distributed here thus just combine them to a row
                res.append(''.join(cur_list))
                # reset the cur list and char count for the remaining words
                cur_list, num_chars = [], 0

            # add current word to the list and add length to char count
            cur_list.append(word)
            num_chars += len(word)

        # This is for the LAST row. The LAST row requires single space and left justified
        # words in the last row might not enter the 'if' condition
        num_spaces = len(cur_list) - 1
        last_row = (' '.join(cur_list)) + self.remaining_spaces(max_width, num_chars, num_spaces)
        res.append(last_row)

        return res

# [KEY] padding space in the ROUND ROBIN fashin is absolutely the key to solving the problem
# 'or' in num_space is elegant. The original solution uses 'max' which was less readable
# The last row could have been handled more elegantly using 'ljust'. However the interviewer might not accept it.
# [ALTERNATIVE] result.append(' '.join(cur_list).ljust(maxWidth))
