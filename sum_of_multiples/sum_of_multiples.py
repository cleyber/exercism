def sum_of_multiples(limite, numeros):
    multiplos = []
    for n in numeros:
        for x in range(n, limite):
            if(x%n==0):
                if(not x in multiplos):
                    multiplos.append(x)
    return sum(multiplos)