# Entregable — Deshacer y rehacer (Deque propia)

**Autor(es):** *[Indique nombres]*  
**Asignatura / fecha:** *[Indique]*  

---

## 1) Descripción breve

### ¿Qué hace el programa?

Es una aplicación de escritorio que simula un **editor con historial de cambios**: el usuario registra acciones (cada una con una descripción y un **nuevo estado** en texto plano), puede **deshacer** y **rehacer** esos cambios, y ver en pantalla el **historial de descripciones** y el **estado actual**. La lógica vive en la clase `UndoRedoSystem`; la interfaz (`ui/tkinter_app.py`) solo muestra datos y llama a esa clase.

### ¿Cómo se utilizó la estructura Deque?

Se implementó una clase **`Deque`** en `app_core/deque.py`, con una **lista interna** y métodos obligatorios: `add_front`, `add_rear`, `remove_front`, `remove_rear`, `is_empty`, `size`. El resto del programa **no sustituye** esta estructura por `collections.deque` ni por otra cola ya hecha para la lógica principal.

En `UndoRedoSystem` se usan **dos instancias de `Deque`**:

- **`_undo_stack`**: guarda las acciones ya aplicadas. La acción más reciente está al **final** (`add_rear` al registrar, `remove_rear` al deshacer).
- **`_redo_stack`**: guarda las acciones deshechas, listas para rehacer (`add_rear` al deshacer, `remove_rear` al rehacer).

Así, cada `Deque` actúa como una **pila (LIFO)** usando solo el extremo trasero para el flujo undo/redo, cumpliendo el requisito de que la estructura central sea la Deque propia.

### ¿Cómo se resolvió undo y redo?

Cada acción es un objeto **`Action`** con: descripción, **estado anterior** y **estado posterior** (copias profundas con `copy.deepcopy`).

- **Registrar acción:** se valida la descripción y el estado; se crea `Action` con el estado actual como `state_before` y el nuevo como `state_after`; se hace `add_rear` en `_undo_stack`; el estado actual pasa a ser el nuevo; se **vacía** `_redo_stack` con `clear()` porque el historial futuro deja de ser válido.
- **Undo:** si `_undo_stack` está vacío, se informa error; si no, `remove_rear` obtiene la última acción, se hace `add_rear` en `_redo_stack`, y el estado actual vuelve a `state_before` de esa acción.
- **Redo:** análogo: si `_redo_stack` está vacío, error; si no, se recupera la acción, se devuelve a `_undo_stack` y el estado pasa a `state_after`.

### ¿Consola o interfaz gráfica?

Se usó **interfaz gráfica con Tkinter** (ventana con campos de texto, botones Registrar / Deshacer / Rehacer y vistas de historial y estado).

### ¿Qué validaciones se implementaron?

- **Deshacer** sin acciones previas: no se modifica el estado; se devuelve `False` y mensaje *"No hay acciones para deshacer."*
- **Rehacer** sin acciones en la pila de redo: `False` y *"No hay acciones para rehacer."*
- **Registrar** con descripción vacía o solo espacios: rechazado con mensaje explícito.
- **Estado no copiable** (fallo en `deepcopy`): registro rechazado con mensaje que incluye la causa.
- Tras una **nueva acción**, la pila de redo se limpia para no dejar un flujo inconsistente.
- En la UI, errores del sistema se muestran en **cuadros de diálogo** y en una **etiqueta de estado**.

---

## 2) Link a video en Google Drive

**Requisitos del video:** duración máxima **3 minutos**, mostrar **código** y **ejecución funcional**, permisos de **lectura** para quien califique.

**Enlace (sustituya por el suyo al subir el video):**

- **Video:** *[PENDIENTE — pegue aquí el enlace compartido de Google Drive con acceso de lector]*

*Instrucción:* en Drive, clic derecho en el archivo → **Obtener enlace** → acceso **Cualquier persona con el enlace** como lector (o el permiso que indique su docente).

---

## 3) Link a repositorio público de GitHub

**Debe incluir:** código fuente, **README** con instrucciones (en la raíz del repo), **pruebas mínimas** en `tests/`.

**Enlace (sustituya tras crear el repositorio y hacer push):**

- **Repositorio:** `https://github.com/decheverriae-prog/deshacer-y-rehacer`  
  *(Nombre del proyecto: **Deshacer y rehacer**; cuenta de GitHub: **decheverriae-prog**. En GitHub el nombre del repo suele ir sin espacios, por ejemplo `deshacer-y-rehacer`. Si al crearlo usó otro nombre, actualice esta URL.)*

---

## Cómo pasar este documento a PDF

1. Abra este archivo en **Visual Studio Code**, **Typora**, **Word** u otro editor.
2. Complete los datos de cabecera y los enlaces de las secciones 2 y 3.
3. Exporte o guarde como **PDF** (por ejemplo: Word → *Guardar como* → PDF; o *Imprimir* → *Microsoft Print to PDF*).

Si usa solo Markdown en la terminal, puede probar [Pandoc](https://pandoc.org/) con un motor LaTeX instalado, por ejemplo: `pandoc INFORME_PDF.md -o informe.pdf`.
