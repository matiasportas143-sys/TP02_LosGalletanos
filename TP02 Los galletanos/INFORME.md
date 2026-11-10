# Informe - TP02 Programación I

**Grupo:** Los Galletanos
**Integrantes:** [Matias Portas, Guiliano Coraglio, Valentin Figueroa, Matias Oberto]

## 1. Diseño Top-Down aplicado

Partimos del problema general, "ejecutar cualquier misión en el robot", y lo dividimos en funciones chicas, cada una con una sola responsabilidad. `main()` conecta el robot y llama a las demás. `ejecutar_mision()` recorre la lista de comandos con un `for`. Por cada comando usa `comando_es_valido()`, que decide si se puede ejecutar y devuelve True o False, y `ejecutar_comando()`, que lo ejecuta en el robot y devuelve un texto con lo que pasó. Al final, `generar_reporte()` cuenta los ejecutados y los rechazados y muestra el motivo de cada rechazo. Gracias a esta división, un comando inválido se registra y la misión sigue sin cortarse.

Nota: el esquema (`esquema_top_down.png`) se reconstruyó a partir del código final, no se dibujó antes de programar.

## 2. Pasaje por valor y por referencia

`historial` es una lista, que es un objeto mutable. Cuando `ejecutar_mision()` hace `historial.append(...)`, modifica la misma lista que creó `main()`, no una copia. Por eso la función no necesita devolverla con `return`: cuando termina, `main()` ya la tiene completa y se la pasa a `generar_reporte()`. Eso es pasaje por referencia.

En cambio, `velocidad` y `tiempo` son números. Cuando se los pasamos a `robot.avanzar(...)`, la función recibe el valor, y lo que haga adentro no cambia las variables de afuera. Eso es pasaje por valor.

## 3. ¿Qué tuvimos que cambiar para ejecutar nuestra propia misión?

Ninguna función. Solo agregamos la lista `MISION_PROPIA` al final de `misiones.py`, la importamos en el programa y cambiamos el nombre de la misión en el `main()`. El programa procesó los 6 comandos y dio 5 ejecutados y 1 rechazado, el comando con tiempo negativo.

El único cambio en una función fue en `generar_reporte()`. Con `MISION_CON_ERRORES` vimos que contaba como ejecutados los comandos que rechazaba el robot con `ErrorDeSeguridad`, porque solo buscaba la palabra "rechazado". Lo corregimos para que cuente también los textos que empiezan con "Error".