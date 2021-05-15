class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, current_list, num_of_letters = [],[], 0
        # res -> stores final res output
        # current_list -> stores list of words which are traversed but not yet added to res
        # num_of_letters -> stores number of chars corresponding to words in current_list
        
        for w in words:
            # total no. of chars in current_list + total no. of chars in current w
            # + total no. of words ~= min. number of spaces between words
            if num_of_letters + len(w) + len(current_list) > maxWidth:
                # size will be used for module "magic" for round robin
                # we use max. 1 because atleast one w would be there and to avoid modulo by 0
                size = max(1, len(current_list)-1)
                
                for i in range(maxWidth-num_of_letters):
                    # add space to each w in round robin fashion
                    index = i%size
                    current_list[index] += ' ' 
                
                # add current line of words to the output
                res.append("".join(current_list))
                current_list, num_of_letters = [], 0
            
            # add current w to the list and add length to char count
            current_list.append(w)
            num_of_letters += len(w)
        
        # form last line by join with space and left justify to maxWidth using ljust (python method)
        # that means pad additional spaces to the right to make string length equal to maxWidth
        res.append(" ".join(current_list).ljust(maxWidth))
        
        return res