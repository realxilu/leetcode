class Solution:
    def reorderLogFiles(self, logs):
        letters, digits = [], []

        for log in logs:
            split_log = log.split()
            if split_log[1].isdigit():
                digits.append(log)
            else:
                # instead of lambda use tuple for sort to resolve tie
                letters.append((split_log[1:], log))

        letters.sort()

        # list comprehension only takes the second part
        return [log for _, log in letters] + digits

# The use of tuple is similar to \corp_Microsoft\merge_k_sorted_list.py
# (x, y): if x comes to tie then use y to further sort