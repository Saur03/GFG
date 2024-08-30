'''
Rotten Oranges – Minimum Time Required to Rot All
Given a matrix of dimension M * N, where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:  

0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges
The task is to the minimum time required so that all the oranges become rotten. A rotten orange at index (i,j ) can rot other fresh oranges which are its neighbors (up, down, left, and right). If it is impossible to rot every orange then simply return -1.

Examples: 

Input:  arr[][C] = { {2, 1, 0, 2, 1}, {1, 0, 1, 2, 1}, {1, 0, 0, 2, 1}};
Output: 2
Explanation: At 0th time frame:
{2, 1, 0, 2, 1}
{1, 0, 1, 2, 1}
{1, 0, 0, 2, 1}
At 1st time frame:
{2, 2, 0, 2, 2}
{2, 0, 2, 2, 2}
{1, 0, 0, 2, 2}
At 2nd time frame:
{2, 2, 0, 2, 2}
{2, 0, 2, 2, 2}
{2, 0, 0, 2, 2}

Input:  arr[][C] = { {2, 1, 0, 2, 1}, {0, 0, 1, 2, 1}, {1, 0, 0, 2, 1}}
Output: -1
Explanation: At 0th time frame:
{2, 1, 0, 2, 1}
{0, 0, 1, 2, 1}
{1, 0, 0, 2, 1}
At 1st time frame:
{2, 2, 0, 2, 2}
{0, 0, 2, 2, 2}
{1, 0, 0, 2, 2}
At 2nd time frame:
{2, 2, 0, 2, 2}
{0, 0, 2, 2, 2}
{1, 0, 0, 2, 2}
The 1 at the bottom left corner of the matrix is never rotten.
'''
# Python3 program to rot all oranges when you can move in all the four direction from a rotten orange
R = 3
C = 5

# Check if i, j is under the array limits of row and column
def issafe(i, j):

    if (i >= 0 and i < R and
            j >= 0 and j < C):
        return True
    return False


def rotOranges(v):

    changed = False
    no = 2
    while (True):
        for i in range(R):
            for j in range(C):

                # Rot all other oranges
                # present at (i+1, j),
                # (i, j-1), (i, j+1),
                # (i-1, j)
                if (v[i][j] == no):
                    if (issafe(i + 1, j) and
                            v[i + 1][j] == 1):
                        v[i + 1][j] = v[i][j] + 1
                        changed = True

                    if (issafe(i, j + 1) and
                            v[i][j + 1] == 1):
                        v[i][j + 1] = v[i][j] + 1
                        changed = True

                    if (issafe(i - 1, j) and
                            v[i - 1][j] == 1):
                        v[i - 1][j] = v[i][j] + 1
                        changed = True

                    if (issafe(i, j - 1) and
                            v[i][j - 1] == 1):
                        v[i][j - 1] = v[i][j] + 1
                        changed = True

        # if no rotten orange found
        # it means all oranges rottened
        # now
        if (not changed):
            break
        changed = False
        no += 1

    for i in range(R):
        for j in range(C):

            # if any orange is found
            # to be not rotten then
            # ans is not possible
            if (v[i][j] == 1):
                return -1

    # Because initial value
    # for a rotten orange was 2
    return no - 2


# Driver function
if __name__ == "__main__":

    v = [[2, 1, 0, 2, 1],
         [1, 0, 1, 2, 1],
         [1, 0, 0, 2, 1]]

    print("Max time incurred: ",
          rotOranges(v))


