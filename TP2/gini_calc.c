/* 
    gini_calc.c 
    Implementación de la función C que Python llamará vía ctypes.
    Esta función recibe un valor GINI como double, llama a la rutina en ensamblador
    para convertirlo a int y sumar 1, y devuelve el resultado como long. 
*/

#include <stdio.h>
#include "gini_calc.h"

long calcular_gini(double valor_gini) {
    // Llamada a la rutina ASM.
    long resultado = gini_convert(valor_gini);

    return resultado;
}
