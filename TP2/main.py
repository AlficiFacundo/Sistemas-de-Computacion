# main.py
# Capa superior: consume API del Banco Mundial y muestra índice GINI

import requests
import ctypes
import os
import sys

# 1. Cargar la biblioteca compartida C + ASM
SO_PATH = os.path.join(os.path.dirname(__file__), "libgini.so")

try:
    lib = ctypes.CDLL(SO_PATH)
except OSError as e:
    print(f"[ERROR] No se pudo cargar libgini.so: {e}")
    sys.exit(1)

lib.calcular_gini.argtypes = [ctypes.c_double]
lib.calcular_gini.restype  = ctypes.c_long

# 2. Consumir la API del Banco Mundial
URL = (
    "https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI"
    "?format=json&date=2011:2020&per_page=32500&page=1"
)

print("\n[Python] Consultando API")
try:
    response = requests.get(URL, timeout=15)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print(f"[ERROR] Fallo la consulta a la API: {e}")
    sys.exit(1)

registros = data[1] if len(data) > 1 else []

# 3. Filtrar Argentina y quedarse con valores no nulos
argentina = [
    r for r in registros
    if r.get("country", {}).get("id") == "AR" and r.get("value") is not None
]

if not argentina:
    print("[Python] No se encontraron datos de GINI para Argentina.")
    sys.exit(1)

argentina.sort(key=lambda r: r["date"], reverse=True)

# 4. Mostrar resultados pasando por C y ASM 
print("\n" + "─" * 55)
print("  Índice GINI — Argentina (Banco Mundial)")
print("─" * 55)
print(f"  {'Año':<8} {'GINI (float)':<18} {'ASM int(GINI) + 1'}")
print("─" * 55)

for registro in argentina:
    anio   = registro["date"]
    valor  = float(registro["value"])       
    resultado = lib.calcular_gini(valor)    
    print(f"  {anio:<8} {valor:<18.4f} {resultado}")

print("\n[Python] Proceso completado\n")
