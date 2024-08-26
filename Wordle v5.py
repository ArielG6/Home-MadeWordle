#Funciones
def palabra_aleatoria():
    '''Selecciona palabra aleatoria desde un archivo con palabras'''
    try:
        archivo = open('palabras a adivinar.txt', "rt", encoding="UTF8")
        palabra = archivo.readline()
        n = 0
        while palabra:
            n = n + 1
            palabra = archivo.readline()
        m = random.randint(1, n)
        archivo.seek(0)
        palabra = archivo.readline()
        palabra=palabra.rstrip('\n')
        k = 0
        while palabra:
            k = k + 1
            if k==m:
                break
            palabra = archivo.readline()
            palabra=palabra.rstrip('\n')
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass
    return palabra

def palabra_esta_en_listado(palabra_a_validar):
    '''funcion que recibe como parametro la palabra ingresada (a validar) y verifica si esta en el archivo o no'''
    palabra_valida = False
    try:
        entrada = open('palabras a comprobar.txt', "rt")
        for palabra in entrada:
            palabra = palabra.rstrip("\n")
            if palabra == palabra_a_validar:
                palabra_valida = True
                break
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo", mensaje)
    except OSError as mensaje:
        print("ERROR: ", mensaje)
    finally:
        try:
            entrada.close()
        except NameError:
            pass
    return palabra_valida

def imprimir_reglas_del_juego():
    '''La función imprime las reglas del juego'''
    print('\n'*20)
    print('Bienvenidos al Wordle'.center(75))
    print()
    print('Objetivo:'.center(75))
    print('Adivinar la palabra secreta en 6 intentos'.center(75))
    print()
    print('Reglas del Juego'.center(75))
    print()
    print('1. Ingresar una palabra de 5 letras.')
    print('2. Luego de ingresar la palabra, las letras se colorean según lo siguiente:')
    print(f'\t{Fore.GREEN}Verde{Style.RESET_ALL}: La letra está en la palabra y está en el lugar correcto.')
    print(f'\t{Fore.YELLOW}Amarillo{Style.RESET_ALL}: La letra está en la palabra pero está en el lugar equivocado.')
    print(f'\t{Fore.BLACK}Negro{Style.RESET_ALL}: La letra no está en la palabra.')
    print('Nota: puede haber letras repetidas.')

def sacar_tilde(palabra):
    '''Funcion que recibe como parametro una cadena (palabra) y le saca las tildes'''
    sintilde='aeiouAEIOU'
    contilde='áéíóúÁÉÍÓÚ'
    palabrasintilde=''
    for caracter in palabra:
        if caracter in contilde:
            posicion=contilde.index(caracter)
            palabrasintilde=palabrasintilde+sintilde[posicion]
        else:
            palabrasintilde=palabrasintilde+caracter
    return palabrasintilde

def formato_palabra(palabra):
    '''funcion que le da formato a la palabra ingresada, le da mayusculas y le saca los simbolos y signos'''
    if not palabra.isalpha():
        palabranueva=''
        for caracter in palabra:
            if caracter.isalpha():
                palabranueva=palabranueva+caracter
        palabra=palabranueva
    if not palabra.isupper():
        palabra=palabra.upper()
    return palabra

def guardar_resultado(n):
    '''Funcion que recibe como parametro la cantidad de intentos y lo guarda
    en un archivo. En caso de no haber adivinado, recibe X'''
    try:
        archivo_resultados = open('Resultados.txt', 'at')
        archivo_resultados.write(str(n) + '\n')
    except FileNotFoundError as mensaje:
        print('No se pudo abrir el archivo.', mensaje)
    except OSError as mensaje:
        print('No se pudo grabar el archivo.', mensaje)
    finally:
        try:
            archivo_resultados.close()
        except NameError:
            pass

