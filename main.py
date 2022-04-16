#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

# def count_layouts(n, m, legos):
#     if n == 0 or m == 0:
#         return 1

#     total_cnt = 0
#     for h, w in legos:
#         if h > n or w > m:
#             continue
#         cnt = count_layouts(n - h, m, legos)
#         if w < m:
#             cnt *= count_layouts(h, m - w, legos)
#         total_cnt += cnt

#     return total_cnt


def count_layer_layouts(m, legos, memo={}):
    if m in memo:
        return memo[m]
    if m < 0:
        return 0
    if m == 0:
        return 1

    total_cnt = 0
    for width in legos:
        total_cnt += count_layer_layouts(m - width, legos, memo)

    memo[m] = total_cnt
    return total_cnt


def legoBlocks(n, m):
    K = 1000000007
    legos = [1, 2, 3, 4]
    P_memo = {}

    # T: total number of possible layouts (bad + good) for width "i + 1"
    T = [((count_layer_layouts(i + 1, legos, P_memo) % K) ** n) % K for i in range(m)]

    # G: number of good layouts that span the first "i + 1" columns
    G = []
    for i in range(m):
        G_i = T[i]
        for j in range(i):
            G_i -= (G[j] * T[i - j - 1]) % K
        G.append(G_i % K)

    return G[-1]


if __name__ == "__main__":
    with open(os.environ["INPUT_PATH"], "r") as f, open(os.environ["OUTPUT_PATH"], "w") as fptr:

        t = int(f.readline().strip())

        for t_itr in range(t):
            first_multiple_input = f.readline().rstrip().split()

            n = int(first_multiple_input[0])

            m = int(first_multiple_input[1])

            result = legoBlocks(n, m)

            fptr.write(str(result) + "\n")
