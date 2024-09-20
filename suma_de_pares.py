def suma_par(matrizA):
    suma_par = 0
    n = len(matrizA)  

    for i in range(n):
        for j in range(n):
            if matrizA[i][j] % 2 == 0:
                suma_par += matrizA[i][j]

    return suma_par

if __name__ == "__main__":
    
    print(suma_par([
        [10, 11],
        [13, 14],
        
    ]))  # 24
    
    print(suma_par([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))  # 20

    print(suma_par([
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32],
        [33, 34, 35, 36]
    ]))  # 232

    print(suma_par([
        [12, 45, 67, 23, 89],
        [34, 78, 56, 91, 17],
        [43, 90, 22, 36, 81],
        [28, 11, 74, 55, 99],
        [63, 10, 85, 42, 19]
        
    ]))  # 482
    print(suma_par([
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]))  # 0
