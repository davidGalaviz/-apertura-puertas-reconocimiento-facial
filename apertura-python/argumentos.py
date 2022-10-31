import argparse

parser = argparse.ArgumentParser()
parser.add_argument("img_src", help="Ruta de la imagen a buscar en la DB")
parser.add_argument("db_path", help="Ruta de la base de datos de caras")
args = parser.parse_args()

ruta = args.img_src  + " " + args.db_path

print(ruta)