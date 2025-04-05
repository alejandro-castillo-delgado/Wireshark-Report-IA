

import datetime

import pandas as pd
from sklearn.cluster import KMeans

# Leer datos de Wireshark
df = pd.read_csv('wireshark.csv')

# Convertir las columnas 'Source', 'Destination', 'Protocol' e 'Info' en variables categóricas
df['Source'] = pd.Categorical(df['Source'])
df['Destination'] = pd.Categorical(df['Destination'])
df['Protocol'] = pd.Categorical(df['Protocol'])
df['Info'] = pd.Categorical(df['Info'])

df = pd.get_dummies(df, columns=['Source', 'Destination','Protocol','Info'])

# Seleccionar las columnas 'Source', 'Destination', 'Protocol', 'Info' y 'Length'
X = df.iloc[:, 1:].values
# Especificar el número de clusters
num_clusters = 6 

# Entrenar el modelo de K-means
kmeans = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=100, n_init=1)
kmeans.fit(X)

# Asignar cada punto de datos a un cluster
df['cluster'] = kmeans.labels_

# Cluster 0 - Tráfico de red sospechoso 
malicious_traffic = df[df['cluster'] == 0]
# Revisar eventos y tomar acciones

# Cluster 1 - Actividad de malware
malware_events = df[df['cluster'] == 1] 
# Revisar eventos y tomar acciones

# Cluster 2 - Accesos no autorizados 
unauthorized_access = df[df['cluster'] == 2]
# Revisar eventos y tomar acciones

# Cluster 3 - Ataques a aplicaciones web
web_app_attacks = df[df['cluster'] == 3] 
# Revisar eventos y tomar acciones

# Cluster 4 - Movimientos laterales
lateral_movement = df[df['cluster'] == 4]  
# Revisar eventos y tomar acciones

# Cluster 5 - Exfiltración y manipulación de datos
data_exfiltration = df[df['cluster'] == 5]  
# Revisar eventos y tomar acciones

# Crear archivo de reporte
reporte = open("reporte.txt", "w")

# Escribir la fecha de creación del reporte
fecha = datetime.datetime.now()
reporte.write("Reporte generado el " + str(fecha) + "\n\n")

# Escribir los datos de cada clúster identificado
reporte.write("Cluster 0 - Tráfico de red sospechoso:\n")
reporte.write(str(malicious_traffic) + "\n\n")

reporte.write("Cluster 1 - Actividad de malware:\n")
reporte.write(str(malware_events) + "\n\n")

reporte.write("Cluster 2 - Accesos no autorizados:\n")
reporte.write(str(unauthorized_access) + "\n\n")

reporte.write("Cluster 3 - Ataques a aplicaciones web:\n")
reporte.write(str(web_app_attacks) + "\n\n")

reporte.write("Cluster 4 - Movimientos laterales:\n")
reporte.write(str(lateral_movement) + "\n\n")

reporte.write("Cluster 5 - Exfiltración y manipulación de datos:\n")
reporte.write(str(data_exfiltration) + "\n\n")

# Cerrar archivo de reporte
reporte.close()