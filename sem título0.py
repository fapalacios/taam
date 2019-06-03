import math
import sys

class ErroNaFunção(Exception):pass
class ErroNoX(ErroNaFunção): pass
class ErroNoBeta(ErroNaFunção): pass

def get_angle(x):
    if (x == 1):
        raise ErroNoX("OOPS: x = 0")
    beta = 1 / (1 - x**2)
    if abs(beta) > 1:
        raise ErroNoBeta("OOPS: x > 1")
    theta = math.acos(beta)
    return (theta)
# --- main code

try:
    x = float(input("Type x: "))
    y = get_angle(x)
    print("y = " + str(y))
except ErroNoX as var1:
    print(var1)
    sys.exit()
#except ErroNaFunção as var1:
#    print("Ocorreu uma exceção")
#    print(var1)
#    sys.exit()
except ErroNoBeta as var2:
    print(var2)
    sys.exit()
#else:
#    print("Cláusula 'else' foi executada")
#finally:
#    print("Bloco 1")