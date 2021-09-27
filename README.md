# Eliminasi Gauss

Melakukan eliminasi gauss pada sistem persamaan linear

## Instalasi

Jika sudah memiliki git jalankan kode dibawah
```console
git clone https://github.com/zeerafle/eliminasi-gauss.git

cd eliminasi-gauss
```

Jika tidak, download repository ini dengan klik __Code__ di halaman ini kemudian pilih __Download as zip__. Ekstrak file zip tadi kemudian buka foldernya. Buka cmd/powershell di folder ini dengan klik kanan sambil tekan shift, kemudian pilih __Open PowerShell window here__

Selanjutnya jalankan kode dibawah
```console
python setup.py install --record files.txt
```

## Penggunaan

Program ini berjalan di terminal dengan sintaks berikut
```console
gauss [OPTIONS] MATRIKS VEKTOR
```

Dengan menampilkan matriks teraugmentasi dengan entri dibawah diagonal utama bernilai nol

Dimana:

- `[OPTIONS]` berisi pilihan `-s` atau `--tampilkan_solusi` dengan nilai `ya` atau `tidak` (default tidak). Opsi ini berfungsi menampilkan hasil berupa solusi $x$ dalam bentuk vektor.

- `MATRIKS` (berbentuk string) adalah sistem persamaan linear yang sudah dibentuk menjadi matriks, elemennya suda terdefinisi didalamnya. Cara penulisannya adalah:
    - Entri kolom dipisahkan dengan spasi
    - Entri baris dipisahkan dengan titik koma (;)

- `VEKTOR` (berbentuk string) adalah vektor kolom

Untuk melihat bantuan ketikkan `gauss --help`

### Contoh

Untuk mendapatkan solusi sistem persamaan linear berikut
$$
\begin{alignat*}{4}
    2x_1 & {}+{} &  3x_2 & {}-{} & x_3 & {}={} & 5 \\
    4x_1 & {}+{} &  4x_2 & {}-{} & 3x_3 & {}={} &  3 \\
    -2x_1 & {}+{} & 3x_2 & {}-{} & x_3 & {}={} & 1
\end{alignat*}
$$
maka jalankan perintah dibawah
```console
gauss "2 3 -1;4 4 -3;-2 3 -1" "5 3 1"
```
Output:
```console
[[ 2.          3.         -1.          5.        ] 
 [ 0.          1.          0.5         3.5       ] 
 [ 0.          0.          0.83333333  2.5       ]]
```

Tambahkan options `-s ya` untuk menampilkan solusi $x$
```console
gauss -s ya "2 3 -1;4 4 -3;-2 3 -1" "5 3 1"
```
Output:
```console
Solusinya adalah x = [1. 2. 3.]
```

## Pencopotan

Jalankan perintah dibawah (powershell)
```powershell
Get-Content files.txt | ForEach-Object {Remove-Item $_ -Recurse -Force}
```