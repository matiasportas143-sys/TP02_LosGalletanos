# =====================================================================
#  TP02 - Programacion I
#  Controlador de misiones
#
#  ESTE ES EL ARCHIVO DONDE ESCRIBIS TU PROGRAMA.
#
#  Antes de ejecutarlo:
#    1. Abri INICIAR_SIMULADOR (elegi G1 o Go2)
#    2. Espera a que aparezca la ventana con el robot
#    3. Recien ahi ejecuta este archivo
#
#  Grupo: Los galletanos
#  Comision: UADE
# =====================================================================

from robot import ErrorDeSeguridad, Robot

from misiones import MISION_BASICA, MISION_CON_ERRORES, MISION_CUADRADO, MISION_PROPIA


# =====================================================================
#  PARTE 1 - Validar un comando
# =====================================================================
def comando_es_valido(comando):
    """Decide si un comando se puede ejecutar. Devuelve True o False.

    Un comando es una tupla. El primer elemento dice que hacer:

        ("avanzar", velocidad, tiempo)    velocidad en m/s, tiempo en s
        ("girar", velocidad, tiempo)      velocidad en rad/s, tiempo en s
        ("detenerse",)
        ("saludar",)

    Cosas que conviene revisar:
      - que la tupla no este vacia
      - que el nombre del comando sea uno de los cuatro validos
      - que tenga la cantidad de datos que corresponde
        (avanzar y girar llevan dos; detenerse y saludar, ninguno)
      - que velocidad y tiempo sean numeros de verdad, no textos
      - que el tiempo no sea negativo
    """
    # TU CODIGO ACA
    if len(comando) == 0:
        return False
    else:
        tipo=comando[0]
        if tipo not in ("avanzar", "girar", "detenerse", "saludar"):
            return False
        if tipo in ("avanzar", "girar"):
            if len(comando) != 3:
                return False
            else:
                if not isinstance(comando[1],(int,float)):
                    return False
                if not isinstance(comando[2],(int,float)):
                    return False
                if comando[2]<0:
                    return False
        else:
            if len(comando) !=1:
                return False
        return True
    

            

# =====================================================================
#  PARTE 2 - Ejecutar un comando
# =====================================================================
def ejecutar_comando(robot, comando):
    """Ejecuta UN comando en el robot. Devuelve un texto con lo que paso.

    Ordenes que podes usar:

        robot.avanzar(velocidad=..., tiempo=...)
        robot.girar(velocidad=..., tiempo=...)
        robot.detenerse()
        robot.saludar()

    Ojo: aunque el comando parezca valido, el robot puede rechazarlo
    igual (por ejemplo, si la velocidad supera el limite de la materia).
    Eso llega como un ErrorDeSeguridad y conviene atraparlo.
    """
    # TU CODIGO ACA
    tipo=comando[0]
    if tipo=="avanzar":
        velocidad=comando[1]
        tiempo=comando[2]
        try:
            robot.avanzar(velocidad=velocidad,tiempo=tiempo)
            return "avanzar ejecutado"
        except ErrorDeSeguridad as error:
            return f"Error: {error}"
    elif tipo=="girar":
        velocidad=comando[1]
        tiempo=comando[2]
        try:
            robot.girar(velocidad=velocidad,tiempo=tiempo)
            return "girar ejecutado"
        except ErrorDeSeguridad as error:
            return f"Error: {error}"
    elif tipo=="detenerse":
        try:
            robot.detenerse()
            return "detenerse ejecutado"
        except ErrorDeSeguridad as error:
            return f"Error: {error}"
    elif tipo=="saludar":
        try:
            robot.saludar()
            return "saludar ejecturado"
        except ErrorDeSeguridad as error:
            return f"Error:{error}"
    
        

            



# =====================================================================
#  PARTE 3 - Recorrer la mision entera
# =====================================================================
def ejecutar_mision(robot, mision, historial):
    """Recorre la lista de comandos, uno por uno.

    Por cada comando:
      - si NO es valido, lo rechaza y sigue con el siguiente
      - si es valido, lo ejecuta
      - en los dos casos, guarda en 'historial' que fue lo que paso

    Un comando invalido NO tiene que cortar la mision.
    """
    # TU CODIGO ACA
    for comando in mision:
        if comando_es_valido(comando):
            resultado=ejecutar_comando(robot,comando)
            historial.append(resultado)
        else:
            historial.append(f"Comando rechazado:{comando}")



# =====================================================================
#  PARTE 4 - El reporte final
# =====================================================================
def generar_reporte(historial):
    """Muestra por pantalla un resumen de la mision.

    Tiene que decir, como minimo:
      - cuantos comandos se ejecutaron bien
      - cuantos se rechazaron
      - cual fue el motivo de cada rechazo
    """
    # TU CODIGO ACA
    ejecutados = 0
    rechazados = 0
    motivos = []

    for item in historial:
        if "rechazado" in item or item.startswith("Error"):
            rechazados += 1
            motivos.append(item)
        else:
            ejecutados += 1

    print("=== REPORTE DE MISION ===")
    print(f"Comandos ejecutados: {ejecutados}")
    print(f"Comandos rechazados: {rechazados}")
    if rechazados > 0:
        print("Motivos de rechazo:")
        for motivo in motivos:
            print(f"  - {motivo}")


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    robot = Robot()
    robot.conectar()

    historial = []

    try:
        # Empeza probando con MISION_BASICA.
        # Cuando funcione, proba con MISION_CON_ERRORES: esa tiene
        # comandos invalidos a proposito.
        ejecutar_mision(robot, MISION_BASICA, historial)
        generar_reporte(historial)
    finally:
        robot.detenerse()
        robot.desconectar()


if __name__ == "__main__":
    main()
