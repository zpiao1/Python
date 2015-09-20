__author__ = 'zpiao1'


def pounds2Dollars(pounds, exchangeRate):
    return pounds * exchangeRate


pounds = float(input("Enter the money in pounds: "))
exchangeRate = float(input("Enter the exchange rate: "))
dollars = pounds2Dollars(pounds, exchangeRate)
print("The money in dollars is: ${:.2f}".format(dollars))



