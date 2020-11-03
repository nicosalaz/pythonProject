def pascal(n):
    conta = 0
    estado = False
    result = [1]
    while(conta < n and estado == False):
        if len(result) == 1:
            result.append(1)
        else:
            for x in range(0,n):
                print(result)
                for y in range(0, x):
                    if y != len(result)-1:
                        intro = result[y]+result[y+1]
                        result.insert(y+1,intro)
        conta+=1
        if conta == n-1:
            estado= True

pascal(7)