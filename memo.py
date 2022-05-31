# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 00:50:43 2022

@author: yuito
"""
line = 0


# 文字列を受け取る場合
S = line

# 整数を受け取る場合
N = int(line)

# 小数を受け取る場合
F = float(line)


# 文字列を受け取る場合
A, B = line.split()

# 整数を受け取る場合
X, Y, Z = map(int, line.split())

# 小数を受け取る場合
H, M, S = map(float, line.split())

# 先頭文字列以下整数
S = line.split()[0]
X, Y, Z = map(int, line.split()[1:])


# 文字列を受け取る場合
A = line.split()

# 整数列を受け取る場合
A = list(map(int, line.split()))

# 小数列を受け取る場合
A = list(map(float, line.split()))
