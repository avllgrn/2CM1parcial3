from os import system
from Colas import Cola

class Nodo:
    def __init__(self, izquierdo=None, dato=None, derecho=None):
        self.izquierdo = izquierdo
        self.dato = dato
        self.derecho = derecho

    def __str__(self):
        return '| ' + str(self.dato) + ' |'

class Arbol:
    def __init__(self):
        self.raiz = None

    def __del__(self):
        self.eliminaArbolRecursivo(self.raiz)

    def estaVacio(self):
        return self.raiz==None

    def inserta(self, dato):
        if self.estaVacio():
            self.raiz = Nodo(None, dato, None)
        else:
            self.insertaRecursivo(self.raiz, dato)

    def insertaRecursivo(self, aqui, dato):
        if dato<=aqui.dato and aqui.izquierdo==None:
            aqui.izquierdo = Nodo(None, dato, None)
        elif dato>aqui.dato and aqui.derecho==None:
            aqui.derecho = Nodo(None, dato, None)
        elif dato<=aqui.dato and aqui.izquierdo!=None:
            self.insertaRecursivo(aqui.izquierdo, dato)
        elif dato>aqui.dato and aqui.derecho!=None:
            self.insertaRecursivo(aqui.derecho, dato)

    def muestraPreorden(self):
        self.muestraPreordenR(self.raiz)

    def muestraPreordenR(self, aqui):
        if aqui!=None:
            print(aqui, end=' ')
            self.muestraPreordenR(aqui.izquierdo)
            self.muestraPreordenR(aqui.derecho)

    def muestraInorden(self):
        self.muestraInordenR(self.raiz)

    def muestraInordenR(self, aqui):
        if aqui!=None:
            self.muestraInordenR(aqui.izquierdo)
            print(aqui, end=' ')
            self.muestraInordenR(aqui.derecho)

    def muestraPostorden(self):
        self.muestraPostordenR(self.raiz)

    def muestraPostordenR(self, aqui):
        if aqui!=None:
            self.muestraPostordenR(aqui.izquierdo)
            self.muestraPostordenR(aqui.derecho)
            print(aqui, end=' ')

    def muestraEnAmplitud(self):
        if not self.estaVacio():
            C = Cola()
            C.push(self.raiz)
            while not C.estaVacia():
                aqui = C.pop()
                print(aqui, end=' ')
                if aqui.izquierdo!=None:
                    C.push(aqui.izquierdo)
                if aqui.derecho!=None:
                    C.push(aqui.derecho)

    def busca(self, dato):
        return self.buscaRecursivo(self.raiz, dato)

    def buscaRecursivo(self, aqui, dato):
        if aqui == None:
            return False
        elif dato == aqui.dato:
            return True
        elif dato < aqui.dato:
            return self.buscaRecursivo(aqui.izquierdo, dato)
        elif dato > aqui.dato:
            return self.buscaRecursivo(aqui.derecho, dato)

    def eliminaArbol(self):
        if not self.estaVacio():
            self.eliminaArbolRecursivo(self.raiz)
            self.raiz=None

    def eliminaArbolRecursivo(self, aqui):
        if aqui!=None:
            self.eliminaArbolRecursivo(aqui.izquierdo)
            self.eliminaArbolRecursivo(aqui.derecho)
            del aqui

    def buscaMenor(self):
        if self.estaVacio():
            return None
        else:
            return self.buscaMenorRecursivo(self.raiz)

    def buscaMenorRecursivo(self, aqui):
        if aqui.izquierdo==None:
            return aqui
        else:
            return self.buscaMenorRecursivo(aqui.izquierdo)

    def eliminaMenor(self):
        if self.estaVacio():
            return None
        elif self.raiz.izquierdo==None:
            x = self.raiz
            self.raiz = x.derecho
            menor = x.dato
            del x
            return menor
        else:
            return self.eliminaMenorRecursivo(None, self.raiz)

    def eliminaMenorRecursivo(self, Padre, aqui):
        if aqui.izquierdo==None:
            Padre.izquierdo = aqui.derecho
            menor = aqui.dato
            del aqui
            return menor
        else:
            return self.eliminaMenorRecursivo(aqui, aqui.izquierdo)

    def buscaMayor(self):
        if self.estaVacio():
            return None
        else:
            return self.buscaMayorRecursivo(self.raiz)

    def buscaMayorRecursivo(self, aqui):
        if aqui.derecho==None:
            return aqui
        else:
            return self.buscaMayorRecursivo(aqui.derecho)

    def eliminaMayor(self):
        if self.estaVacio():
            return None
        elif self.raiz.derecho==None:
            x = self.raiz
            self.raiz = x.izquierdo
            mayor = x.dato
            del x
            return mayor
        else:
            return self.eliminaMayorRecursivo(None, self.raiz)

    def eliminaMayorRecursivo(self, Padre, aqui):
        if aqui.derecho==None:
            Padre.derecho = aqui.izquierdo
            mayor = aqui.dato
            del aqui
            return mayor
        else:
            return self.eliminaMayorRecursivo(aqui, aqui.derecho)

    def cuenta(self):
        if self.estaVacio():
            return 0
        else:
            return self.cuentaRecursivo(self.raiz)

    def cuentaRecursivo(self, aqui):
        if aqui==None:
            return 0
        else:
            return 1 + self.cuentaRecursivo(aqui.izquierdo) + self.cuentaRecursivo(aqui.derecho)

    def acumula(self):
        if self.estaVacio():
            return 0
        else:
            return self.acumulaRecursivo(self.raiz)

    def acumulaRecursivo(self, aqui):
        if aqui==None:
            return 0
        else:
            return aqui.dato + self.acumulaRecursivo(aqui.izquierdo) + self.acumulaRecursivo(aqui.derecho)

    def altura(self):
        return self.alturaRecursivo(self.raiz)

    def alturaRecursivo(self, aqui):
        if aqui==None:
            return 0
        i = self.alturaRecursivo(aqui.izquierdo)
        d = self.alturaRecursivo(aqui.derecho)
        if i>d:
            return 1 + i
        else:
            return 1 + d

    def profundidad(self, dato):
        return self.profundidadRecursivo(self.raiz, dato, 0)

    def profundidadRecursivo(self, aqui, dato, p):
        if aqui == None:
            return None
        elif dato == aqui.dato:
            return p
        elif dato < aqui.dato:
            return self.profundidadRecursivo(aqui.izquierdo, dato, p+1)
        elif dato > aqui.dato:
            return self.profundidadRecursivo(aqui.derecho, dato, p+1)

    def elimina(self, dato):
        if self.estaVacio():
            return False
        elif dato==self.raiz.dato:
            i = self.alturaRecursivo(self.raiz.izquierdo)
            d = self.alturaRecursivo(self.raiz.derecho)

            if i==0 and d==0:
                del self.raiz
                self.raiz=None
            elif i<=d:
                aux = Nodo(self.raiz.derecho, self.raiz.dato, None)
                x = self.eliminaMenorRecursivo(aux, self.raiz.derecho)
                self.raiz.dato = x
                self.raiz.derecho = aux.izquierdo
                del aux
            else:
                aux = Nodo(None, dato, self.raiz.derecho)
                x = self.eliminaMayorRecursivo(aux, self.raiz.izquierdo)
                self.raiz.dato = x
                self.raiz.izquierdo = aux.derecho
                del aux
            return True
        else:
            return self.eliminaRecursivo(None, self.raiz, dato)

    def eliminaRecursivo(self, Padre, aqui, dato):
        if dato < aqui.dato and aqui.izquierdo == None:
            return False
        elif dato > aqui.dato and aqui.derecho == None:
            return False
        elif dato < aqui.dato and aqui.izquierdo != None:
            return self.eliminaRecursivo(aqui, aqui.izquierdo, dato)
        elif dato > aqui.dato and aqui.derecho != None:
            return self.eliminaRecursivo(aqui, aqui.derecho, dato)
        elif dato == aqui.dato:
            i = self.alturaRecursivo(aqui.izquierdo)
            d = self.alturaRecursivo(aqui.derecho)
            print(f'i={i}, d={d}')

            if i==0 and d==0:
                if aqui==Padre.izquierdo:
                    Padre.izquierdo=None
                else:
                    Padre.derecho=None
                del aqui
            elif i<=d:
                aux = Nodo(aqui.derecho, aqui.dato, None)
                x = self.eliminaMenorRecursivo(aux, aqui.derecho)
                aqui.dato = x
                aqui.derecho = aux.izquierdo
                del aux
            else:
                aux = Nodo(None, dato, aqui.derecho)
                x = self.eliminaMayorRecursivo(aux, aqui.izquierdo)
                aqui.dato = x
                aqui.izquierdo = aux.derecho
                del aux
            return True

    def listaOrdenada(self, L):
        if not self.estaVacio():
            self.listaOrdenadaRecursivo(self.raiz, L)

    def listaOrdenadaRecursivo(self, aqui, L):
        if aqui!=None:
            self.listaOrdenadaRecursivo(aqui.izquierdo, L)
            L.append(aqui.dato)
            self.listaOrdenadaRecursivo(aqui.derecho, L)

    def generaDeLista(self, L):
        if len(L)>0:
            self.generaDeListaRecursivo(L, 0, len(L)-1)

    def generaDeListaRecursivo(self, L, ini, fin):
        if ini<=fin:
            m = ini + (fin-ini)//2
            self.inserta(L[m])
            self.generaDeListaRecursivo(L, ini, m-1)
            self.generaDeListaRecursivo(L, m+1, fin)

if __name__ == '__main__':
    system('cls')

    A = Arbol()

    A.inserta(50)
    A.inserta(30)
    A.inserta(70)
    A.inserta(20)
    A.inserta(40)
    A.inserta(60)
    A.inserta(80)
    A.inserta(10)
    A.inserta(25)
    A.inserta(35)
    A.inserta(45)
    A.inserta(55)
    A.inserta(65)
    A.inserta(75)
    A.inserta(90)

    print('\n\nInOrdem')
    A.muestraInorden()
    print('\n\nPreOrdem')
    A.muestraPreorden()
    print('\n\nPostOrdem')
    A.muestraPostorden()
    print('\n\nAnchura')
    A.muestraEnAmplitud()

    L = []
    A.listaOrdenada(L)
    print(f'\n\nL = {L}')
