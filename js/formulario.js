
//Validación del formulario.

function envioFormulario() {


    //VALIDACIÓN DEL NOMBRE.

    if (document.fcontacto.nombre.value.length <= 3) {
        alert("Complete la casilla nombre");
        document.fcontacto.nombre.focus();
        return;
    }


    //VALIDACIÓN DEL APELLIDO.

    if (document.fcontacto.apellido.value.length < 2) {
        alert("Complete la casilla apellido");
        document.fcontacto.apellido.focus();
        return;
    }

    //VALIDACIÓN DE LA EDAD.

    let edad = document.fcontacto.edad.value;

    edad = validarEntero(edad);
    document.fcontacto.edad.value = edad;

    if (edad == "") {
        alert("Complete la casilla edad");
        document.fcontacto.edad.focus();
        return;
    }


    //VALIDACIÓN DEL GÉNERO.

    if (document.fcontacto.genero.selectedIndex == 0) {
        alert("Debe seleccionar un género");
        document.fcontacto.genero.focus();
        return;
    }

    //VALIDACIÓN DEL PAÍS.

    if (document.fcontacto.pais.selectedIndex == 0) {
        alert("Debe seleccionar un país");
        document.fcontacto.pais.focus();
        return;
    }

    //VALIDACIÓN DEL TELEFONO

    let telefono = document.fcontacto.telefono.value;

    telefono = validarEntero(telefono);
    document.fcontacto.telefono.value = telefono;

    if (telefono == "") {
        alert("Debe introducir un numero de teléfono")
        document.fcontacto.telefono.focus();
        return;
    }

    //VALIDACIÓN DE EMAIL.



    if(document.fcontacto.email.value.length == ""){
        alert("Debe completar correctamente el campo email");
        document.fcontacto.email.focus();
        return;
    }else{
        alert("El formulario ha sido enviado. ¡Muchas gracias!")
        document.fcontacto.submit();
        return;
    }




   

}

function validarEntero(valor) {

    valor = parseInt(valor);

    if (isNaN(valor)) {
        return "";
    } else {
        return valor;
    }
}



