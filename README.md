# Análisis de Complejidad Algorítmica y Notación Big-O: Merge Sort

## Descripción
Este proyecto analiza la eficiencia algorítmica mediante el estudio de la complejidad temporal y espacial con notación asintótica Big-O. Se toma como caso de estudio principal el algoritmo **Merge Sort** (Ordenamiento por Mezcla), implementando el paradigma *Divide y Vencerás* para resolver el problema del ordenamiento de datos a gran escala y demostrando la cota de eficiencia de $O(n \log n)$.

## Dataset
Para realizar la evaluación empírica del algoritmo, se emplean conjuntos de datos numéricos generados dinámicamente mediante simulaciones sintéticas:
- **Fuente:** Generación sintética mediante el módulo nativo `random` de Python.
- **Descripción:** Arreglos de números enteros aleatorios en el rango de $1$ a $1,000,000$. Se evalúan diferentes escalas de entrada con $n = 1,000$, $10,000$, $100,000$ y $500,000$ elementos.

## Tecnologías
- Python
- Librerías utilizadas (`time`, `random`)

## Implementación
El tema abordado se implementó a través de la estructuración de Merge Sort en dos componentes clave:
- **División Recursiva (`merge_sort`):** Fracciona el arreglo de entrada a la mitad de forma recursiva hasta llegar a los casos base ($n \le 1$), generando una profundidad de llamadas de $\log_2 n$.
- **Combinación Lineal (`fusionar`):** Intercala las dos sublistas previamente ordenadas en una lista resultante, con un costo temporal de $O(n)$ por nivel.
- **Análisis de Complejidad:**
  - **Complejidad Temporal:** $T(n) = 2T(n/2) + O(n) \implies O(n \log n)$ (demostrado mediante el Caso 2 del Teorema Maestro).
  - **Complejidad Espacial:** $E(n) = O(n)$ debido a la memoria auxiliar requerida para fusionar los elementos.

## Ejecución
Instrucciones para correr el proyecto:

```bash
python main.py
```

## Resultados
Al evaluar el script de medición empírica con distintos valores de $n$, se observaron los siguientes tiempos de ejecución:

- **$n = 1,000$:** ~0.0035 segundos
- **$n = 10,000$:** ~0.0452 segundos
- **$n = 100,000$:** ~0.6435 segundos
- **$n = 500,000$:** ~3.4582 segundos

**Observación de Resultados:** Los tiempos empíricos confirman que al aumentar la entrada $n$ por un factor de 10, el crecimiento del tiempo no es cuadrático ($O(n^2)$), sino que escala de acuerdo a la curva matemática esperada de $O(n \log n)$.

## Autores
- [Tu Nombre Completo]
