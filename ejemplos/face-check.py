from deepface import DeepFace

result = DeepFace.verify(img1_path = "/home/david/Documentos/Git/-apertura-puertas-reconocimiento-facial/deepFace/chris-evans2.jpg", img2_path = "/home/david/Documentos/Git/-apertura-puertas-reconocimiento-facial/deepFace/chris-evans1.jpg")


print("El resultado es : ")
print(result)
