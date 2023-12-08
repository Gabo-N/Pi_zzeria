const URL = "GaboN.pythonanywhere.com/"

const app = Vue.createApp({
    data() {
        return {
            codigo: '',
            descripcion: '',
            cantidad: '',
            precio: '',
            categoria: '',
            mostrarDatosProducto: false,
        };
    },
    methods: {
        obtenerProducto() {
            fetch(URL + 'productos/' + this.codigo)
                .then(response => response.json())
                .then(data => {
                    this.descripcion = data.descripcion;
                    this.cantidad = data.cantidad;
                    this.precio = data.precio;
                    this.categoria = data.categoria;
                    this.mostrarDatosProducto = true;
                })
                .catch(error => console.error('Error:', error));
        },
        guardarCambios() {
            const formData = new FormData();
            formData.append('codigo', this.codigo);
            formData.append('descripcion', this.descripcion);
            formData.append('cantidad', this.cantidad);
            formData.append('categoria', this.categoria);
            formData.append('precio', this.precio);


            fetch(URL + 'productos/' + this.codigo, {
                method: 'PUT',
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    alert('Producto actualizado correctamente');
                    this.limpiarFormulario();
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error al actualizar el producto');
                });
        },
        limpiarFormulario() {
            this.codigo = '';
            this.descripcion = '';
            this.cantidad = '';
            this.precio = '';
            this.categoria = '';
            this.mostrarDatosProducto = false;
        }
    }
});

app.mount('#app');