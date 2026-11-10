# Errores de instalación (texto copiado de la terminal en el momento)

No se guardaron capturas de estos errores. Se conserva el texto exacto que mostró la terminal.

## 1. `py` no reconocido
Comando: `py -3 -m pip install mujoco`
Resultado: `py : El término 'py' no se reconoce como nombre de un cmdlet, función, archivo de script o programa ejecutable.`

## 2. Acceso directo de la Microsoft Store
Comandos: `python3 -m pip install mujoco` y `python -m pip install mujoco`
Resultado: `Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.`

## 3. `python` no reconocido (después de desactivar los alias)
Comando: `python -m pip install mujoco`
Resultado: `python : El término 'python' no se reconoce como nombre de un cmdlet, función, archivo de script o programa ejecutable.`