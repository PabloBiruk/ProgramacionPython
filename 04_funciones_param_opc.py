import math

def opcionales(oblig_1,oblig_2,opc_1="uno",opc_2="dos",*args,**kwargs):
    pass

opcionales(1,2)

# -----------------------------------------------------

def superficie(radio=1):
    return radio * radio * math.pi

s = superficie()
print(s)

# -----------------------------------------------------

def vol_cilindro(radio,altura):
    #return (radio*radio) * math.pi * altura
    return superficie(radio) * altura

v = vol_cilindro(10,12)
print(v)