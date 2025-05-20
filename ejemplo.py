from os import system

if __name__ == '__main__':
    system('cls')
    
    m = int(input('Dame m '))
    n = int(input('Dame n '))
    
    for i in range(m):
        for j in range(n):
            print(f'i={i},j={j}')
