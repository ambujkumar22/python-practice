"""By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

t = [[75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def func():
    num = [75,]
    index = [0,]
    for i in range(1,15):
        number = num[-1]
        ind = index[-1]

        left = t[i][ind]
        leftofleft = t[i+1][ind]
        common = t[i+1][ind+1]
        sum1 = number + left + leftofleft
        sum2 = number + left + common

        right = t[i][ind + 1]
        rightofright = t[i + 1][ind + 2]
        sum3 = number + right + common
        sum4 = number + right + rightofright

        if (sum1 > sum2) and (sum1 > sum3) and (sum1 > sum4):
            num.append(left)
            index.append(ind)
        elif (sum2 > sum1) and (sum2 > sum3) and (sum2 > sum4):
            num.append(left)
            index.append(ind)
        elif (sum3 > sum1) and (sum3 > sum2) and (sum3 > sum4):
            num.append(right)
            index.append(ind + 1)
        else:
            num.append(right)
            index.append(ind + 1)

    print(sum(num))

func()
