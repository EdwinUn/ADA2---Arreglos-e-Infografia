# Informe Técnico: Optimización de Estructuras de Datos y Rendimiento de Memoria

## 1. Introducción
Este proyecto analiza el impacto de la disposición de datos en arreglos multidimensionales sobre el rendimiento de un sistema. Se simula un entorno académico con **500 alumnos y 6 materias**, comparando dos arquitecturas de almacenamiento distintas para determinar cuál optimiza el uso de los recursos del hardware.



## 2. Descripción del Experimento
Se implementaron dos modelos de datos utilizando la librería `NumPy` en Python:

* **Modelo A (Materia-Alumno):** Estructura de $6 \times 500$. Las materias actúan como filas y los alumnos como columnas.
* **Modelo B (Alumno-Materia):** Estructura de $500 \times 6$. Los alumnos actúan como filas y las materias como columnas.

El objetivo fue medir el tiempo de respuesta en tareas de **recorrido total** y **búsqueda específica** (localización del Alumno 321, Materia 5).

## 3. Análisis de Resultados y Conclusiones

### Eficiencia en el Acceso a Memoria
Los resultados experimentales confirman que el **Modelo B (Alumno-Materia)** presenta un rendimiento superior. Esta diferencia se fundamenta en el principio de **Localidad de Referencia**:

1.  **Localidad Espacial:** En lenguajes orientados a filas (*Row-major order*), el Modelo B permite que los datos de un mismo alumno se almacenen en direcciones físicas contiguas.
2.  **Optimización de Caché:** Al estar los datos juntos, la CPU realiza menos accesos a la memoria RAM, cargando la información directamente en la memoria caché. El Modelo A, por el contrario, genera múltiples *Cache Misses* al realizar saltos de 500 posiciones por cada consulta.



### Escalabilidad y Límites del Sistema
Durante las pruebas de estrés, se determinaron las siguientes conclusiones sobre la escalabilidad:

* **Crecimiento Lineal:** A medida que el volumen de alumnos aumenta a 100,000 o más, la brecha de rendimiento entre ambos modelos se amplía, volviendo al Modelo A inviable para aplicaciones de tiempo real.
* **Restricciones de Hardware:** El intento de procesar volúmenes masivos (ej. $10^{16}$ elementos) resulta en un desbordamiento de memoria (*MemoryError*). Esto se debe a que el tamaño del arreglo supera la capacidad física de la RAM, provocando la interrupción del proceso por el sistema operativo.

## 4. Recomendaciones de Diseño
Para el desarrollo de sistemas de gestión de datos, se recomienda:
* Utilizar estructuras donde los atributos de una misma entidad (Alumno) permanezcan contiguos.
* Priorizar la disposición de "filas para registros" y "columnas para atributos", alineándose con los estándares de la industria y la arquitectura de los procesadores modernos.

---
**Fecha:** Febrero de 2026
  
## Tecnologías Utilizadas
* **Python 3.x**: Lenguaje de programación base para el desarrollo de la lógica.
* **NumPy**: Biblioteca especializada para la creación y manipulación de arreglos multidimensionales de alto rendimiento.
* **Time Profiling**: Módulos nativos de Python para la medición precisa de tiempos en nanosegundos.
* **IA Generativa (Gemini & ChatGPT)**: Herramientas utilizadas para la optimización de algoritmos de búsqueda, análisis de arquitectura de memoria y redacción de la documentación técnica.