> [!NOTE]
> **Autor:** Juan Jose Perez Garcia  
> **Correo:** j.perez@utp.edu.co  
> **Universidad Tecnológica de Pereira (UTP)**

# Juego del Ahorcado (`mi-web-juan2`)

---

## 📋 Lista de Requerimientos y Tareas (Task List)

- [ ] **Configuración del repositorio y estructura inicial:**
  - [ ] Crear el repositorio público en GitHub con el nombre `mi-web-juan2`.
  - [ ] Crear el archivo `README.md` inicial con los datos del autor y este listado de tareas en formato *task list*.
  - [ ] Estructurar los tres archivos principales del proyecto: programa principal, archivo de palabras y archivo del monigote.

- [ ] **Módulo de palabras (`palabras.py` o similar):**
  - [ ] Definir una lista de palabras ocultas predefinidas.
  - [ ] Implementar la lógica para seleccionar una palabra de manera aleatoria.

- [ ] **Módulo de representación gráfica (`monigote.py` o similar):**
  - [ ] Diseñar y almacenar las 6 etapas de representación en símbolos del monigote del ahorcado según los errores.

- [ ] **Lógica principal del juego (`main.py`):**
  - [ ] Inicializar la palabra oculta reemplazando cada carácter por un guión bajo (`_`).
  - [ ] Solicitar al usuario que ingrese una letra por consola.
  - [ ] Validar que la entrada sea **estrictamente una sola letra** (controlando errores si ingresan números o cadenas vacías/largas).
  - [ ] Validar que la letra esté contenida en el rango `[A-Z]` (manejando mayúsculas/minúsculas).
  - [ ] Validar que la letra **no se haya utilizado previamente** (control de letras repetidas).
  - [ ] Verificar si la letra existe en la palabra oculta:
    - [ ] Si existe una o varias veces, reemplazar los guiones bajos correspondientes en la posición exacta.
    - [ ] Si no existe, restar una vida (de un total de 6), mostrar el contador de vidas actual y actualizar la representación gráfica del monigote.
  - [ ] Controlar la condición de derrota: si las vidas llegan a 0, mostrar el monigote final, el mensaje de derrota y revelar la palabra oculta.
  - [ ] Controlar la condición de victoria: si se adivinan todas las letras, mostrar el mensaje de victoria.
  - [ ] Implementar el menú de fin de partida que pregunte al jugador si desea finalizar el programa o jugar de nuevo.

- [ ] **Control de versiones y entregas parciales:**
  - [ ] Realizar commits y *pushes* parciales a medida que se vayan solucionando o implementando los requerimientos (evitar un repositorio con un solo commit).

---

## ⚙️ Instrucciones de Ejecución

1. Asegúrate de tener instalado **Python** en tu equipo.
2. Clona el repositorio o descarga los archivos fuente en un mismo directorio de trabajo (`mi-web-juan2`).
3. Abre tu terminal o entorno de desarrollo (como Visual Studio Code) en la carpeta del proyecto.
4. Ejecuta el archivo principal con el siguiente comando:
   ```bash
   python main.py