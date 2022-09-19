import time
def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end = time.time()
    print("calc_square took " + str((end-start)*1000) + " milliseconds")
    return result

def calc_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    print("calc_cube took " + str((end-start)*1000)+" milliseconds")
    return result
array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

