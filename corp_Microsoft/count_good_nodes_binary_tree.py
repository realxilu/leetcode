# The default parameter is very elegant here
class Solution:
    def goodNodes(self, node, _max=-float(inf)):
        if node is None:
            return 0

        res = 1 if node.val >= _max else 0
        res += self.goodNodes(node.left, max(_max, node.val))
        res += self.goodNodes(node.right, max(_max, node.val))

        return res
