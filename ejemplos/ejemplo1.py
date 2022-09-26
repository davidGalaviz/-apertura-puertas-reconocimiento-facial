from deepface import DeepFace

obj = DeepFace.analyze(img_path = "/home/david/Documentos/Git/-apertura-puertas-reconocimiento-facial/deepFace/face2.jpg",actions = ['age', 'gender', 'race', 'emotion'])


print("El resultado de la imagen es: ")
print(obj)
