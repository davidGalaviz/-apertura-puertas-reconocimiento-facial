from deepface import DeepFace

print("Buscando rostro")

df = DeepFace.find (img_path = "/home/david/Documentos/Git/-apertura-puertas-reconocimiento-facial/deepFace/Elizabeth-olsen.jpg", db_path = "/home/david/Documentos/Git/-apertura-puertas-reconocimiento-facial/deepFace/my_db")
print("Resultado ")
print(df)
print("imagen de mayor similitud")
print(df.identity[0])