def sum(numbers):
  result = 0
  for number in numbers:
      result += number
  return result

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([1, 2, 3, 4]) == 9

def test_product():
    assert product([1, 2, 3]) == 6
    assert product([1, 2, 3, 4]) == 24
