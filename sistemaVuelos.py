# Ruben Alejandro Leon Mendieta


def busqueda(x,l):
    resultados = []
    lcopy = l.copy()
    print('\nNombre de aerolinea - Ciudad de origen - Ciudad de destino - Codigo - Fecha - Hora - Precio - Asientos disponibles')
    for i in l:
        if i.lower() == x.lower():
            resultados.append(i)
    for y in resultados:
        id = lcopy.index(y)
        lcopy[id] = 0
        print('\n',lAerolinea[id],' - ',lOrigen[id],' - ',lDestino[id],' - ',lCodigo[id],' - ',lFecha[id],' - ',lHora[id],' - ',lPrecio[id],' - ',lCantidad[id],'\n\n')
    


def validarDatoNumerico (valor):
    while not (valor.isnumeric() and int(valor)>0):
        #Solo ingresa si el dato no es numérico
        #isnumeric solo valida datos positivos
        print("- El valor ingresado no es numérico: '%s'" % valor)
        valor = input("Por favor ingrese un valor numérico entero mayor que cero: ")
    return int(valor)

def reserva():
    
    print('Para reservar un vuelo debe indicar:\n')
    cod = input('Codigo de vuelo: ')
    cantidadA = input('Cantidad de asientos: ')
    cantidadA = validarDatoNumerico(cantidadA)
    nombre = input('Ingrese su nombre: ')
    if cod in lCodigo:
        id = lCodigo.index(cod)
        print('\nEl valor a cancelar es: ', lPrecio[id]*cantidadA)
        lCantidad[id] -= cantidadA
        input('\n*******\tPrecione enter para continuar\t*******\n\n')

    else: 
        print('Codigo incorrecto')
        input('\n*******\tPrecione enter para continuar\t*******\n\n')

# iniciamos el sistema
input('\n*******\tPrecione enter para inciar el sistema\t*******')

# iniciamos nuestra base de datos de usuarios y contraseñas
lUPass = ['juanchito-Juan2004', 'arielJ-Ariel2004', 'princes20-Princes20', 'Moulita-Zelda33', 'sheynnis-Camilito2004']

lAerolinea = [
    "Airline", "LATAM", "TAME", "Avianca", "KLM",
    "JetBlue", "American Airlines", "Copa Airlines", "Iberia", "Air France"
]

lOrigen = [
    "Guayaquil", "Quito", "Cuenca", "Guayaquil", "Quito",
    "Cuenca", "Guayaquil", "Quito", "Cuenca", "Guayaquil"
]

lDestino = [
    "Quito", "Cuenca", "Guayaquil", "Cuenca", "Guayaquil",
    "Quito", "Cuenca", "Guayaquil", "Quito", "Cuenca"
]

lCodigo = [
    "AG123", "LA234", "TM345", "AV456", "KL567",
    "JB678", "AA789", "CA890", "IB901", "AF012"
]

lFecha = [
    "2023/06/01", "2023/06/02", "2023/06/03", "2023/06/04", "2023/06/05",
    "2023/06/06", "2023/06/07", "2023/06/08", "2023/06/09", "2023/06/10"
]

lHora = [
    "08:00", "09:00", "10:00", "11:00", "12:00",
    "13:00", "14:00", "15:00", "16:00", "17:00"
]

lPrecio = [
    100, 120, 150, 110, 130,
    140, 160, 115, 125, 135
]

lCantidad = [
    10, 20, 15, 25, 30,
    18, 22, 16, 19, 21
]



# variables iniciales
x = 0
salir = ''

