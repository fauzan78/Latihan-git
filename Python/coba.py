import numpy as np
import matplotlib.pyplot as plt

pers=input("Masukan f(x):")
a=float(input("Masukan Nilai a:"))
b=float(input("Masukan Nilai b:"))
e=1e-5
print("Akar persamaan adalah ",a,"dan",b)

def f(x):
    return eval(pers)

if f(a)*f(b)>0:
    print("Persamaan tidak memiliki akar")
else:
    print("n    a           b           c         f(a)         f(b)         f(c)")
    for i in range(15):
      c=(a+b)/2 
      print(i+1,"\t",format(a,".5f"),"\t",format(b,".5f")
        ,"\t",format(c,".5f"),"\t",format(f(a),".5f")
        ,"\t",format(f(b),".5f"),"\t",format(f(c),".5f"))
      if abs (f(c))<e:
        break
      elif f(a)*f(c)<0:
        b=c
      else:
        a=c
print ("Akar persamaannya adalah=",a, "dan",b)
c=np.linspace(2.5, 2.6, 100)
plt.plot(c,f(c))
plt.grid()
plt.show()
input ("\n tekan enter untuk keluar")