def candles(a):
    """
    Args:
        a: Las alturas de las velas.
    
    Returns:
        El número de velas más altas.
    """

    max_height = a[0] 
    count = 0 
    
    for i in range(len(a)):
        if a[i] > max_height:
            max_height = a[i]
            count = 1  
        elif a[i] == max_height:
            count += 1  
    return count


if __name__ == "__main__":
    print(candles([4, 4, 1, 3])) # 2
    print(candles([1, 1, 1, 1, 1])) # 5
    print(candles([5, 3, 1, 3, 5, 3, 1, 3, 5])) # 3
    print(candles([10000, 10001, 10002, 10002, 10000])) # 2
    print(candles([999, 1000, 99, 912, 100])) # 1
