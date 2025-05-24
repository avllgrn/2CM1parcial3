from os import system

if __name__ == '__main__':
    system('cls')
    
    n = int(input('Dame n '))
    
    M = [ [0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i==j:
                M[i][j] = 1
            else:
                M[i][j] = 0

    for i in range(n):
        for j in range(n):
            print(f'{M[i][j]}', end='\t')
        print()
