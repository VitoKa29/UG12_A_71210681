deret_angka = input("Masukkan deret angka : ")
split_angka = deret_angka.split(",")
count = len(split_angka)

if(int(split_angka[0]) % 2 == 0):
    awal = split_angka[0]
    sum = int(awal)
else:
    awal = int(split_angka[0])*-1
    sum = int(awal)

print("Total :",awal,end="")

for angka in split_angka[1:count]:
    if(angka != split_angka[0]):
        if (int(angka) % 2 == 1):        
            angka = int(angka) * -1
            sum = sum + int(angka) 
            print("",angka,end="")
        elif(int(angka) % 2 == 0):
            sum = sum + int(angka) 
            if (angka == split_angka[0]):
                print(angka,end="")
            else:
                print(" +",angka,end="")
    
print()
print("Hasil perhitungan diatas ialah",sum)