# nuestro sistema
while x < 3:
    U = input("\n\nIngrese el usuario: \n")
    C = input("\nIngrese la contraseña: \n")
    if U + '-' + C in lUPass:
        print('\n\n*******\tBienvenido entro al sistema\t*******\n')
        input('\n*******\tPrecione enter para continuar\t*******\n\n')
        while salir != 'salir':
            print('\n\nMenu principal: \nC: Cambio de Clave\nR: Registrar Vuelo \nB: Buscar Vuelos\nS: Salir')
            
            opcion = input('Ingrese la opcion deseada: ')
            # opcion C cambio de clave
            if opcion == 'C':
                C0 = input('Ingrese la clave actual:\n')
                if C0 == C:
                    V = True
                    R1 = False
                    R2 = False
                    R3 = False
                    Ca = input('\n\nIngrese la clave clave nueva cumpliendo los siguientes parametros:\n*Debe tener almenos 5 caracteres\n*Al menos un caracter en mayusculas\n*Al menos un numero\n\n')
                    #validamos
                    for validacion in Ca:
                        if validacion in '1234567890':
                            R1 = True
                        elif  validacion != validacion.lower():
                            R2 = True
                        elif len(Ca) >= 5:
                            R3 = True
                    if R2 == True and R1== True and R3 == True:
                        lUPass[lUPass.index(U+'-'+C)] = U+'-'+Ca
                        C = Ca
                        input('La contraseña fue cambiada exitosamente\n****Precione enter para regresar al menu principal****')
                    else:
                        input('\nError la contraseña no cumple los parametros\n****Precione enter para regresar al menu principal****\n')  
                else:
                    print('\nLa contraseña no es correcta')
                    input('Precione enter para regresar al menu principal')
            # opccion R registrar vuelo
            elif opcion == 'R':
                cA = True
                N = input('Ingrese el nombre de la aerolinea:\n')
                while cA:
                    cO = input('ingrese la ciudad de origen:\n')
                    # validamos si la ciudad de origen 
                    if cO.lower() == 'guayaquil' or cO.lower() == 'quito' or cO.lower() == 'cuenca':
                        while cA:
                            cD = input('Ingrese la ciudad de destino:\n')
                            # validamos la ciudad de destino
                            if cD.lower() != cO.lower():
                                if cD.lower() == 'guayaquil' or cD.lower() == 'quito' or cD.lower() == 'cuenca':
                                    while cA:
                                        codV = input('Ingrese el codigo de vuelo:\n')
                                        #validamos el codigo que tenga 5 caracteres numericos
                                        if len(codV) == 5:
                                            while cA:
                                                confirmacion = 0
                                                fechV = input('Ingrese la fecha de vuelo:\n')
                                                # validamos la fecha de vuelo
                                                for L in fechV:
                                                    if L in '1234567890':
                                                        confirmacion+=1
                                                if confirmacion == 8 and fechV[4] == '/' and fechV[7] == '/' and int(fechV[5:7]) <= 12 and int(fechV[8:])<= 31 :
                                                    while cA:
                                                        confirmacion = 0
                                                        hD = input('Ingrese la hora de despegue\n')
                                                        # validamos la hora de despegue
                                                        for L2 in hD:
                                                            if L2 == ':':
                                                                confirmacion+=1
                                                            elif L2 in '1234567890':
                                                                confirmacion+=1
                                                        if confirmacion == 5 and hD[2] == ':' and int(hD[:2]) <= 24 and int(hD[3:]) <= 59:
                                                                Cost = input('Ingrese el costo del viaje')
                                                                Cost = validarDatoNumerico(Cost)
                                                                cantA = input('Ingrese la cantidad de asientos disponibles:')
                                                                cantA = validarDatoNumerico(cantA)
                                                                lAerolinea.append(N)
                                                                lOrigen.append(cO.lower().capitalize())
                                                                lDestino.append(cD.lower().capitalize())
                                                                lCodigo.append(codV)
                                                                lFecha.append(fechV)
                                                                lHora.append(hD)
                                                                lPrecio.append(Cost)
                                                                lCantidad.append(cantA)
                                                                cA = False
                                                        else:
                                                            print('Ingrese correctamente los datos con este formato hh:mm')
                                                    else:
                                                        print('Ingrese correctamente los datos con este formato aaaa/mm/dd')
                                        else:
                                            print('Ingrese correctamente el codigo de vuelo debe tener 5 caracteres')
                                        
                                else:
                                                            print('La ciudad destino tiene que ser una de estas (Guayaquil, Quito, Cuenca) intentelo de nuevo')                        
                            elif cD == cO:
                                print('La ciudad de destino no puede ser igual a la ciudad de origen intentelo de nuevo')
                    else:
                        print('La ciudad origen tiene que ser una de estas (Guayaquil, Quito, Cuenca) intentelo de nuevo')                        
            # opcion B buscar vuelos
            elif opcion == 'B':
                salir2 = ''
                while salir2 != 'salir':
                    print('\n\nMenu de busqueda: \nO: Ciudad de Origen\nD: Ciudad de Destino\nF: Fecha \nV: Volver\n')
                    opcion2 = input('Ingrese la opcion deseada: ')
                    # buscamos las ciudades de origen
                    if opcion2 == 'O':
                        llave = 1
                        while llave == 1:
                            seleC = input('Las ciudades de origen son:\nGuyaquil --- Quito --- Cuenca\n')
                            if seleC.lower() == 'guayaquil' or seleC.lower() == 'quito' or seleC.lower() == 'cuenca':
                                busqueda(seleC,lOrigen)
                                reserva()
                                llave = 0
                            else:
                                print('\nEscoja una ciudad disponible')    
                    # buscamos las ciudades de destino
                    elif opcion2 == 'D':
                        llave = 1
                        while llave == 1:
                            seleC = input('Las ciudades de origen son:\nGuyaquil --- Quito --- Cuenca\n')
                            if seleC.lower() == 'guayaquil' or seleC.lower() == 'quito' or seleC.lower() == 'cuenca':
                                busqueda(seleC,lDestino)
                                reserva()
                                llave = 0
                            else:
                                print('\nEscoja una ciudad disponible') 
                    # buscamos las fechas disponibles
                    elif opcion2 == 'F':
                        llave = 1
                        c = ' --- '.join(lFecha)
                        
                        while llave == 1:
                            print('Las fechas de vuelos son: ', c)
                            seleC = input('Seleccione una de las fechas disponibles: ')
                            confirmacion = 0
                            for L in seleC:
                                if L in '1234567890':
                                    confirmacion+=1
                            if confirmacion == 8 and seleC[4] == '/' and seleC[7] == '/' and int(seleC[5:7]) <= 12 and int(seleC[8:])<= 31 :
                                if seleC in lFecha:
                                    busqueda(seleC,lFecha)
                                    reserva()
                                    llave = 0
                                else:
                                    print('Escoja una feha dispobible')
                            else:
                                print('La fecha debe cumplir el formato aaaa/mm/dd\n\n')
                                
                    elif opcion2 == 'V':
                        salir2 = 'salir'
                    
            # opcion S salida del sistema
            elif opcion == 'S':
                x = 4
                print('\n\n*******\tGracias por preferirnos vuelva pronto\t*******\n')
                salir = 'salir'

            else:
                print('\n\n\n******\tLa opcion no es correcta intentelo otra vez\t*******\n\n\n')

    else:
        print('\n\n*******\tUsuario o contraseña incorrecto\t*******')
        x += 1
if x == 3:
    print('\n\n\n*******\tEL SISTEMA A TERMINADO\t*******')
