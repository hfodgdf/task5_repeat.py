def repeat(func, times, value):
    result = value
    for _ in range(times):
        result = func(result)
    return result

print(repeat(lambda x: x + 1, 3, 5))
print(repeat(lambda x: x * 2, 4, 1))git 
