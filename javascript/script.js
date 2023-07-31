
const nombre = document.getElementById('intro');
const button = document.getElementById('BtonUp');
const formulario = document.getElementById('form');

formulario.addEventListener('submit', (e) => {
  e.preventDefault();
    if(nombre.value.length < 1){
        alert('Por favor, ingresa tu nombre');
    }
    else{
        formulario.submit(window.location.href = 'index2.html');
    }
});