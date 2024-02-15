def collision(aPosition:tuple, aSize:tuple, bPosition:tuple, bSize:tuple):
    if aPosition[0] <= bPosition[0] + bSize[0] and aPosition[0] + aSize[0] >= bPosition[0]:
        if aPosition[1] <= bPosition[1] + bSize[1] and aPosition[1] + aSize[1] >= bPosition[1]:
            return True
    return False