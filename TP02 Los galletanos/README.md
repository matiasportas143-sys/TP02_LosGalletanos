# TP02 - Programación I: Controlador de misiones (Unitree Go2)

**Equipo:** Los Galletanos
**Comisión:** UADE

## Descripción

Este trabajo consiste en desarrollar un controlador de misiones en Python para el robot Unitree Go2, utilizando su gemelo digital en MuJoCo para realizar las pruebas.

El programa permite recibir una misión compuesta por una lista de comandos, verificar que cada uno sea válido y ejecutar aquellos que cumplan con las condiciones establecidas. En caso de encontrar un comando inválido, lo rechaza e informa el motivo. Finalmente, genera un reporte con los resultados de la misión, indicando cuántos comandos se ejecutaron correctamente y cuántos fueron rechazados.

## Contenido del proyecto

El proyecto está organizado en diferentes archivos y carpetas para facilitar la consulta y el seguimiento del trabajo realizado:

- `BITACORA.md`: contiene el registro de las actividades realizadas, los resultados obtenidos y las dificultades que fueron apareciendo durante el desarrollo.
- `PROBLEMAS.md`: presenta un análisis más detallado de los principales problemas encontrados, las posibles causas y las soluciones aplicadas.
- `CONCLUSIONES.md`: incluye una reflexión final sobre el trabajo y las respuestas correspondientes al cierre de la actividad.
- `codigo/`: contiene el código fuente del controlador de misiones.
- `evidencias/`: reúne las capturas de pantalla tomadas durante las distintas etapas del trabajo, organizadas por carpetas.
- `esquema_top_down.png`: esquema de las funciones del programa (reconstruido a partir del código final)
- `INFORME.md`: informe breve de diseño, pasaje de parámetros y misión propia

## Caracterización del entorno (Etapa 1)

A continuación, se detallan las herramientas y características del entorno utilizadas para desarrollar y ejecutar el trabajo.

| Elemento | Información |
|---|---|
| Sistema operativo | Windows [versión obtenida mediante `systeminfo`] |
| Arquitectura | x64 (según `systeminfo`) |
| Python | 3.14.7 (reinstalado durante el desarrollo del TP, ver Problema N.º 1) |
| pip | 26.2.1 |
| Git | 2.54.0 |
| MuJoCo previamente instalado | No. Se instaló la versión 3.13.0 durante el trabajo. |
| IDE utilizado | Visual Studio Code |
| Método de obtención del material | `git clone https://github.com/tsamaan/UadeRobotLab.git` |

## Misiones probadas

Durante las pruebas se ejecutaron cuatro misiones diferentes para comprobar el funcionamiento del controlador y verificar cómo respondía ante distintos tipos de comandos.

Los resultados obtenidos fueron los siguientes:

- `MISION_BASICA`: 4 comandos ejecutados correctamente y ninguno rechazado.
- `MISION_CON_ERRORES`: 4 comandos ejecutados correctamente y 7 rechazados.
- `MISION_CUADRADO`: 9 comandos ejecutados correctamente y ninguno rechazado.
- `MISION_PROPIA`: 5 comandos ejecutados correctamente y 1 rechazado.

## Nivel máximo alcanzado

**Nivel 10: reporte final generado.**

Se completaron las etapas previstas hasta llegar a la generación del reporte final, verificando el funcionamiento del controlador mediante las distintas misiones de prueba.

## Evidencias

Las capturas de pantalla se organizaron en diferentes carpetas para que sea más sencillo identificar qué se realizó en cada etapa:

- `01_entorno/`: contiene las versiones de Python, pip y Git, junto con la información del sistema operativo.
- `02_instalacion/`: incluye el proceso de clonado del repositorio, la instalación de MuJoCo y las verificaciones del entorno.
- `03_errores/`: reúne las capturas de los problemas que surgieron durante la instalación y ejecución del programa.
- `04_soluciones/`: muestra las soluciones aplicadas, incluida la reinstalación de Python.
- `05_gemelo_digital/`: contiene las capturas del simulador funcionando con el robot Go2.
- `06_misiones/`: incluye los reportes obtenidos durante la ejecución de las cuatro misiones.

## Nota sobre la bitácora

La bitácora fue elaborada una vez finalizada la actividad, utilizando como referencia el historial del trabajo realizado.

Aunque su registro se completó posteriormente, se respetaron los hechos y el orden real en el que ocurrieron las distintas actividades, pruebas y soluciones.