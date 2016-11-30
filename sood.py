
import math, matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
by "Mohmmad Hossein Forouhesh Tehrani" in April 2016
to calculate the deposition of your money dropped in bank
"""


def printCol(var):
    for i in range(0, len(var)):
        print('month: {:3} | Total Wealth: {:.2f}'.format(i, var[i]))


def BankingDeposition(initial, rate, value, year):
    try:
        response = (12 / rate) * value
    except ZeroDivisionError as err:
        print(err)

    wealth = (initial + response) * math.e**(rate * year) - response
    return wealth


def BanckingWithInfarction(initial, rate, value, year, infarctMoney, infarctionTime, isSaved=None):
    wealthTotal = list()
    try:
        response = (12 / rate) * value
    except ZeroDivisionError as err:
        print(err)

    for t in range(0, len(year)):
        if t < infarctionTime:
            wealthTotal.append((initial + response) * math.e**(rate * year[t]) - response)
        else:
            const = ((initial + response) * math.e**(year[infarctionTime - 1] * rate) - 2 * infarctMoney) / (math.e**(year[infarctionTime] * rate))
            if isSaved:
                wealthTotal.append((const * math.e ** (rate * year[t]) + infarctMoney - response) + infarctMoney)
            else:
                wealthTotal.append(const * math.e**(rate * year[t]) + infarctMoney - response)
    return wealthTotal


def main() -> object:
    init = input('init ')
    rate = input('rate ')
    value = input('value ')
    duration = input('duration in year ')
    infarction = input('if infarction happens[Y/n]?')

    if value.find('.'):
        value = float(value)
    else:
        value = int(value)

    month = np.arange(0, int(duration), 0.0833)

    if str(infarction) == 'Y' or str(infarction) == 'y':
        infarctionTime = input('InfarctionTime in month ')
        infarctMoney = input('InfarctMoney ')
        isSaved = input('save infarct money some where else[Y/n]?')

        if str(isSaved) == 'Y' or str(isSaved) == 'y':
            isSaved = True
        elif str(isSaved) == 'N' or str(isSaved) == 'n':
            isSaved = False
        else:
            print('IO error')

        deposit = BanckingWithInfarction(int(init), float(rate), value, month, int(infarctMoney), int(infarctionTime), isSaved=isSaved)

    elif str(infarction) == 'N' or str(infarction) == 'n':
        deposit = BankingDeposition(int(init), float(rate), value, month)

    else:
        pass

    printCol(deposit)

    plt.scatter(month, deposit)

    plt.xlabel('Year')
    plt.ylabel('Wealth')
    plt.title('Histogram of Deposition')

    plt.show()
    matplotlib.interactive(True)

if __name__ == "__main__":
    main();
