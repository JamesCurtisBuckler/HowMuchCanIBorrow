# -*- coding: utf-8 -*-
import numpy as np

def computePmt(PV, r, n):
    '''
    Compute how much you pay back per month.

    Parameters:
    PV : float - Present value or amount borrowed
    r : float - Monthly interest rate
    n : int - Number of months

    Returns:
    Pmt : float - Amount paid per month
    '''
    r = r / 100  # Convert APR to decimal
    r = r / 12   # Monthly interest rate

    Pmt = r * PV / (1 - (1 + r) ** -n)
    return Pmt

def computePV(Pmt, r, n):
    '''
    Compute how much you can afford to borrow.

    Parameters:
    Pmt : float - Amount you can afford to pay per month
    r : float - Monthly interest rate
    n : int - Number of months

    Returns:
    PV : float - Maximum amount you can afford to borrow
    '''
    r = r / 100  # Convert APR to decimal
    r = r / 12   # Monthly interest rate

    PV = (1 - (1 + r) ** -n) * Pmt / r
    return PV

# Input choice: 1 for PV, 2 for Pmt
while True:
    choice = int(input('Enter choice 1 for PV, 2 for Pmt -> '))
    if choice == 1 or choice == 2:
        break
    else:
        print(f'Enter 1 or 2, you entered {choice}\n')

if choice == 2:
    PV = float(input('Enter PV: '))
    r = float(input('Enter interest rate (APR): '))
    n = int(input('Enter number of months: '))

    pmt = computePmt(PV, r, n)
    pmt = np.round(pmt, 2)
    print(f"Payment is {pmt} per month")

if choice == 1:
    Pmt = float(input('Enter Pmt: '))
    r = float(input('Enter interest rate (APR): '))
    n = int(input('Enter number of months: '))

    PV = computePV(Pmt, r, n)
    print(f"Maximum amount you can borrow is {PV}")
