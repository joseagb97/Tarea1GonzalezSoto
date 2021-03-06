def check_char(x):
    if type(x) is not str:      # Compara si la variable de entrada es string
        print("No puede ingresar varoles de tipo int, array, float, clase...")
    elif len(x) > 1:        # Compara si solo se ingresó 1 solo caracter
        print("Error: Solo puede ingresar una letra")
    elif 64 < ord(x) < 91 or 96 < ord(x) < 123:
        return 0     # Verifica que se es una letra del abecedario y retorna 0
    else:       # Es un solo caracter que no es parte del abecedario
        print("Error: Solamente puede introducir letras(No cuenta la ñ)")


def caps_switch(x):
    if check_char(x) == 0:      # Verifica las condiciones de check_char
        if ord(x) < 91:      # Verifica que es mayúscula
            return chr(ord(x) + 32)      # Le suma 32 para la letra minúscula
        else:                # Cae en el caso de ser minúscula
            return chr(ord(x) - 32)       # Le resta 32 para la letra mayúscula
    else:
        print("Vuelva a intentarlo introduciendo solo 1 letra en formato str")

# PARA EJECUTAR LAS PRUEBAS ESCRIBA LA PALABRA pytest, LUEGO PRESIONE ENTER
# PRUEBAS


def test1():    # Verifica que sea solo 1 letra
    assert check_char("vT") == 0


def test2():    # Verifica que sea una letra(no cuenta ñ)
    assert check_char("ñ") == 0


def test3():    # Verifica que sea un string
    assert check_char(8) == 0


def test4():        # Verifica todas las entradas para check_char
    i = 65          # Primera letra(en número) en codigo ASCII
    while i < 123:
        assert check_char(chr(i)) == 0      # Cambia a caracter y verifica
        if i == 90:         # Última letra en mayúscula en ASCII
            i = i + 7       # Salta a las letras minúsculas
        else:
            i = i + 1       # Salta a siguiente letra


def test5():        # Verifica todas las entradas para caps_switch
    i = 65          # Primera letra(en número) en codigo ASCII
    while i < 123:      # Cambia a caracter y verifica
        if i < 91:      # Verifica que sea mayúscula
            assert caps_switch(chr(i)) == chr(i + 32)  # Verifica la minúscula
            if i == 90:     # Última letra en mayúscula en ASCII
                i = i + 7   # Salta a las letras minúsculas
            else:
                i = i + 1   # Salta a siguiente letra
        else:
            assert caps_switch(chr(i)) == chr(i - 32)  # Verifica la mayúscula
            i = i + 1       # Salta a siguiente letra
