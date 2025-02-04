import os
import subprocess

# Definir el entorno virtual (si lo usas)
venv_path = os.path.join(os.getcwd(), "venv")

# Activar el entorno virtual (solo si existe)
if os.path.exists(venv_path):
    activate_script = os.path.join(venv_path, "Scripts", "activate")
    subprocess.call(activate_script, shell=True)

# Ejecutar el script principal
print("Iniciando el sistema de certificados...")
subprocess.run(["python", r".\src\window.py"])
