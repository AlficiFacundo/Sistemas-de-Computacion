.code16                    # Código modo real

mov $msg, %si              # SI apunta al string
mov $0x0e, %ah             # Función 0x0e de BIOS: imprimir caracter en pantalla

loop:
    lodsb                
    or %al, %al            # Verifica si el caracter es 0
    jz halt                # Si es 0, salta a halt
    int $0x10              # Llama a la BIOS para imprimir el caracter
    jmp loop               # Repite para el siguiente caracter

halt:
    hlt                    # Detiene el CPU

msg:
    .asciz "Hello World"  