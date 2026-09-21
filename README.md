# POO - Programación Orientada a Objetos Seguros
**Semestre:** 2  
**Estudiante:** Jeison Coloma  

---------------------

## 📌 Guía de Comandos Básicos de Git

Esta guía documenta los comandos fundamentales de Git para la configuración de usuario, clonación de repositorios y el flujo de trabajo para guardar cambios en GitHub.


---------------------

### 1. Clonar un Repositorio
```bash
git clone url_repo .
```
> **Explicación:** Copia un repositorio remoto existente desde una URL hacia tu equipo local.  
> *Nota:* El punto (`.`) al final indica que los archivos se descargarán directamente en la carpeta actual en la que estás ubicado, en lugar de crear una subcarpeta nueva.


---------------------

### 2. Configurar Identidad de Usuario
```bash
git config --global user.name "nombre_usuario"
git config --global user.email "email_github"
```
> **Explicación:** Define el nombre y el correo electrónico vinculados a tus confirmaciones de cambios (*commits*).  
> La bandera `--global` aplica esta configuración a todos los repositorios localizados en tu máquina.

---

### 3. Verificar la Configuración
```bash
git config --global --list
```
> **Explicación:** Muestra una lista con todas las variables de configuración globales guardadas (como tu usuario y correo) para verificar que la conexión e identidad estén correctamente establecidas.

---

### 4. Preparar Archivos (*Staging*)
```bash
git add .
```
> **Explicación:** Añade todos los archivos modificados o nuevos en el directorio actual al área de preparación (*Staging Area*), indicando a Git que se incluirán en la próxima versión o guardado.

---

### 5. Registrar Cambios (*Commit*)
```bash
git commit -m "comentario"
```
> **Explicación:** Guarda los cambios en el historial del repositorio local. El parámetro `-m` permite añadir un mensaje descriptivo explicativo sobre los cambios realizados.

---

### 6. Subir Cambios a la Nube (*Push*)
```bash
git push origin main
```
> **Explicación:** Envía los *commits* registrados localmente al repositorio remoto (GitHub) en la rama principal (`main`), guardando tu trabajo en la nube.

---

## 🔄 Flujo de Trabajo Resumido

```
1. Modificar archivos ➔ 2. git add . ➔ 3. git commit -m "mensaje" ➔ 4. git push origin main
