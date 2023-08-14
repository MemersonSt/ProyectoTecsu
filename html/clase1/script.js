const ejemplos = document.querySelectorAll('.example');
const cajas = document.querySelectorAll('.data-box');

ejemplos.forEach(ejemplo => {
  ejemplo.addEventListener('dragstart', (e) => {
    e.dataTransfer.setData('text/plain', ejemplo.textContent);
  });
});

cajas.forEach(caja => {
  caja.addEventListener('dragover', (e) => {
    e.preventDefault();
  });

  caja.addEventListener('drop', (e) => {
    e.preventDefault();
    const dataArrastrado = e.dataTransfer.getData('text/plain');
    const tipoEsperado = caja.querySelector('h2').textContent.toLowerCase();
    
    if (validarCoincidencia(dataArrastrado, tipoEsperado)) {
      caja.style.backgroundColor = '#27ae60'; // Coincidencia correcta
    } else {
      caja.style.backgroundColor = '#e74c3c'; // Coincidencia incorrecta
    }
  });
});

function validarCoincidencia(datos, tipoEsperado) {
  if (tipoEsperado === 'entero' && /^\d+$/.test(datos)) {
    return true;
  } else if (tipoEsperado === 'flotante' && /^\d+\.\d+$/.test(datos)) {
    return true;
  } else if (tipoEsperado === 'cadena' && /^".*"$/.test(datos)) {
    return true;
  } else if (tipoEsperado === 'booleano' && /^(verdadero|falso)$/.test(datos)) {
    return true;
  }
  return false;
}
