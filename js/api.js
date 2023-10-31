function generarCliente() {
  const url = 'https://randomuser.me/api/' // API a leer
  // Utiliza la función fetch para realizar una solicitud GET a la URL de la API.
  fetch(url) 

    // La función then() se encarga de manejar la respuesta de la solicitud.
    .then(datos => datos.json()) // Convierte los datos de la respuesta a formato JSON y retorna una promesa.

    // Cuando se resuelve la promesa anterior, ejecuta esta función de devolución de llamada.
    .then(datos => {     
      
      const fotoCliente = document.getElementById("fotoCliente");
      const nombreCliente = document.getElementById("nombreCliente");
      // Obtiene imagen y nombre del cliente feliz mostrado en la página
      
      // Actualiza el contenido del elemento HTML con el id "fotoCliente".      
      fotoCliente.src = datos.results[0].picture.large;
      // Muestra la imagen obtenida de los datos de la API.


      // Actualiza el contenido del elemento HTML con el id "nombreCliente".
      nombreCliente.innerText = `${datos.results[0].name.first} ${datos.results[0].name.last}`;
      // Muestra el nombre obtenido de los datos de la API.
    })
}

function recomendarProductoAzar(){
  const numeroAzar = Math.floor(Math.random() * 4);
  //Sortea un número entre 4 posibles

  const producto1 = {
    texto: "nuestras pizzas",
    foto: "./imagenes/fotos/card_pizza_500x300_serjan-midili--9LB0GKPF0o-unsplash.jpg"
  }
  const producto2 = {
    texto: "nuestras bebidas",
    foto: "./imagenes/fotos/card_bebida_500x300_bohdan-stocek-vt0O0Av96R4-unsplash.jpg"
  }
  const producto3 = {
    texto: "nuestros postres",
    foto: "./imagenes/fotos/card_postre_500x300_max-nayman-5Qp5JaKHfUo-unsplash.jpg"
  }
  const producto4 = {
    texto: "nuestras empanadas",
    foto: "./imagenes/fotos/card_empanadas_500x300_lucas-oriogun-3uNOYXf6-MI-unsplash.jpg"
  }
  //Define textos y fotos de las recomendaciones posibles
  
  let loteProductos = [producto1, producto2, producto3, producto4];
  //Establece lista ordenada de las recomendaciones
  
  
  const fotoRecomendacion = document.getElementById("fotoRecomendacion");
  const textoRecomendacion = document.getElementById("textoRecomendacion");
  // Obtiene imagen y texto de la recomendación mostrada en la página

  
  fotoRecomendacion.src = loteProductos[numeroAzar].foto;
  textoRecomendacion.innerText = loteProductos[numeroAzar].texto;
  // Asocia el número sorteado con el texto y la imagen de la recomendación a mostrar
}

function verClientesProductos() {
  generarCliente();
  recomendarProductoAzar();
    // Llama a las dos funciones
}