def comparar_palabra(palabra_a_adivinar, palabra_ingresada):
    '''funcion que recibe como parametro la palabra a adivinar y la palabra ingresada y las compara. Devuelve un diccionario con los colores correspondientes'''
    lista_palabra_original = []
    lista_palabra_ingresada = []  
    for letra in palabra_a_adivinar:
        lista_palabra_original.append(letra)
    for letra in palabra_ingresada:
        lista_palabra_ingresada.append(letra)      
    dic_color = {}    
    lista_aux = []
    for i in range(len(lista_palabra_original)):  # buscamos los verdes
        if lista_palabra_original[i] == lista_palabra_ingresada[i]:
            dic_color[i] = 'verde'
        else:
            lista_aux.append(lista_palabra_original[i])
    for i in range(len(lista_palabra_ingresada)):  # buscamos los amarillos
        if lista_palabra_ingresada[i] in lista_aux and dic_color.get(i) != 'verde':
            dic_color[i] = 'amarillo'
            lista_aux.remove(lista_palabra_ingresada[i])
    for i in range(len(lista_palabra_original)):  # buscamos los negros
        if i not in dic_color:
            dic_color[i] = 'negro'
    return dic_color

def estadisticas():
    '''La función toma el archivo con los resultados almacenados para cada jugador,
    los procesa para obtener las estadísticas e imprime los resultados'''
    print('\n'*20)
    resultados = []
    try:
        arch = open('Resultados.txt','rt')
        resultado = arch.readline().rstrip('\n')
        while resultado:
            resultados.append(resultado)
            resultado = arch.readline().rstrip('\n')
    except FileNotFoundError:
        print('Falla al cargar historial de partidas')
    except OSError:
        print('No se puede leer el archivo')
    finally:
        try:
            arch.close()
        except NameError:
            pass
    for i in range(len(resultados)):
        resultados[i] = int(resultados[i])
    cont_resultados = []
    for i in range(7):       #Este número es la cantidad de intentos + 1
        cont_resultados.append(resultados.count(i+1))
    partidas = sum(cont_resultados)
    victorias = sum(cont_resultados[:-1])
    derrotas = cont_resultados[-1]
    porcentaje_vic = victorias/partidas*100
    print(f'{Fore.GREEN}Estadísticas{Style.RESET_ALL}'.center(90),'\n')
    print(f'{Fore.GREEN}Partidas{Style.RESET_ALL}'.rjust(35),end='')
    print(f'{Fore.GREEN}Victorias{Style.RESET_ALL}'.center(37),end='')
    print(f'{Fore.GREEN}Derrotas{Style.RESET_ALL}'.ljust(18))
    print(' '*18,end='')
    print(f'{partidas:^8}',end='')
    print(f'{victorias:^29}',end='')
    print(f'{derrotas:^8}')
    print(f'{Fore.GREEN}% de Victorias{Style.RESET_ALL}'.center(90))
    print(f'{porcentaje_vic:>42.1f} %','\n'*2)
    print(('-'*(6*len(cont_resultados)+2)).center(80))
    for i in range(11):
        print(' '*int((80-6*len(cont_resultados))/2-1) + '|',end='')
        for resultado in cont_resultados:
            if (11-i)>resultado/partidas*10 and (10-i)<=resultado/partidas*10:
                print(f'{resultado/partidas*100:5.1f}%',end='')
            elif (10-i)>resultado/partidas*10:
                print('      ',end='')
            else:
                print('  |*| ',end='')
        print('|')
    print(' '*int((80-6*len(cont_resultados))/2-1) + '|   ',end='')
    for i in range(len(cont_resultados)-1):
          print(i+1,' '*4,end='')
    print('X  |')
    print(('-'*(6*len(cont_resultados)+2)).center(80))
        
def imprimir_matriz(matriz,f,c,colores):
    '''Funcion que recibe como parametros la matriz, fila y columna inicial, y el diccionario con los colores e imprime la matriz de manera recursiva'''
    if f==len(matriz)-1 and c==len(matriz[f])-1:
        imprimir_letra(matriz,f,c,colores)
        print()
        return
    if c<len(matriz[f]):
        imprimir_letra(matriz,f,c,colores)
        imprimir_matriz(matriz,f,c+1,colores)
    else:
        print('\n\t',end='')
        imprimir_matriz(matriz,f+1,0,colores)

