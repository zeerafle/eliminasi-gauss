import click
import numpy as np

@click.command()
@click.argument('matriks')
@click.argument('vektor')
@click.option('--tampilkan_solusi', '-s', type=click.Choice(['ya', 'tidak']))
def eliminasi_gauss_naif(matriks, vektor, tampilkan_solusi):
    """
    Melakukan eliminasi gauss pada sistem persamaan linear

        Parameter: 

            matriks (string): Matriks dengan kolom dipisah dengan spasi dan baris dipisah dengan titik koma

            vektor (string): Vektor dengan 1 baris dengan jumlah elemen sebanyak ordo dan dipisah dengan spasi
        
        Returns:

            Matriks teraugmentasi dengan entri dibawah diagonal utama bernilai nol
            
            (Jika ingin menampilkan solusi, tambahkan option '-s ya')
    """
    A = np.mat(matriks, dtype=np.float64)
    b = np.array(np.mat(vektor), dtype=np.float64).reshape((-1,1))
    
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
    
    if tampilkan_solusi == "ya":
        click.echo(sulih_mundur(A, b))
    else:
        click.echo(np.append(A, b.reshape((-1, 1)), axis=1))

def pivotingSebagian(A, b, loop, n):
    for i in range(loop+1, n):
        if np.fabs(A[i,loop]) > np.fabs(A[loop,loop]):
            A[[loop,i]] = A[[i,loop]]
            b[[loop,i]] = b[[i,loop]]
            break
    return A, b

def sulih_mundur(A, b):
    n = len(A)
    x = np.zeros(n, float)
    # x[n-1] = b[n-1] / A[n-1,n-1]
    for i in range(n-1, -1, -1):
        sigma = 0
        for j in range(i+1, n):
            sigma += A[i,j] * x[j]
        x[i] = (b[i] - sigma) / A[i,i]
    
    return x