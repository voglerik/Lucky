import math

a = float(input("a oldal (mm): "))
b = float(input("b oldal (mm): "))

K = 2 * (a+b) / 1000
T = a*b / 1000**2
r_k = (a+b) / 2000
r_b = min(a,b) / 2000 if a == b else None

print(f"Kerület: {K:.2f} m")
print(f"Terület: {T:.2f} m²")
print(f"Köré írt kör sugara: {r_k:.1f} mm")
if r_b:
    print(f"Bele írt kör sugara: {r_b:.1f} mm")
    