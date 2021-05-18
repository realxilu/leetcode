class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res, current_list, num_of_letters = [], [], 0
        # res:              final result
        # current_list:     list of traversed words but not yet added to res
        # num_of_letters:   number of chars of words added to the current_list
        
        for word in words:
            # total number of chars in the current_list
            # + total number of chars in the current word
            # + total number of words (minimum number of spaces between words) because one word requires at least one space
            if num_of_letters + len(word) + len(current_list) > max_width:
                num_spaces = len(current_list) - 1 or 1
                
                # ROUND ROBIN for padding spaces evenly
                for i in range(max_width - num_of_letters):
                    # add one space to each word in a round-robin fashion
                    current_list[i % num_spaces] += ' '
                
                # note the spaces have already been distributed here thus just combine them to a row
                res.append(''.join(current_list))
                # reset the cur list and char count for the remaining words
                current_list, num_of_letters = [], 0
            
            # add current word to the list and add length to char count
            current_list.append(word)
            num_of_letters += len(word)
        
        # words in the last line might not enter the 'if' condition, thus the line below
        num_spaces = len(current_list) - 1
        last_row = (' '.join(current_list)) + self.remaining_spaces(max_width, num_of_letters, num_spaces)
        res.append(last_row)
        
        return res
    
    def remaining_spaces(self, max_width, num_of_letters, num_spaces):
        return str(''.join((max_width - num_of_letters - num_spaces) * [' ']))

# [KEY] padding space in the ROUND ROBIN fashin is absolutely the key to solving the problem
# I think 'or' in num_space is elegant