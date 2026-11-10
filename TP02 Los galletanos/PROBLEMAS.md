## Problema N.º 1 — Python no reconocido en la terminal

**Qué se estaba intentando hacer:**
Instalar MuJoCo con pip, que es el paso 3 del orientador.

**Comando ejecutado:**
`py -3 -m pip install mujoco`, y después `python -m pip install mujoco` y `python3 -m pip install mujoco`.

**Resultado esperado:**
Que pip descargara e instalara MuJoCo.

**Resultado obtenido:**
Tres errores distintos según el comando:
- `py`: "no se reconoce como nombre de un cmdlet".
- `python` y `python3`: "Python was not found; run without arguments to install from the Microsoft Store".
- `python`, después de desactivar los alias: "no se reconoce como nombre de un cmdlet".

**Mensaje de error:**
`py : El término 'py' no se reconoce como nombre de un cmdlet, función, archivo de script o programa ejecutable.`
`Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.`

**Interpretación del grupo:**
VS Code detectaba Python 3.14.5 en su panel lateral, pero la terminal no lo encontraba. Es decir, el intérprete existía, pero Windows no sabía dónde buscarlo desde la consola. El mensaje de la Microsoft Store venía de un acceso directo falso (alias de ejecución) que Windows interpone cuando `python` no está en el PATH.

**Hipótesis sobre la causa:**
Python se había instalado sin tildar "Add python.exe to PATH". El `INSTALACION.md` lo advierte como la causa número uno de que "después nada funcione".

**Solución 1 intentada y resultado:**
Desactivar los alias de ejecución de `python.exe` y `python3.exe` en Configuración. Resultado parcial: el mensaje de la Store desapareció, pero el error pasó a ser "python no se reconoce", lo que confirmó que Python no estaba en el PATH.

**Solución 2 intentada y resultado:**
Reinstalar Python 3.14.7 con el instalador clásico de python.org, con "Add python.exe to PATH" tildado. Antes apareció el "Python Install Manager", que no tiene esa casilla, y lo cancelé. Resultado: `python --version` devolvió `Python 3.14.7` y `pip install mujoco` terminó bien (MuJoCo 3.13.0).

**Estado final:** Resuelto.

**Evidencia:** capturas en `evidencias/03_errores/` y `evidencias/04_soluciones/`.
## Problema N.º 2 — Se inició el robot equivocado (G1 en lugar del Go2)

**¿Qué se estaba intentando hacer?**

Iniciar el simulador utilizando el robot Go2.

**Comando ejecutado:**

Se ejecutó `.\INICIAR_SIMULADOR.bat` y se seleccionó la opción 1 del menú.

**Resultado esperado:**

Que se abriera la ventana del simulador mostrando al perro robot Go2.

**Resultado obtenido:**

Se abrió una ventana llamada «g1_29dof scene», en la que aparecía el robot humanoide G1 en lugar del Go2.

**Mensaje de error:**

No apareció ningún mensaje de error. El simulador se inició correctamente, pero con un robot diferente al que necesitábamos.

**Interpretación del grupo:**

Al revisar lo ocurrido, nos dimos cuenta de que el simulador funcionaba correctamente y que el problema estaba en la opción seleccionada al iniciarlo. Habíamos elegido un robot distinto al que necesitábamos utilizar.

**Hipótesis sobre la causa:**

Identificamos que la opción 1 correspondía al robot G1, mientras que la opción 2 permitía iniciar el Go2.

**Solución 1 intentada y resultado:**

Cerramos el simulador y volvimos a ejecutar el archivo de inicio. Esta vez seleccionamos la opción 2 y se abrió correctamente la ventana con el robot Go2.

**Solución 2 intentada y resultado:**

No fue necesario aplicar una segunda solución, ya que con el cambio de opción se resolvió el problema.

**Estado final:** Resuelto.

**Evidencia:** Capturas de pantalla del simulador mostrando el robot G1 y, posteriormente, el Go2.

---

## Problema N.º 3 — El simulador se cerraba durante la ejecución del programa

**¿Qué se estaba intentando hacer?**

Ejecutar nuestro programa y lograr que se conectara correctamente con el simulador del robot.

**Comando ejecutado:**

Se ejecutó `.\EJECUTAR_MI_CODIGO.bat` desde la misma terminal en la que se estaba ejecutando el simulador.

**Resultado esperado:**

Que el programa pudiera establecer la conexión con el simulador y comenzar a ejecutarse normalmente.

**Resultado obtenido:**

El programa no logró conectarse y mostró el error `NoHaySimulador`, acompañado del mensaje «Simulador cerrado».

**Mensaje de error:**

`sim.robot.NoHaySimulador: No encuentro el simulador.`

**Interpretación del grupo:**

A partir de lo ocurrido, entendimos que el simulador debía mantenerse abierto en su propia terminal, mientras que nuestro programa tenía que ejecutarse desde otra terminal independiente.

**Hipótesis sobre la causa:**

