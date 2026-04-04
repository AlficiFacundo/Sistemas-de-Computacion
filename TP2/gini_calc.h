#ifndef GINI_CALC_H
#define GINI_CALC_H

/* Declaración de la función ensamblador.
   C la ve como una función normal que recibe double y devuelve long. */
extern long gini_convert(double valor);

/* Función C que Python va a llamar vía ctypes.
   Recibe el GINI como double, llama al ASM, devuelve el resultado. */
long calcular_gini(double valor_gini);

#endif /* GINI_CALC_H */