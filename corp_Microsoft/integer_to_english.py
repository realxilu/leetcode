class Solution:
    def __init__(self):
        # NOTE the first item is left as an empty string
        self.less_than_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                             'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        self.tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty',
                     'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        self.thousands = ['', 'Thousand', 'Million', 'Billion']

    def numberToWords(self, num):
        if num == 0:
            return 'Zero'

        i, words = 0, ''

        while num:
            if num % 1000:
                words = self._helper(num % 1000) + self.thousands[i] + ' ' + words
            num = num // 1000
            i += 1

        return words.strip()

    # [RECURSION]
    def _helper(self, num):
        # [IMPORTANT] handle '0' differently
        if num == 0:
            return ''
        # (0, 20)
        elif num < 20:
            return self.less_than_20[num] + ' '
        # [20, 100)
        elif num < 100:
            return self.tens[num // 10] + ' ' + self._helper(num % 10)
        # [100, 1000)
        else:
            return self.less_than_20[num // 100] + ' Hundred ' + self._helper(num % 100)

# [KEY][RECURSION] Figure out each intervals and handle them differently: 0 | 0 < x < 20 | 20 =< x < 100 | 100 < x <= 1000 | x > 1000
