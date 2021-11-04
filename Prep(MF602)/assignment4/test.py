# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 02:44:31 2021

@author: MSI_NB
"""




amount_reverse =[100000, 100000, 100000, 150000, 400000, 120000, 250000, 200000, 300000, 350000]
amount_winning = []
number = 0
total_offering_fv = 1400000.00
for i in range(len(amount_reverse)):
               
   if total_offering_fv > amount_reverse[i]:
            number += 1
            amount_winning += [amount_reverse[i]]
            total_offering_fv = total_offering_fv - amount_reverse[i]
   elif total_offering_fv < amount_reverse[i] and total_offering_fv >= 0:
            number += 1
            amount_winning += [total_offering_fv]
            total_offering_fv = total_offering_fv - amount_reverse[i]
   elif total_offering_fv < amount_reverse[i] and total_offering_fv < 0:
            amount_winning += [0]