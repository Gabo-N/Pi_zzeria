#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify, render_template
#from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------



app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

#--------------------------------------------------------------------
class Catalogo:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            categoria INT)
                            ''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        
    #----------------------------------------------------------------
    def agregar_producto(self, codigo, descripcion, cantidad, precio, categoria):
        # Verificamos si ya existe un producto con el mismo código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        producto_existe = self.cursor.fetchone()
        if producto_existe:
            return False

        sql = "INSERT INTO productos (codigo, descripcion, cantidad, precio, categoria) VALUES (%s, %s, %s, %s, %s)"
        valores = (codigo, descripcion, cantidad, precio, categoria)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return True

    #----------------------------------------------------------------
    def consultar_producto(self, codigo):
        # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    #----------------------------------------------------------------
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria):
        sql = "UPDATE productos SET descripcion = %s, cantidad = %s, precio = %s, categoria = %s WHERE codigo = %s"
        valores = (nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def listar_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall()
        return productos

    #----------------------------------------------------------------
    def eliminar_producto(self, codigo):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_producto(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Categoría..: {producto['categoria']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")



#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
catalogo = Catalogo(host='localhost', user='root', password='', database='pi_zzeria')

catalogo.agregar_producto(101, "Pizza grande Muzzarella", 40, 6700, 1)
catalogo.agregar_producto(102, "Pizza grande Anchoas", 8, 7100, 1)
catalogo.agregar_producto(103, "Pizza grande Fugazza", 12, 4400, 1)
catalogo.agregar_producto(104, "Pizza grande Fugazzeta", 12, 8800, 1)
catalogo.agregar_producto(105, "Pizza grande Jamón", 12, 9000, 1)
catalogo.agregar_producto(106, "Pizza grande Jamón y morrones", 12, 10500, 1)
catalogo.agregar_producto(107, "Pizza grande Napolitana", 12, 10100, 1)
catalogo.agregar_producto(108, "Pizza grande Calabresa", 12, 11300, 1)
catalogo.agregar_producto(109, "Pizza grande Roquefort", 12, 11400, 1)
catalogo.agregar_producto(110, "Pizza grande Fugazzeta al roquefort", 12, 11400, 1)
catalogo.agregar_producto(111, "Pizza grande Provolone", 12, 11200, 1)
catalogo.agregar_producto(112, "Pizza grande Salvattore", 12, 12100, 1)
catalogo.agregar_producto(113, "Pizza grande Cuatro quesos", 12, 11300, 1)
catalogo.agregar_producto(114, "Pizza grande El capricho del pizzero", 8, 14400, 1)
catalogo.agregar_producto(115, "Pizza grande Rúcula", 12, 9000, 1)
catalogo.agregar_producto(116, "Pizza grande Espinaca", 8, 9000, 1)

catalogo.agregar_producto(201, "Sour Ale", 30, 4400, 2)
catalogo.agregar_producto(202, "Imperial Stout", 30, 4400, 2)
catalogo.agregar_producto(203, "Sweet Stout", 30, 4400, 2)
catalogo.agregar_producto(204, "American Pale Ale", 30, 4400, 2)
catalogo.agregar_producto(205, "Irish Pale Ale", 30, 4400, 2)
catalogo.agregar_producto(206, "Pilsener", 30, 4400, 2)
catalogo.agregar_producto(207, "Lager", 30, 4400, 2)
catalogo.agregar_producto(208, "Porter", 30, 4400, 2)
catalogo.agregar_producto(209, "Golden Lager", 30, 4400, 2)
catalogo.agregar_producto(210, "Brown Ale", 30, 4400, 2)
catalogo.agregar_producto(211, "Bock", 30, 4400, 2)
catalogo.agregar_producto(212, "Gin Martini", 20, 4400, 2)
catalogo.agregar_producto(213, "Sex on the Beach", 20, 4400, 2)
catalogo.agregar_producto(214, "Bloody Mary", 20, 4400, 2)
catalogo.agregar_producto(215, "Piña colada", 20, 4400, 2)
catalogo.agregar_producto(216, "Margarita", 20, 4400, 2)
catalogo.agregar_producto(217, "Mojito", 20, 4400, 2)
catalogo.agregar_producto(218, "Caipirinha", 20, 4400, 2)
catalogo.agregar_producto(219, "Martini expreso", 20, 4400, 2)
catalogo.agregar_producto(220, "Martini francés", 20, 4400, 2)
catalogo.agregar_producto(221, "San Francisco", 20, 4400, 2)
catalogo.agregar_producto(222, "Cosmopolitan", 20, 4400, 2)
catalogo.agregar_producto(223, "Agua fresca", 40, 2200, 2)
catalogo.agregar_producto(224, "Gaseosa", 200, 1200, 2)
catalogo.agregar_producto(225, "Copa de vino de la casa", 100, 1800, 2)
catalogo.agregar_producto(226, "Agua mineral envasada 500 ml", 200, 1200, 2)
catalogo.agregar_producto(227, "Agua saborizada envasada 500 ml", 200, 1200, 2)
catalogo.agregar_producto(228, "Licuado de banana con leche", 30, 2100, 2)

catalogo.agregar_producto(301, "Torta Sacher", 20, 3000, 3)
catalogo.agregar_producto(302, "Torta de naranja", 20, 2600, 3)
catalogo.agregar_producto(303, "Flan casero", 40, 2000, 3)
catalogo.agregar_producto(304, "Budín de pan", 40, 2000, 3)
catalogo.agregar_producto(305, "Sopa inglesa", 20, 1900, 3)
catalogo.agregar_producto(306, "Postre Balcarce", 20, 2600, 3)
catalogo.agregar_producto(307, "Crema helada", 60, 2000, 3)
catalogo.agregar_producto(308, "Profiteroles", 20, 2600, 3)
catalogo.agregar_producto(309, "Tiramisú", 20, 2600, 3)
catalogo.agregar_producto(310, "Mousse de limón con maracuyá", 20, 2600, 3)
catalogo.agregar_producto(311, "Torta Rogel", 20, 2600, 3)
catalogo.agregar_producto(312, "Brownie", 100, 800, 3)
catalogo.agregar_producto(313, "Dona", 100, 800, 3)
catalogo.agregar_producto(314, "Cupcake", 40, 1100, 3)

catalogo.agregar_producto(401, "Té", 60, 800, 4)
catalogo.agregar_producto(402, "Café", 100, 900, 4)
catalogo.agregar_producto(403, "Cortado", 60, 1100, 4)
catalogo.agregar_producto(404, "Café con leche", 60, 1300, 4)
catalogo.agregar_producto(405, "Café largo", 60, 1400, 4)
catalogo.agregar_producto(406, "Capuccino", 60, 1400, 4)
catalogo.agregar_producto(407, "Submarino", 60, 1500, 4)
catalogo.agregar_producto(408, "Medialuna", 300, 400, 4)


# Carpeta para guardar las imagenes.
# ruta_destino = './static/imagenes/'



#--------------------------------------------------------------------
#fetch("www.misitio.com.ar/productos")
@app.route("/productos", methods=["GET"])
def listar_productos():
    productos = catalogo.listar_productos()
    return jsonify(productos)

#--------------------------------------------------------------------
@app.route("/productos/<int:codigo>", methods=["GET"])
def mostrar_producto(codigo):
    producto = catalogo.consultar_producto(codigo)
    if producto:
        return jsonify(producto), 201
    else:
        return "Producto no encontrado", 403

#--------------------------------------------------------------------

@app.route("/productos", methods=["POST"])
def agregar_producto():
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    cantidad = request.form['cantidad']
    precio = request.form['precio']
    categoria = request.form['categoria']  
    # imagen = request.files['imagen']
    # nombre_imagen = secure_filename(imagen.filename)
    # print("*"*20)
    # print(nombre_imagen)
    # print("*"*20)
    # nombre_base, extension = os.path.splitext(nombre_imagen)
    # nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    # imagen.save(os.path.join(ruta_destino, nombre_imagen))

    if catalogo.agregar_producto(codigo, descripcion, cantidad, precio, categoria):
        return jsonify({"mensaje": "Producto agregado"}), 201
    else:
        return jsonify({"mensaje": "Producto ya existe"}), 400

#--------------------------------------------------------------------

@app.route("/productos/<int:codigo>", methods=["PUT"])
def modificar_producto(codigo):
    # Procesamiento de la imagen
    # imagen = request.files['imagen']
    # nombre_imagen = secure_filename(imagen.filename)
    # print("*"*20)
    # print(nombre_imagen)
    # print("*"*20)
    # nombre_base, extension = os.path.splitext(nombre_imagen)
    # nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    # imagen.save(os.path.join(ruta_destino, nombre_imagen))

    # Datos del producto
    data = request.form
    nueva_descripcion = data.get("descripcion")
    nueva_cantidad = data.get("cantidad")
    nuevo_precio = data.get("precio")
    nueva_categoria = data.get("categoria")

    # Actualización del producto
    if catalogo.modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_categoria):
        return jsonify({"mensaje": "Producto modificado"}), 200
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404


#--------------------------------------------------------------------

@app.route("/productos/<int:codigo>", methods=["DELETE"])
def eliminar_producto(codigo):
    # Primero, obtén la información del producto para encontrar la imagen
    producto = catalogo.consultar_producto(codigo)
    if producto:
        # Eliminar la imagen asociada si existe
        # ruta_imagen = os.path.join(ruta_destino, producto['imagen_url'])
        # if os.path.exists(ruta_imagen):
        #     os.remove(ruta_imagen)

        # Luego, elimina el producto del catálogo
        if catalogo.eliminar_producto(codigo):
            return jsonify({"mensaje": "Producto eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el producto"}), 500
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404
#--------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)