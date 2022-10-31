# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:13:20 2022

@author: oluwo
"""
import re
import string
x = string.digits
print(x)

text = '8000'
def pin_check(text):
    if len(text) == 4 or len(text) == 6:
        s = re.findall(r"\d", text)
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    return False 

print(pin_check(text))