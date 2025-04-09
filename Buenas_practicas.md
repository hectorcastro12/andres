# Buenas Prácticas en Python y Convencional Commits

## Buenas Prácticas en Python

### 1. Usa Nombres Claros
- **Variables**: Usa nombres descriptivos como `edad`, `nombre_usuario` en lugar de `x`, `y`.
- **Funciones**: Usa verbos que describan la acción, como `calcular_promedio()`, `enviar_mensaje()`.

### 2. Sigue PEP 8
- Usa **4 espacios** para la indentación.
- Escribe **comentarios** y **documentación** usando docstrings.

### 3. Evita Código Redundante
- Si escribes algo varias veces, conviértelo en una **función**.

### 4. Manejo de Errores con Excepciones
- Usa `try`/`except` para manejar errores sin que el programa se detenga.

```python
try:
    numero = int(input("Introduce un número: "))
except ValueError:
    print("¡Error! No es un número válido.")

```

### Tipos de Commit
- 🐛 `fix`: Corregir un bug.
- ✨ `feat`: Añadir una nueva característica.
- 🧹 `chore`: Tareas generales de mantenimiento.
- 📝 `docs`: Actualización de la documentación.
- 🎨 `style`: Cambios en el formato del código (sin cambiar la funcionalidad).
- ⚡ `perf`: Mejoras en el rendimiento.
- 🔧 `build`: Modificaciones relacionadas con el sistema de construcción o dependencias.
- 🔒 `security`: Cambios enfocados en la seguridad.
- ✅ `test`: Añadir o corregir pruebas.
