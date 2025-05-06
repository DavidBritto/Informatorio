# -*- coding: utf-8 -*-
# Archivo de inicio personalizado para el intérprete interactivo de Python
# Guarda este archivo como python_startup.py (o el nombre que prefieras)
# y configura la variable de entorno PYTHONSTARTUP para apuntar a él.

import sys
import os
import platform
import atexit

# --- Configuración de Colores (Usando códigos de escape ANSI) ---
# Estos códigos funcionan bien en la mayoría de las terminales modernas,
# incluyendo Windows Terminal y PowerShell/CMD más recientes.
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Colores de texto (Foreground)
FG_BLACK = "\033[30m"
FG_RED = "\033[31m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"
FG_BLUE = "\033[34m"
FG_MAGENTA = "\033[35m"
FG_CYAN = "\033[36m"
FG_WHITE = "\033[37m"
FG_BRIGHT_BLACK = "\033[90m"
FG_BRIGHT_RED = "\033[91m"
FG_BRIGHT_GREEN = "\033[92m"
FG_BRIGHT_YELLOW = "\033[93m"
FG_BRIGHT_BLUE = "\033[94m"
FG_BRIGHT_MAGENTA = "\033[95m"
FG_BRIGHT_CYAN = "\033[96m"
FG_BRIGHT_WHITE = "\033[97m"

# Colores de fondo (Background) - menos comunes en prompts
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
# ... (puedes añadir más si los necesitas)

# --- Logo de Serpiente ASCII Art ---
# Ajustado para que no sea demasiado grande
snake_logo = rf"""
{FG_BRIGHT_BLUE}       .--._____{RESET}
{FG_BRIGHT_BLUE}     .'   \     \{RESET}
{FG_BRIGHT_BLUE}    /      |    \\{RESET}
{FG_BRIGHT_YELLOW}   |       \   \\{RESET}
{FG_BRIGHT_YELLOW}   \        `---'{RESET}
{FG_BRIGHT_YELLOW}    '._______.'{RESET} {FG_BRIGHT_GREEN}{BOLD}Python Interactivo{RESET}
"""

# --- Mensaje de Bienvenida ---
def display_welcome_message():
    """Muestra el logo y alguna información útil al iniciar."""
    print(snake_logo)
    try:
        python_version = platform.python_version()
        print(f"{DIM}Python {python_version} [{platform.python_implementation()}] en {platform.system()} {platform.release()}{RESET}")
        # Muestra el directorio actual de forma sutil
        cwd = os.getcwd()
        print(f"{FG_CYAN}Directorio actual: {UNDERLINE}{cwd}{RESET}")
    except Exception as e:
        print(f"{FG_BRIGHT_RED}Advertencia: No se pudo obtener toda la información de bienvenida ({e}).{RESET}")
    print("-" * 50) # Separador

# Llama a la función de bienvenida al iniciar
display_welcome_message()

# --- Personalización del Prompt (Indicador) ---
# sys.ps1 es el prompt principal (>>>)
# sys.ps2 es el prompt secundario (...) para bloques de código indentados

# Ejemplo de Prompt: [Py] >>> con colores azul y amarillo
prompt_color_user = FG_BRIGHT_BLUE
prompt_color_symbol = FG_BRIGHT_YELLOW
prompt_secondary_color = FG_BRIGHT_RED

sys.ps1 = f"{prompt_color_user}{BOLD}[Py]{RESET} {prompt_color_symbol}>>> {RESET}"
sys.ps2 = f"{prompt_secondary_color}{BOLD}... {RESET}" # Prompt secundario en rojo

# --- Habilitar historial de comandos entre sesiones (si es posible) ---
# Esto guarda el historial de comandos para que esté disponible la próxima vez.
try:
    import readline
    import rlcompleter
    # Habilita la completación con Tab (puede necesitar 'pyreadline3' en Windows)
    # pip install pyreadline3
    if 'libedit' in readline.__doc__: # Para macOS/BSD
        readline.parse_and_bind("bind ^I rl_complete")
    else: # Para GNU readline (Linux, WSL, y a veces Windows con pyreadline3)
        readline.parse_and_bind("tab: complete")

    # Define dónde guardar el archivo de historial
    histfile_dir = os.environ.get("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
    if not os.path.exists(histfile_dir):
        try: os.makedirs(histfile_dir) # Crea el directorio si no existe
        except OSError: histfile_dir = os.path.expanduser("~") # Falla si no se puede crear, usa home

    histfile = os.path.join(histfile_dir, ".python_history")

    # Intenta cargar el historial existente
    try:
        readline.read_history_file(histfile)
        # Limita el tamaño del historial para que no crezca indefinidamente
        readline.set_history_length(1000)
    except FileNotFoundError:
        pass # No pasa nada si el archivo no existe todavía
    except Exception as e:
        print(f"{FG_BRIGHT_RED}Advertencia: No se pudo cargar el historial: {e}{RESET}")

    # Registra la función para guardar el historial al salir
    atexit.register(readline.write_history_file, histfile)
    print(f"{DIM}Historial de comandos habilitado ({histfile}). Completación con Tab activada.{RESET}")

except ImportError:
    print(f"{FG_YELLOW}Advertencia: Módulo 'readline' no encontrado. El historial y la completación avanzada no estarán disponibles.{RESET}")
    print(f"{FG_YELLOW}En Windows, instala 'pyreadline3': pip install pyreadline3{RESET}")
except Exception as e:
    print(f"{FG_BRIGHT_RED}Error configurando readline/historial: {e}{RESET}")


# --- Imports Útiles (Opcional) ---
# Puedes descomentar o añadir módulos que uses frecuentemente
# print(f"{DIM}Importando módulos comunes...{RESET}")
# try:
#    import math
#    # from collections import Counter, defaultdict # etc.
#    print(f"{FG_GREEN}OK: math importado.{RESET}")
# except ImportError as e:
#    print(f"{FG_YELLOW}Advertencia: No se pudo importar un módulo: {e}{RESET}")


# --- Limpieza (Opcional) ---
# Elimina las variables y funciones globales de este script para no contaminar
# el namespace interactivo.
try:
    del (sys, os, platform, atexit, readline, rlcompleter, histfile, histfile_dir,
         RESET, BOLD, DIM, ITALIC, UNDERLINE, # ... y todos los FG_, BG_
         FG_BLACK, FG_RED, FG_GREEN, FG_YELLOW, FG_BLUE, FG_MAGENTA, FG_CYAN, FG_WHITE,
         FG_BRIGHT_BLACK, FG_BRIGHT_RED, FG_BRIGHT_GREEN, FG_BRIGHT_YELLOW, FG_BRIGHT_BLUE,
         FG_BRIGHT_MAGENTA, FG_BRIGHT_CYAN, FG_BRIGHT_WHITE, BG_BLACK, BG_RED,
         snake_logo, display_welcome_message,
         prompt_color_user, prompt_color_symbol, prompt_secondary_color)
    # Si añadiste imports útiles, también bórralos aquí:
    # del math #, Counter, defaultdict
except NameError:
    pass # Ignora si alguna variable ya no existe (p.ej., readline si no se importó)

print(f"{BOLD}{FG_BRIGHT_GREEN}¡Listo! Entorno interactivo personalizado cargado.{RESET}")