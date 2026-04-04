/* gini_stub.c
   Reemplazo temporal de gini.asm
   Tiene la MISMA firma que la función ASM exportada: gini_convert(double)
*/

#include <stdio.h>

long gini_convert(double valor) {
    /* STUB: misma lógica que hará el ASM */
    long resultado = (long)valor + 1;

    return resultado;
}
