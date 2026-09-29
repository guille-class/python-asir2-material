# Puesta en marcha

Pasos para dejar todo listo antes de la primera práctica.

## 1. Cuenta de GitHub

1. Crea una cuenta gratuita en <https://github.com> (si ya tienes una, sirve).
2. Usa un nombre de usuario reconocible (por ejemplo `nombre-apellido`) y **pásaselo al profesor**: con él te dará de alta en la clase.
3. Te llegará un correo de invitación a la organización **guille-class**. Acéptalo (también puedes hacerlo en <https://github.com/orgs/guille-class/invitation>). Sin este paso no funcionan los enlaces de las prácticas.

## 2. Aceptar una práctica

1. Abre el enlace de la práctica que el profesor publica en el aula virtual e inicia sesión con GitHub.
2. Acepta la práctica. Se crea un repositorio privado solo para ti, con el enunciado y los ficheros de partida, llamado `<clase>-<práctica>-<tu-usuario>`.

## 3. Preparar tu ordenador

1. Instala **Python 3.12** desde <https://www.python.org/downloads/> (en Windows marca *Add python.exe to PATH*).
2. Instala **Visual Studio Code** y su extensión **Python**.
3. Instala **Git** desde <https://git-scm.com/downloads>.
4. Configura tu nombre y correo (una sola vez):
   ```bash
   git config --global user.name "Tu Nombre"
   git config --global user.email "tu-correo@ejemplo.com"
   ```
5. Clona tu repositorio de la práctica (botón **Code → HTTPS**, copia la URL):
   ```bash
   git clone https://github.com/guille-class/nombre-de-tu-repo.git
   ```

## 4. Flujo de trabajo en cada práctica

```bash
python fichero.py            # ejecutar un programa
pip install -r requirements.txt   # solo la primera vez
python -m pytest -v          # pasar las comprobaciones automáticas

git add .
git commit -m "Describe lo que has hecho"
git push                     # entregar
```

- Haz *commit* a menudo, cada vez que termines un ejercicio.
- Se revisa la **última versión subida** antes de la fecha de entrega.
- Cada *push* lanza la corrección automática en la pestaña **Actions** de tu repositorio: ✅ todo correcto, ❌ algo falla (entra para ver qué).

## 5. Si algo falla

| Problema | Solución |
|---|---|
| `python` no se reconoce | Reinstala Python marcando *Add to PATH* o usa `py` en Windows |
| `git push` pide usuario y contraseña | Inicia sesión en la ventana que abre VS Code/Git; GitHub ya no acepta la contraseña en la terminal |
| `No module named pytest` | Ejecuta `pip install -r requirements.txt` |
| La comprobación dice que falta una variable | No cambies los nombres de variables y funciones del enunciado |
