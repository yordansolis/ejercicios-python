def calcular_iva(monto):
    return monto * 0.19

precio_producto1= 1000
precio_producto2= 2000

print("1. Calcular IVA")
print(calcular_iva(precio_producto1)) #✅ 190.0
print(calcular_iva(precio_producto2)) #✅ 380.0