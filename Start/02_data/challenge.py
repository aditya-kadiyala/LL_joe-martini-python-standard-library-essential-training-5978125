"""
  Sorting complex objects witht he key parameter

  You are given a list of tuples. Each tuple represents a stock quote: the ticker, the opening value, the closing value

  The list looks like this:
  # Ticker, Opening, Closing
  quotes = [
    ("XYZ", 100.0, 105.2),
    ("XYZ", 101.3, 102.5),
    ("XYZ", 98.7, 99.7),
    ("XYZ", 99.7, 102.1),
    ("XYZ", 101.9, 103.5),
  ]

  Your task: sort the list by the closing values of each stock, in descending order.

  Parameters
  quotes: A list of tuples that each represent a stock quote

  Result
  list: The list of quotes, sorted by the closing value, in descending order(largest closing value comes first)

  The above quote list would be sorted as:

  quotes = [
    ("XYZ", 100.0, 105.2),
    ("XYZ", 101.9, 103.5),
    ("XYZ", 101.3, 102.5),
    ("XYZ", 99.7, 102.1),
    ("XYZ", 98.7, 99.7),
  ]
  """

from operator import itemgetter

def sort_stocks(quotelist):
  sorted_quotelist = sorted(quotelist, key = lambda i: i[2], reverse=True)
  # sorted_quotelist = sorted(quotelist, key = itemgetter(2), reverse=True) # using operator
  return sorted_quotelist


quotes = [
  ("XYZ", 100.0, 105.2),
  ("XYZ", 101.3, 102.5),
  ("XYZ", 98.7, 99.7),
  ("XYZ", 99.7, 102.1),
  ("XYZ", 101.9, 103.5),
] 
print(sort_stocks(quotes))