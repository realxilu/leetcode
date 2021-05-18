class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res, current_list, num_of_letters = [], [], 0
        # res -> final result list
        # current_list -> list of words which are traversed but not yet added to result
        # num_of_letters -> number of chars corresponding to words in current_list
        
        for word in words:
            # total no. of chars in current_list + total no. of chars in current word
            # + total no. of words (min. number of spaces between words) because 1 word requir 1 space at least
            if num_of_letters + len(word) + len(current_list) > max_width:
                num_spaces = len(current_list) - 1 or 1
                
                # round robin for padding spaces evenly
                for i in range(max_width - num_of_letters):
                    # add 1 space to each word in a round-robin fashion
                    current_list[i % num_spaces] += ' '
                
                # note the spaces have already been distributed here thus just combine them to a row
                res.append(''.join(current_list))
                # reset the cur list and char count for the remaining words
                current_list, num_of_letters = [], 0
            
            # add current word to the list and add length to char count
            current_list.append(word)
            num_of_letters += len(word)
        
        # words in the last line might not enter the 'if' condition, thus the line below
        res.append(' '.join(current_list).ljust(max_width))
        
        return res

# [KEY] padding space in the round robin fashin is absolutely the key to solving the problem
