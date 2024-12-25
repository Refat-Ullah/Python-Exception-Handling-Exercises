try:
    x = int(input())
    assert x >= 0, "Only positive values are allowed."
except AssertionError as e:
    print("An error occurred:", str(e))