import random

#////////////////////////////////
def creaSubA(A, indIzq, indDer):
    return A[indIzq:(indDer + 1)]

def Merge(A, p, q, r): 
    izq = creaSubA(A, p, q)
    der = creaSubA(A, q + 1, r)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if(j >= len(der)) or (i < len(izq) and izq[i] < der[j]):
            A[k] = izq[i]
            i = i + 1
        else:
            A[k] = der[j]
            j = j + 1

def MergeS(A, p, r): 
    if(p < r):
        q = int((p + r)/2)   #Divide
        MergeS(A, p, q)    #Conquista
        MergeS(A, q + 1, r) 
        Merge(A, p, q, r)  #Mezcla o combina

        return A

#//////////////777

def BusquedaBinaIter(A,x,iizq,ider):#x es la llave
	#nos ahorramos la bandera con el return
	while iizq<=ider:
		medio=int((iizq+ider)/2)
		if x==A[medio]:
			return medio
		elif A[medio]<x:
			iizq=medio+1
		else:
			ider=medio-1
	return False	

def main():
	#L=random.sample(range(0,20),10)
    L=[1,2,3,4,5,6,7,8,9]
    print(L)
    MergeS(L,0,len(L)-1)
    print(L)
    print(BusquedaBinaIter(L,5,0,len(L)-1))
	
main()
