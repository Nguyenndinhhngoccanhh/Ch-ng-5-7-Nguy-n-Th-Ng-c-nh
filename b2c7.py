# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:33:36 2024

@author: Ngoc Anh
"""

danh_sach = [('Tiền Giang', 63), ('Long An', 62), ('Vĩnh Long', 64), ('Bình Dương', 61)]
danh_sach_sap_xep = sorted(danh_sach, key=lambda x: x)
print(danh_sach_sap_xep)
