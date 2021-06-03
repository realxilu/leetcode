# const removeKdigits = (num, k) = > {
#     let res = []

#     num += ''
#     for (let c of num) {
#         while (res.length & & res[res.length - 1] > c & & k) {
#             // make sure digits in 'res' are in ascending order
#             res.pop()
#             k--
#         }

#         // can't have leading '0's => De Morgan's law if hard to read
#         if (res.length | | c !== '0') res.push(c)
#     }

#     // need to remove k digits in total. pay attention to the scope of 'k'
#     while (res.length & & k--) res.pop()

#     return res.length ? res.join(''): '0'
# }
# TODO