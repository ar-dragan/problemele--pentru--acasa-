n=6500
a=n%10   #unitatile numarului n
print("a,"ultima cifra a numarului n")
b=(n%100)//10 #zecile numarului n
print(b,"penultima cifra a numarului n")
print(n,"//",9,"=",n//9)
print(n,"%",9,"=",n%9)
c=(n%1000)// #sutimile numarului numarului n 
d=n//1000 #miimile numarului n
print(a+b+c+d," suma cifrelor numarului n")
m=1000*a+100*b+10*c+d
print(m,"rasturnatul numarului")