Consideramos que, al ingresar el comando para ejecutar nuestro programa en la misma terminal del simulador, terminamos interrumpiendo su ejecución y provocando que se cerrara. Por este motivo, el programa no encontraba el simulador al intentar establecer la conexión.

**Solución 1 intentada y resultado:**

Decidimos utilizar dos terminales separadas: una para mantener el simulador abierto y otra para ejecutar nuestro código. Además, evitamos ingresar comandos en la terminal del simulador una vez iniciado.

Con este cambio, el programa logró conectarse correctamente y funcionar sin inconvenientes.

**Solución 2 intentada y resultado:**

No fue necesario implementar una segunda solución, ya que la separación de las terminales resolvió el problema.

**Estado final:** Resuelto.

**Evidencia:** Capturas de pantalla donde se observa el error inicial y, posteriormente, la conexión exitosa con el simulador.

---

## Problema N.º 4 — Errores en la estructura del archivo mi_tp02.py

**¿Qué se estaba intentando hacer?**

Realizar una primera ejecución del programa para comprobar que el código estuviera correctamente estructurado y funcionara como se esperaba.

**Comando ejecutado:**

Antes de ejecutar el programa, realizamos una revisión del archivo `mi_tp02.py` para detectar posibles errores en las funciones.

**Resultado esperado:**

Que las funciones estuvieran correctamente definidas y que el programa pudiera ejecutarse sin errores relacionados con la estructura del código.

**Resultado obtenido:**

Durante la revisión encontramos dos problemas. Por un lado, la función `comando_es_valido()` estaba definida dentro de sí misma. Por otro, dentro de la función `ejecutar_comando()` faltaba definir la variable `tipo = comando[0]`, necesaria para continuar con la ejecución.

**Mensaje de error:**

Si se ejecutaba el código con estos errores, podía producirse un `NameError`, debido a que la variable `tipo` no estaba definida dentro de la función correspondiente.

**Interpretación del grupo:**

Al analizar el código, observamos que la definición duplicada de `comando_es_valido()` provocaba que la función externa no tuviera un cuerpo correctamente desarrollado ni un `return` que devolviera el resultado esperado. Como consecuencia, podía terminar devolviendo `None`.

Además, detectamos que la variable `tipo` se utilizaba en `ejecutar_comando()`, pero nunca había sido inicializada dentro de esa función.

**Hipótesis sobre la causa:**

Consideramos que estos errores se produjeron al copiar y organizar el código. Al pegar las funciones, quedó duplicada la definición de `comando_es_valido()` y, al mismo tiempo, omitimos la asignación de la variable `tipo` en `ejecutar_comando()`.

**Solución 1 intentada y resultado:**

Eliminamos la definición duplicada de `comando_es_valido()` y agregamos la línea `tipo = comando[0]` al comienzo de `ejecutar_comando()`.

Después de realizar estas modificaciones, volvimos a revisar el código y ejecutamos el programa. La ejecución se realizó correctamente y los problemas detectados quedaron solucionados.

**Solución 2 intentada y resultado:**

No fue necesario aplicar una segunda solución, ya que las modificaciones realizadas fueron suficientes para corregir los errores.

**Estado final:** Resuelto.

**Evidencia:** Capturas de pantalla del código antes y después de realizar las correcciones.

---

## Problema N.º 5 — El reporte no contaba como rechazados los comandos frenados por el robot

**¿Qué se estaba intentando hacer?**

Ejecutar `MISION_CON_ERRORES` y obtener un reporte que contara todos los comandos inválidos como rechazados.

**Comando ejecutado:**

Se cambió `MISION_BASICA` por `MISION_CON_ERRORES` en el `main()` y se ejecutó `.\EJECUTAR_MI_CODIGO.bat`.

**Resultado esperado:**

7 comandos rechazados, que son los inválidos de la misión.

**Resultado obtenido:**

7 ejecutados y 4 rechazados.

**Mensaje de error:**

No hubo mensaje de error. El programa no se cortó, pero el reporte era incorrecto.

**Interpretación del grupo:**

Tres comandos inválidos (velocidad 0.9, tiempo 50 y giro 3.0) los frenó el robot con `ErrorDeSeguridad`, y no nuestra función `comando_es_valido()`. `ejecutar_comando()` los devolvía como un texto que empieza con "Error:", y `generar_reporte()` los contaba como ejecutados.

**Hipótesis sobre la causa:**

`generar_reporte()` clasificaba los textos buscando solo la palabra "rechazado", que los mensajes del robot no contienen.

**Solución 1 intentada y resultado:**

Se cambió la condición a `if "rechazado" in item or item.startswith("Error"):`. El reporte pasó a dar 4 ejecutados y 7 rechazados, con el motivo de cada uno.

**Solución 2 intentada y resultado:**

No fue necesario.

**Estado final:** Resuelto.

**Evidencia:** Capturas del reporte antes y después del cambio, en `evidencias/06_misiones/`.

