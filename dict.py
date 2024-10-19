# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:17:32 2024

@author: Ngoc Anh
"""

n = int(input("Nhập giá trị nguyên n: "))
tao_dict = {i: i** i for i in range(1, n + 1)}
print(tao_dict)
