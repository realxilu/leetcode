class Solution:
    def __init__(self):
        self.less_than_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        self.tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        self.thousands = ['', 'Thousand', 'Million', 'Billion']

    def number_to_words(self, num):
        if num == 0:
            return 'Zero'

        i, words = 0, ''

        while num:
            if num % 1000:
                words = self._helper(num % 1000) + self.thousands[i] + ' ' + words
            num = num // 1000
            i += 1

        return words.strip()

    def _helper(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return self.less_than_20[num] + ' '
        elif num < 100:
            return self.tens[num // 10] + ' ' + self._helper(num % 10)
        else:
            return self.less_than_20[(num // 100)] + ' Hundred ' + self._helper(num % 100)
