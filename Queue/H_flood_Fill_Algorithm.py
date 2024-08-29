'''
Flood Fill Algorithm.
Given a 2D image img[][] where each img[i][j] is an integer representing the color of that pixel, also given the location of a pixel (x, y) and a new color newClr, the task is to replace the existing color of the given pixel and all the adjacent same-colored pixels with the given newClr.

Example: 

Input: img[][] =
{ {1, 1, 1},
{1, 1, 0},
{1, 0, 1} }
x = 1, y = 1, newClr = 3
Output: img[][] =
{{3, 3, 3},
{3, 3, 0},
{3, 0, 1}}
Explanation: The value at arr[1][1] is 1. All connected pixels with the color 1 are replaced with 3

Input: img[][] =
{ {0, 0, 0},
{0, 1, 1} }
x = 1, y = 1, newClr = 1
Output: img[][] =
{{0, 0, 0},
{0, 1 , 1}}
Explanation: Old and new colors are same, so no change

Input:: arr[][] =
{ {2, 2, 2},
{2, 2, 2}, }
x = 0, y = 0, newClr = 1
Output: img[][] =
{{1, 1, 1},
{1, 1, 1}}}
'''
def dfs(img, x, y, prev_clr, new_clr):
  
    # Base case: if the current pixel is not 
    # the same as the previous color
    if img[x][y] != prev_clr:
        return

    # Marking it as the new color
    img[x][y] = new_clr

    # Moving up, right, down, and left one by one
    n = len(img)
    m = len(img[0])
    if x - 1 >= 0:
        dfs(img, x - 1, y, prev_clr, new_clr)
    if y + 1 < m:
        dfs(img, x, y + 1, prev_clr, new_clr)
    if x + 1 < n:
        dfs(img, x + 1, y, prev_clr, new_clr)
    if y - 1 >= 0:
        dfs(img, x, y - 1, prev_clr, new_clr)

def flood_fill(img, x, y, new_clr):
    prev_clr = img[x][y]
    if prev_clr == new_clr:
        return
    dfs(img, x, y, prev_clr, new_clr)

# Driver code
img = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

# Co-ordinate provided by the user
x = 1
y = 1

# New color that has to be filled
new_clr = 3
flood_fill(img, x, y, new_clr)

# Printing the updated img
for row in img:
    print(' '.join(map(str, row)))
