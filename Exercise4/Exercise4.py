# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hCF79yLykIausPQUEvev9v8KBL7trTAO
"""

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
empty_list = []
for i in sample_list:
    if i not in empty_list:
        empty_list.append(i)
    else:
        print(i,end=' ')