'''
The square-ten tree decomposition of an array is defined as follows:

The lowest (0th) level of the square-ten tree consists of single array elements in their natural order.
The kth level (starting from 1) of the square-ten tree consists of subsequent array subsegments of length 10 power 2k-1 in their natural order. 
Thus, the 1st level contains subsegments of length 10 power 2 power 1-1 = 10, the 2nd level contains subsegments of length 10 power 2 power 2-1 = 100, the 3rd level contains subsegments of length 10 power 2 power 3-1 = 10000, etc.
In other words, every kth level (for every k > equal to 1) of square-ten tree consists of array subsegments indexed as:


Level 0 consists of array subsegments indexed as 
[1,1], [2,2], ............, [i,i],,,,,,,,,,,,,,.
The image below depicts the bottom-left corner (i.e., the first 128 array elements) of the table representing a square-ten tree. 
The levels are numbered from bottom to top:

4x128 square-ten tree table

Task
Given the borders of array subsegment [L,R], find its decomposition into a minimal number of nodes of a square-ten tree. 
In other words, you must find a subsegment sequence [l1,r1], [l2, r2], ....., [lm, rm] such as li+1 = ri+1 for every 1<equal to i , l1 =L,rm= R , where every [li,ri] belongs to any of the square-ten tree levels and m is minimal amongst all such variants.

Input Format
The first line contains a single integer denoting L.
The second line contains a single integer denoting R.

Constraints
- 1<equal to L <equal to R <equal to 10 power 10 power 6.
- The numbers in input do not contain leading zeroes.

Output Format
As soon as array indices are too large, you should find a sequence of m square-ten tree level numbers,s1,s2,.......,sm , meaning that subsegment [li,ri] belongs to the 8ith level of the square-ten tree.

Print this sequence in the following compressed format:

On the first line, print the value of n (i.e., the compressed sequence block count).
For each of the n subsequent lines, print 2 space-separated integers,ti and ci (ti> equal to 0, ci>equal to 0 ), meaning that the number ti appears consequently ci times in sequence s. Blocks should be listed in the order they appear in the sequence. 
In other words,s1, s2,........., sc1  should be equal to t1,sc1, sc2, ..................., sc1+c2  should be equal to t2, etc.
Thus  must be true and  must be true for every . All numbers should be printed without leading zeroes.

Sample Input 0

1
10
Sample Output 0

1
1 1
'''
import sys
import cProfile


class output_result:
    ROOT_UPDATE = 0
    LEFT_TREE_UPDATE = 1
    RIGHT_TREE_UPDATE = 2

    def __init__(self):
        self.root = []
        self.ltree = []
        self.rtree = []
        self.bt_cnt = 0
        self.obuf = ""

    def __insert_node(self, node, tree_update):
        if (tree_update == self.LEFT_TREE_UPDATE):
            nl = []
            nl.insert(0, node)
            if (len(self.ltree) > 0):
                t = self.ltree.pop(0)
                nl.insert(1, t)
                nl.insert(2, [])
            else:
                nl.insert(1, [])
                nl.insert(2, [])
            self.ltree.insert(0, nl)
        elif (tree_update == self.RIGHT_TREE_UPDATE):
            nl = []
            nl.insert(0, node)
            if (len(self.rtree) > 0):
                t = self.rtree.pop(0)
                nl.insert(1, [])
                nl.insert(2, t)
            else:
                nl.insert(1, [])
                nl.insert(2, [])
            self.rtree.insert(0, nl)
        else:
            self.root.insert(0, node)
            if (len(self.ltree) > 0):
                self.root.insert(1, self.ltree[0])
            else:
                self.root.insert(1, [])
            if (len(self.rtree) > 0):
                self.root.insert(2, self.rtree[0])
            else:
                self.root.insert(2, [])
        if len(node[1]) > 0 and node[1][0] != 0:
            self.bt_cnt += 1
        return

    def __inorder_traversal(self, node):
        if (len(node[1]) > 0):
            self.__inorder_traversal(node[1])

        if len(node[0][1]) > 0:
            outputstr = ''.join(map(str, node[0][1]))
            if (outputstr != "0"):
                self.obuf += str(node[0][0]) + " " + outputstr + "\n"

        if (len(node[2]) > 0):
            self.__inorder_traversal(node[2])
        return

    def get_root(self):
        return self.root

    def get_tree_cnt(self):
        return self.bt_cnt

    def left_tree_add(self, node):
        self.__insert_node(node, self.LEFT_TREE_UPDATE)
        return

    def right_tree_add(self, node):
        self.__insert_node(node, self.RIGHT_TREE_UPDATE)
        return

    # add the root node
    def root_add(self, node):
        self.__insert_node(node, self.ROOT_UPDATE)
        return

    # print the output result
    def print_output(self):
        sys.stdout.write(str(self.bt_cnt) + "\n")
        self.__inorder_traversal(self.root)
        sys.stdout.write(self.obuf)
        return

# each entry is stored as (asl, max-entries, mav-value)
ores = []
l = 0
r = 0
clv = 0


def create_ten_power_x_list(k):
    if (k <= 1):
        return [1, 0], 1
    rl = [1]
    r2p = 0
    if (k > 1):
        r2p = pow(2, k - 1)
        rl = rl + [0]*r2p
    return rl, r2p


