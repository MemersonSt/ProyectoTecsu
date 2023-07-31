// Espera a que el documento HTML esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
  // Obtén la imagen y el contenedor
  const movableImage = document.getElementById("movable-image");
  const movableImage2 = document.getElementById("movable-image");
  const movableImage3 = document.getElementById("movable-image");
  const container = document.getElementById("container");

  // Variables para almacenar la posición inicial del mouse y la imagen
  let offsetX, offsetY;

  // Cuando se presiona el mouse sobre la imagen, se activa el evento "mousedown"
  movableImage.addEventListener("mousedown", function(e) {
    // Obtén la posición inicial del mouse en relación con la imagen
    offsetX = e.clientX - movableImage.getBoundingClientRect().left;
    offsetY = e.clientY - movableImage.getBoundingClientRect().top;

    // Cambia el cursor a "grabbing" durante el arrastre
    movableImage.style.cursor = "grabbing";

    // Agrega un evento para que la imagen siga el mouse durante el movimiento
    document.addEventListener("mousemove", moveImage);
  });

  // Cuando se suelta el mouse, se activa el evento "mouseup"
  document.addEventListener("mouseup", function() {
    // Restaura el cursor a "grab" después de soltar el mouse
    movableImage.style.cursor = "grab";

    // Elimina el evento de movimiento para detener el arrastre
    document.removeEventListener("mousemove", moveImage);
  });

  // Función para mover la imagen según la posición del mouse
  function moveImage(e) {
    // Calcula las coordenadas donde debe estar la imagen en relación con el contenedor
    let posX = e.clientX - offsetX - container.getBoundingClientRect().left;
    let posY = e.clientY - offsetY - container.getBoundingClientRect().top;

    // Limita la posición para que la imagen no se salga del contenedor
    posX = Math.min(Math.max(posX, 0), container.offsetWidth - movableImage.offsetWidth);
    posY = Math.min(Math.max(posY, 0), container.offsetHeight - movableImage.offsetHeight);

    // Establece la nueva posición de la imagen
    movableImage.style.left = posX + "px";
    movableImage.style.top = posY + "px";
  }
});

