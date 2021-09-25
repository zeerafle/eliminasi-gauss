import click
import os
import numpy as np

@click.command()
@click.argument('ordo')
def gauss(ordo):
    A = input_matrix(int(ordo))
    b = input_vektor(int(ordo))

    click.echo(eliminasi_gauss_naif(A, b))

def eliminasi_gauss_naif(A, b):
    n = len(A)
    for k in range(n-1):
        if np.fabs(A[k,k]) < 1.0e-12:
            A, b = pivotingSebagian(A, b, k, n)
        for i in range(k+1, n):
            if A[i,k] == 0:
                continue
            faktor = A[k,k]/A[i,k]
            for j in range(k, n):
                A[i,j] = A[k,j] - A[i,j] * faktor
            b[i] = b[k] - b[i] * faktor
    
    return np.append(A, b.reshape((-1, 1)), axis=1)

def input_matrix(ordo):
    list_matrix = []
    for i in range(ordo):
        baris = input(f"Masukkan entri matriks A sejumlah {ordo} kolom pada baris {i+1} dipisah dengan spasi\n")
        list_matrix.append(baris)
        os.system('cls' if os.name == 'nt' else 'clear')
    string_matrix = ";".join(list_matrix)

    return np.mat(string_matrix, dtype=np.float64)

def input_vektor(ordo):
    baris = input(f"Masukkan entri vektor b sebanyak {ordo} dipisah dengan spasi\n")
    os.system('cls' if os.name == 'nt' else 'clear')

    return np.array(np.mat(baris)).reshape(ordo)

def pivotingSebagian(A, b, loop, n):
    for i in range(loop+1, n):
        if np.fabs(A[i,loop]) > np.fabs(A[loop,loop]):
            A[[loop,i]] = A[[i,loop]]
            b[[loop,i]] = b[[i,loop]]
            break
    return A, b
