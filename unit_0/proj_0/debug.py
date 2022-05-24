# original code
"""
def get_sum_metrics(predictions, metrics=[]):
    for i in range(3):
        metrics.append(lambda x: x + i)

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)

    return sum_metrics
"""

# issues: it looks like the course developers just took the two examples from this booK: https://docs.python-guide.org/writing/gotchas/

# first issues is that since it is function's default argument, the new list "metrics" is created ONCE (when the function is defined), 
# you might not notice it if you call the function just one time, but every call after the first one will keeps appending to the SAME list;
# to fix, we need to create a new objest each time the function is called with no metrics argument passed.

# second issues is that the append function doesn't have any variable called i in its own scope, 
# so it checks the surrounding scope at call time (in for metric in metrics loop); 
# by then, the for loop has completed and i is left with its final value of 2.


# fixed code

def get_sum_metrics(predictions, metrics=None):
    if metrics is None:
        metrics = []
    for i in range(3):
        metrics.append(lambda x, y=i: x+y)

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)

    return sum_metrics
  
  
def main():
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    print(get_sum_metrics(3, [lambda x: x]))  # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9

if __name__ == "__main__":
    main()
