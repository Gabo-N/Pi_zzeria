
const URL = "http://127.0.0.1:5000/"

// Capturamos el evento de envío del formulario
document.getElementById('formulario').addEventListener('submit', function (event) {
    event.preventDefault(); // Evitamos que se envie el form 

    var formData = new FormData();
    formData.append('codigo', document.getElementById('codigo').value);
    formData.append('descripcion', document.getElementById('descripcion').value);
    formData.append('cantidad', document.getElementById('cantidad').value);
    formData.append('precio', document.getElementById('precio').value);
    formData.append('categoria', document.getElementById('categoria').value);
    
    fetch(URL + 'productos', {
        method: 'POST',
        body: formData // Aquí enviamos formData en lugar de JSON
    })
    .then(function (response) {
        if (response.ok) { return response.json(); }
    })
    .then(function (data) {
        alert('Producto agregado correctamente.');
        // Limpiar el formulario para el proximo producto
        document.getElementById('codigo').value = "";
        document.getElementById('descripcion').value = "";
        document.getElementById('cantidad').value = "";
        document.getElementById('precio').value = "";
        document.getElementById('categoria').value = "";
    })
    .catch(function (error) {
        // Mostramos el error, y no limpiamos el form.
        alert('Error al agregar el producto.');
    });
    
})