# algo for a + b
def add_two_int_list(x, y):
    # print "======"
    # print "add_two_int_list: " + " x: " + str(x) + " y: " + str(y)
    al = len(x)
    bl = len(y)
    if (bl == 0):
        a = x[:]
    elif (al == 0):
        a = y[:]
    else:
        if (al < bl):
            a = y[:]
            minl = al
            b = x
            maxl = bl
        elif (bl < al):
            a = x[:]
            maxl = al
            b = y
            minl = bl
        else:
            a = x[:]
            b = y
            maxl = al
            minl = bl

        carry = 0
        i = 1
        entries = 0
        # a >= b as per this logic and result is also stored in a
        while entries < minl:
            sum_t = b[minl - i] + a[maxl - i] + carry
            if (sum_t >= 10):
                carry = 1
                a[maxl - i] = sum_t - 10
            else:
                carry = 0
                a[maxl - i] = sum_t
            i += 1
            entries += 1

        # if carry > 0, then we need to do some more work
        i = maxl - minl - 1
        while carry > 0 and i >= 0:
            sum_t = a[i] + carry
            if (sum_t >= 10):
                carry = 1
                a[i] = sum_t - 10
            else:
                a[i] = sum_t
                carry = 0
            i -= 1

        if (carry == 1):
            a = [1] + a

        if (a[0] == 0):
            a.pop(0)
    # print "add_two_int_list: " + " a: " + str(a)
    return a


# algo for a - b
def del_two_int_list(x, y):
    al = len(x)
    bl = len(y)
    # print "x: " + str(x) + " y: " + str(y)

    if al < bl:
        return []

    a = x[:]
    b = y

    if al == bl and a[0] < b[0]:
        return []

    a_i = al - 1
    b_i = bl - 1
    while (b_i >= 0):
        # subtraction borrow logic
        if (a[a_i] < b[b_i]):
            a[a_i] = 10 + a[a_i]
            i = 1
            while a[a_i - i] == 0:
                a[a_i - i] = 9
                i += 1
            a[a_i - i] -= 1
        # subtract logic
        a[a_i] = a[a_i] - b[b_i]
        a_i -= 1
        b_i -= 1

    i = 0
    while i < al:
        if a[i] != 0:
            break
        i += 1
    if i > 0:
        a = a[i:]
    # print "a: " + str(a)
    return a


def compare_two_list_int(a, b):
    a1 = len(a)
    b1 = len(b)

    if a1 > b1:
        return 1
    elif a1 < b1:
        return -1
    else:
        i = 0
        while (i < a1):
            if (a[i] != b[i]):
                if (a[i] > b[i]):
                    return 1
                else:
                    return -1
            i += 1
        return 0


# a % b where b is the number of zeroes in 10
def divmod_10_list_int(x, b, mod_reqd):
    # print(sys._getframe().f_code.co_name + " ")
    c = []
    a = x[:]
    al = len(a)
    if b >= len(a):
        return a, [0]
    if mod_reqd is True:
        c = a[al - b:]
        i = 0
        while i < len(c):
            if c[i] != 0:
                break
            i += 1
        c = c[i:]
    a = a[:al - b]
    return c, a


def range_traverse():
    global clv, l, r, ores
    clv_me, clv_10s = create_ten_power_x_list(clv)
    # print "#######"
    # print "l: " + str(l) + " r: " + str(r) + " clv_me: " + str(clv_me)
    range_diff = del_two_int_list(r, l)
    if compare_two_list_int(range_diff, clv_me) >= 0:
        modl, divl = divmod_10_list_int(l, clv_10s, True)
        del divl
        lent = del_two_int_list(clv_me, modl)
        if compare_two_list_int(lent, clv_me) == 0:
            lent = [0]
        rent, rentr = divmod_10_list_int(r, clv_10s, True)
        tmpl = add_two_int_list(l, lent)
        # print "tmpl: " + str(tmpl) + " lent: " + str(lent)
        modl, l = divmod_10_list_int(tmpl, clv_10s, False)
        del tmpl
        del modl
        modr, r = divmod_10_list_int(del_two_int_list(r, rent), clv_10s, False)
        del modr
        # print "l: " + str(l) + " r: " + str(r) + " clv_me: " + str(clv_me)
        ores.left_tree_add((clv, lent))
        ores.right_tree_add((clv, rent))
        clv += 1
        del range_diff
        range_traverse()
    else:
        ent = range_diff
        modent, divent = divmod_10_list_int(ent, clv_10s, True)
        # print "ent: " + str(ent) + " modent: " + str(modent)
        ores.root_add((clv, modent))
        del range_diff
    return


# @profile
def main():
    global ores, l, r
    ores = output_result()
    l = list(map(int, (sys.stdin.readline()).strip()))
    r = list(map(int, (sys.stdin.readline()).strip()))
    l = del_two_int_list(l, [1])
    range_traverse()
    ores.print_output()
    return


enable_profiling = 0
if __name__ == "__main__":
    if (len(sys.argv) == 2):
        if (sys.argv[1] == "profile"):
            enable_profiling = 1
        else:
            print("usage: %s profile <optional>" % sys.argv[0])
            exit(-1)
    if (len(sys.argv) > 2):
        print("usage: %s profile <optional>" % sys.argv[0])
        exit(-1)

    if (enable_profiling == 1):
        cProfile.run('main()')
    else:
        main()
    sys.exit(0)