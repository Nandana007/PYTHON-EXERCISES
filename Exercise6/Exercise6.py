# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hCF79yLykIausPQUEvev9v8KBL7trTAO
"""

row_count = int(input("Enter the number of rows:"))  
k = 1  
  
for i in range(row_count, 0, -1):   

    for j in range(1, i + 1):  
        print(k, end=' ') 
    print(end = "\n")
    k += 1