def imprimir_letra(matriz,f,c,colores):
    '''Funcion que recibe como parametro el diccionario, la fila, la columna y la matriz e imprime la letra en el color correspondiente'''#lo tenia que poner dos veces en la funcion imprimir_matriz sin esta funcion.
    if colores[f][c]=='verde':
        print(f'{Fore.GREEN}{matriz[f][c]}{Style.RESET_ALL}',end=' ')
    if colores[f][c]=='negro':
        print(f'{Fore.BLACK}{matriz[f][c]}{Style.RESET_ALL}',end=' ')
    if colores[f][c]=='amarillo':
        print(f'{Fore.YELLOW}{matriz[f][c]}{Style.RESET_ALL}',end=' ')

def imprimir_menu():
    '''La función imprime el menú principal del juego y da opciones al jugador'''
    print('\n'*20)
    print(f'{Fore.RED}██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗'.center(84))
    print(f'██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝'.center(80))
    print(f'██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  '.center(80))
    print(f'██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  '.center(80))
    print(f'╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗'.center(80))
    print(f' ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝{Style.RESET_ALL}'.center(84))
    print()
    
    print(' '*30,f'{Fore.CYAN}Elige una opción:')
    print(' '*30,'1- Jugar')
    print(' '*30,'2- Instrucciones')
    print(' '*30,'3- Resultados')
    print(' '*30,f'4- Salir{Style.RESET_ALL}')
    


#Programa principal
from colorama import Fore, Style
import random
jugar = 0
while jugar != 4:
    jugar = imprimir_menu()
    while True:
        try:
            jugar = int(input())
            assert 0 < jugar < 5
            break
        except (ValueError,AssertionError):
            print('No hemos entendido su ingreso.')
            print('Intente nuevamente.')
    if jugar == 1:
        diccionario_colores={}
        matriz_palabras=[]
        contador_de_intentos = 0
        numero_intentos = 6
        palabra_a_adivinar = palabra_aleatoria()
        while contador_de_intentos != numero_intentos:
            contador_de_intentos+=1
            matriz_palabras.append([])
            palabra_a_limpiar = input("Ingrese una palabra de 5 letras:")
            palabra_sintilde=sacar_tilde(palabra_a_limpiar)
            palabra_a_comparar=formato_palabra(palabra_sintilde)
            es_valida = palabra_esta_en_listado(palabra_a_comparar)
            while not es_valida:
                print("La palabra ingresada no es válida o no forma parte del juego.")
                palabra_a_limpiar = input("Ingrese otra palabra de 5 letras:")
                palabra_sintilde=sacar_tilde(palabra_a_limpiar)
                palabra_a_comparar=formato_palabra(palabra_sintilde)
                es_valida = palabra_esta_en_listado(palabra_a_comparar)
            lista=[]
            for letra in palabra_a_comparar:
                lista.append(letra)
            matriz_palabras[contador_de_intentos-1]=lista
            diccionario_colores[contador_de_intentos-1]=comparar_palabra(palabra_a_adivinar, palabra_a_comparar)
            print()
            print('\t',end='')
            imprimir_matriz(matriz_palabras,0,0,diccionario_colores)
            print()
            if palabra_a_comparar==palabra_a_adivinar:
                print('ENHORABUENA. HAS ADIVINADO LA PALABRA EN: %d INTENTO(s)\n' %contador_de_intentos)
                guardar_resultado(contador_de_intentos)
                break
            if contador_de_intentos==6:
                print('NO HAS ADIVINADO LA PALABRA')
                print('GAME OVER')
                print('La palabra era:', palabra_a_adivinar)
                print()
                guardar_resultado(7)
            else:
                print(f'Cantidad de intentos restantes: {numero_intentos-contador_de_intentos}\n')
        input('Presione Enter para proceder a ver las estadisticas')
        estadisticas()
        input('Presione Enter para volver al menu principal')
    elif jugar == 2:
        imprimir_reglas_del_juego()
        input('Presione Enter para volver al menu principal')
    elif jugar == 3:
        estadisticas()
        input('Presione Enter para volver al menu principal')


        
        
    



