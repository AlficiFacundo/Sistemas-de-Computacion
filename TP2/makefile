# Makefile — TP2 GINI
# Compila: gini.asm + gini_calc.c → libgini.so (biblioteca compartida)
# Python la carga en tiempo de ejecución con ctypes.

CC        = gcc
NASM      = nasm
CFLAGS    = -Wall -fPIC          
NASMFLAGS = -f elf64             
TARGET    = libgini.so
VENV      = venv
PYTHON    = $(VENV)/bin/python3
PIP       = $(VENV)/bin/pip

all: $(TARGET)

# Crea el venv e instala dependencias
$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install requests

deps: $(VENV)/bin/activate
	@echo "[OK] Entorno virtual listo en ./$(VENV)"

# Detectar si el .asm existe para decidir qué usar
ASM_EXISTS := $(wildcard gini.asm)

ifeq ($(ASM_EXISTS), gini.asm)
    $(info [INFO] Usando rutina ASM: gini.asm)

    gini.o: gini.asm
	    $(NASM) $(NASMFLAGS) -o gini.o gini.asm

    gini_calc.o: gini_calc.c gini_calc.h
	    $(CC) $(CFLAGS) -c -o gini_calc.o gini_calc.c

    $(TARGET): gini.o gini_calc.o
	    $(CC) -shared -o $(TARGET) gini.o gini_calc.o
else
    $(info [INFO] gini.asm no encontrado — compilando con stub C)

    gini_calc.o: gini_calc.c gini_calc.h
	    $(CC) $(CFLAGS) -c -o gini_calc.o gini_calc.c

    gini_stub.o: gini_stub.c
	    $(CC) $(CFLAGS) -c -o gini_stub.o gini_stub.c

    $(TARGET): gini_calc.o gini_stub.o
	    $(CC) -shared -o $(TARGET) gini_calc.o gini_stub.o
endif

# Ejecutar 
run: deps $(TARGET)
	$(PYTHON) main.py

# Limpieza 
clean:
	rm -f *.o $(TARGET)

clean-all: clean
	rm -rf $(VENV)

.PHONY: all deps run clean clean-all
