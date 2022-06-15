def calculating_math_func(data, frame={}):
    print(frame)
    if data in frame:
        return frame[data]
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    frame[data] = result
    return result

