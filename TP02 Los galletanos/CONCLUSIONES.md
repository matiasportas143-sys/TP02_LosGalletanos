# Conclusiones - TP02 Programación I

**Grupo:** Los Galletanos

## Antes de comenzar

**a) ¿Qué herramientas necesita el TP?**
Python 3.10 o superior, la librería MuJoCo (se instala con pip) y un editor de código. En Windows puede hacer falta el Visual C++ Redistributable. No hace falta CycloneDDS ni el SDK oficial de Unitree.

**b) ¿Qué versión de Python se requiere?**
3.10 o cualquier versión más nueva. Usamos la 3.14.7.

**c) ¿Qué componentes ya estaban instalados?**
Python 3.14.5 estaba instalado y VS Code lo detectaba, pero no estaba en el PATH de la terminal. Git estaba instalado (versión 2.54.0). MuJoCo no estaba instalado.

**d) ¿Qué componentes del repositorio oficial de Unitree no son necesarios?**
El SDK oficial (`unitree_sdk2` y `unitree_sdk2_python`) y CycloneDDS. El laboratorio usa Python y MuJoCo con un socket local.

**e) ¿Qué diferencias hay entre el TP en PDF y el repositorio actual?**
Las funciones del repositorio son `comando_es_valido`, `ejecutar_comando`, `ejecutar_mision` y `generar_reporte`, mientras que el PDF usaba `inicializar_robot` y `procesar_comando`. Los movimientos se expresan con velocidad y tiempo (`avanzar(velocidad, tiempo)` y `girar(velocidad, tiempo)`), no con distancia y ángulo. Los límites de la materia son 0.2 m/s, 0.5 rad/s y 10 segundos por orden. El robot rechaza lo que supera esos límites con `ErrorDeSeguridad`. El comando de saludo es `saludar`, no `saludo`.

## Arquitectura del laboratorio

Nuestro programa (`tp02_losgalletanos.py`) llama a métodos como `robot.avanzar(...)`. Esas llamadas pasan por `robot.py`, que funciona como puente y no se modifica. El puente se comunica por un socket local (127.0.0.1) con el gemelo digital, que es MuJoCo con el modelo del Go2. Todo ocurre dentro de la misma computadora.

## Reflexión final

**a) ¿Cuál fue la principal dificultad de instalación?**
Que Python no se reconocía en la terminal. Fue un problema en cadena: `py` no existía, `python` abría un acceso directo a la Microsoft Store, y al desactivarlo el comando seguía sin encontrarse.

**b) ¿Qué error requirió mayor investigación?**
El de Python no reconocido, porque el mensaje cambiaba después de cada intento y había que interpretar cada cambio para entender qué pasaba.

**c) ¿Qué solución resultó efectiva y por qué?**
Reinstalar Python con la casilla "Add python.exe to PATH" tildada. Resolvió la causa real: la terminal no sabía dónde estaba Python.

**d) ¿Qué intento no funcionó y qué aprendimos de él?**
Desactivar los alias de ejecución de la Microsoft Store. Eliminó un mensaje pero el error de fondo seguía. Aprendimos que un error puede ocultar otro y que conviene verificar si el problema cambió, no solo si desapareció el mensaje.

**e) ¿Qué diferencia encontramos entre una guía antigua y la arquitectura actual?**
La guía antigua (el PDF) usaba otra API y otros nombres de función. La arquitectura actual usa un socket local en lugar del SDK de Unitree y movimientos por velocidad y tiempo, igual que el robot real.

**f) ¿Hasta qué nivel logramos avanzar?**
Hasta el nivel 10: reporte final generado. Corrimos `MISION_BASICA`, `MISION_CON_ERRORES`, `MISION_CUADRADO` y una misión propia.

**g) Si tuviéramos que continuar, ¿cuál sería el próximo paso?**
Leer las misiones desde un archivo de texto o JSON, y probar la misión propia en el robot real con supervisión del docente.