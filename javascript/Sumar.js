

function verificarRespuestas() {
    // Obtener las respuestas seleccionadas por el usuario
    const respuestaPregunta1 = document.getElementById("pregunta1").value;
    const respuestaPregunta2 = document.getElementById("pregunta2").value;
    const respuestaPregunta3 = document.getElementById("pregunta3").value;
    const respuestaPregunta4 = document.getElementById("pregunta4").value;
    const respuestaPregunta5 = document.getElementById("pregunta5").value;


    // Calcular la nota
    const nota = parseInt(respuestaPregunta1) + parseInt(respuestaPregunta2) + parseInt(respuestaPregunta3) + parseInt(respuestaPregunta4) + parseInt(respuestaPregunta5);


    // Respuestas correctas
    const respuestasCorrectas = {
        pregunta1: "2",
        pregunta2: "2",
        pregunta3: "2",
        pregunta4: "2",
        pregunta5: "2"
    };


    // Comparar respuestas con las correctas
    let respuestasUsuario = [respuestaPregunta1, respuestaPregunta2, respuestaPregunta3, respuestaPregunta4, respuestaPregunta5];
    let numRespuestasCorrectas = 0;
    let preguntasCorrectas = [];


    for (let i = 0; i < respuestasUsuario.length; i++) {
        if (respuestasUsuario[i] === respuestasCorrectas[`pregunta${i + 1}`]) {
            numRespuestasCorrectas++;
            preguntasCorrectas.push(`Pregunta ${i + 1}`);
        }
    }


    // Mostrar el resultado en la página
    const resultadoElemento = document.getElementById("resultado");
    resultadoElemento.textContent = `Tu nota es: ${nota}/10. Respuestas correctas: ${numRespuestasCorrectas}/5 (${preguntasCorrectas.join(", ")})`;
    const botonVerificar = document.querySelector("button");
    botonVerificar.disabled = true;

    return nota;
}


//import { getClassId } from "./getClassId";
//import { getClassByIdFromNameFile } from "../javascript/getClassId";
var btn = document.getElementById("btn");
var verificar = document.getElementById("verificar");

verificar.addEventListener("click", function(){

    var nota = verificarRespuestas();

    if (nota >= 7) {
        btn.classList.remove("not-active");
        //console.log(getClassByIdFromNameFile());
        const nameFile = window.location.pathname.split("/").pop();
        const numberClass = nameFile.replace("FormClass", ""). replace(".html", "");
        const numeroClase = numberClass.replace("FormClass", "");
        //alert(numeroClase);
        fetch(`/api/datos/guardar-dato?classId=${numeroClase}`)
        .then(response => response.json())
        .then(data => data.estado);
    } else {
        btn.classList.add("not-active");
    }
});

