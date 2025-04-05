# Wireshark Report IA  

Este proyecto presenta un estudio de caso en el que se utiliza **Wireshark** junto con un **script de Python** que implementa el algoritmo de **K-means** para analizar tráfico de red, identificar patrones de comportamiento y agruparlos en clusters con diferentes clasificaciones.  

## 📌 Características principales  

- **Recolección de datos mediante Wireshark**: Captura y almacenamiento de tráfico de red en un archivo CSV para su posterior análisis.  
- **Procesamiento con K-means**: Implementación de un script en Python que utiliza el algoritmo de clustering **K-means** para agrupar paquetes de red según su similitud.  
- **Generación de informes automatizados**: Creación de un reporte en formato **TXT** que detalla los clusters identificados, incluyendo:  
  - Cantidad de paquetes agrupados.  
  - Intervalos de tiempo de actividad.  
  - Protocolos utilizados.  
  - Descripción del comportamiento detectado.  

## 🚀 Objetivo  

El proyecto busca facilitar el análisis de tráfico de red mediante técnicas de **machine learning**, permitiendo la detección de patrones y comportamientos anómalos o recurrentes en una red.  

## 🔧 Tecnologías utilizadas  

- **Wireshark** (para captura de tráfico).  
- **Python** (procesamiento y análisis de datos).  
- **Scikit-learn** (implementación de K-means).  
- **Pandas** (manejo de datos en CSV).  

## 📂 Estructura del proyecto  

- `data/`: Archivos CSV generados por Wireshark.  
- `scripts/`: Código Python para el procesamiento y clustering.  
- `reports/`: Informes generados en formato TXT.  

Siéntete libre de explorar, contribuir o utilizar este proyecto para tus propios análisis de red. ¡Las sugerencias y mejoras son bienvenidas!  

---  
¡Espero que te sea útil! 🚀
