
const laodEvents = () => {
    const formulario = document.getElementById('formulario'); //Seleccionar el formulario
    const inputs = formulario.querySelectorAll('input'); //Seleccionar todos los inputs (collecion)

    const elements = Array.from(inputs).map((item) => { //Transforma la coleccion en un arreglo que va mapeando. Porque al seleccionar un elemento por su id es como unico no te devulve una coleccion.

        return { //Devuelve un objeto por cada input del array
            'typeValidation': item.name, //De el nombre que le pusiste a dicho elemento
            'element': item, //El elemento en si
        }
    })

    elements.forEach(arg => { //Recorrer ese arreglo (input parametro)

        switch (arg.typeValidation) { //Si el nombre de ese input que tocaste es:
            case 'numero':

                arg.element.addEventListener('input', (event) => { //Dispara el evento y llama a la funcion de validacion. Para lo campos de numero

                    validateInputNumbers(event)
                })
                break;
            case 'texto':
                arg.element.addEventListener('input', (event) => { //Para los campos de texto
                    validateInputText(event)
                })
                break

            case 'solapin':
                arg.element.addEventListener('input', (event) => { //Para el campo que tenga una e y numeros
                    validateInputSolapin(event)
                })
                break

            default:
                console.log(`input no controlado: ${arg.element.name}`) //Muestra por consola el mensaje y el nombre del campo
                break;
        }
    })

    // Expresiones regulares. Serie de regla que indica que debería aceptar en campo
    const expresiones = {
        usuario: /^[a-z]{4,16}$/, //letras minusculas
        contrasena: /^.{4,12}$/, //4 a 12 digitos
        nombreYapellido: /^\w+\s?\w+?\s?$/,

        carrera: /^[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+$/,
        cantApto: /^(1[0-9]|20|[1-9])$/,
        ano: /^(?:[1-5])$/,
        facultad: /^(facultad [1-4]|Facultad [1,4]|1|2|3|4|CITEC|FTE|\s*)$/,

        numeroEdificio: /^\d{1,3}$/,
        numeroApto: /\d{1,3}[\s-.]\d{1,3}/,
        telefono: /^\d{8}$/,
        correo: /[a-zA-Z0-9._-]+@\w+\.[a-zA-Z]+/,
        solapin: /^E{6}$/,
        buscador: /^(?:\d{3}|E{6})$/
    }

}

//funcion para validar que la entrada sea texto
const validateInputText = (event) => {
    const input = event.target.value; //Obtiene el valor introducido en el campo
    const isText = /^[a-zA-Z]+$/.test(input); //Verifica si ese valor coincide con la expresion regular
    const clases = String(event.target.className);  //Convierte el nombre de la clase del input en string para poder comparar despues

    if (!isText) { //Si no coincide con la expresion regular, en este caso tipo texto

        if (!clases.includes('incorrecto')) { //Y si ese input tampoco tiene la clase incorrecto
            event.target.classList.add('incorrecto') //Entonces se la agrego
        }
        event.target.value = input.replace(/[^a-zA-Z]/g, ''); //Ese valor lo voy a remplazar por un espacio en blanco para que no escriba otros caracteres que no sean texto
    } else { //Si no, osea si coincide con la expresion regular y:

        if (clases.includes('incorrecto')) { //Si contiene la clase incorrecto entonces:
            event.target.classList.remove('incorrecto') //La elimino
        }
    }
}


//funcion para validar que la entrada sean solo numeros
const validateInputNumbers = (event) => {
    const input = event.target.value; //Obtiene el valor introducido en el campo
    const onlyNumbers = /^[0-9]*$/.test(input); //Verifica si ese valor coincide con la expresion regular, que sean solo numeros
    const clases = String(event.target.className) //Convierte el nombre de la clase del input en string para poder comparar despues

    if (!onlyNumbers) { //Si no coincide con la expresion regular, en este caso tipo numero
        if (!clases.includes('incorrecto')) { //Y si ese input tampoco tiene la clase incorrecto
            event.target.classList.add('incorrecto') //Entonces se la agrego
        }
        event.target.value = input.replace(/\D/g, ''); //Ese valor lo voy a remplazar por un espacio en blanco para que no escriba otros caracteres que no sean numericos
    } else { //Si no, osea si coincide con la expresion regular y:

        if (clases.includes('incorrecto')) { //Si contiene la clase incorrecto entonces:
            event.target.classList.remove('incorrecto') //La elimino
        }
    }
}


const validateInputSolapin = (event) => {
    const input = event.target.value; //Obtiene el valor introducido en el campo
    const isSolapin = /^[0-9e]+$/.test(input); //Verifica si ese valor coincide con la expresion regular, que sean solo numeros
    const clases = String(event.target.className) //Convierte el nombre de la clase del input en string para poder comparar despues
    


    if (!isSolapin) { //Si no coincide con la expresion regular, en este caso q se inserte una e y luego numeros
        if (!clases.includes('incorrecto')) { //Y si ese input tampoco tiene la clase incorrecto
            event.target.classList.add('incorrecto') //Entonces se la agrego
        }
        event.target.value = input.replace(/^[0-9e]+$/, ''); //Ese valor lo voy a remplazar por un espacio en blanco para que no escriba otros caracteres que no sean los que quiera
    } else { //Si no, osea si coincide con la expresion regular y:

        if (clases.includes('incorrecto')) { //Si contiene la clase incorrecto entonces:
            event.target.classList.remove('incorrecto') //La elimino
        }
    }
}


window.onload = laodEvents //Renderiza la pagina antes de que se carguen los eventos