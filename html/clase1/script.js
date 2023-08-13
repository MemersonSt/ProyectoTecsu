/*Seleciono la clase .example */
const examples = document.querySelectorAll(".example");

examples.forEach(example => {
  example.addEventListener("dragstart", dragStart);
  example.addEventListener("dragend", dragEnd);
});

let draggedExample = null;

function dragStart(event) {
  event.dataTransfer.setData("text/plain", event.target.dataset.type);
  draggedExample = event.target;
}

function dragEnd() {
  draggedExample = null;
}

document.addEventListener("mousemove", moveExample);

function moveExample(event) {
  if (draggedExample && draggedExample.classList.contains("example")) {
    draggedExample.style.position = "absolute";
    draggedExample.style.left = `${event.clientX}px`;
    draggedExample.style.top = `${event.clientY}px`;
  }
}

/*document.addEventListener("DOMContentLoaded", function () {
  const examples = document.querySelectorAll(".example");

  examples.forEach(example => {
    example.addEventListener("dragstart", dragStart);
    example.addEventListener("dragend", dragEnd);
  });
});

let draggedExample = null;

function dragStart(event) {
  event.dataTransfer.setData("text/plain", event.target.dataset.type);
  draggedExample = event.target;
}

function dragEnd() {
  draggedExample = null;
}

document.addEventListener("mousemove", moveExample);

function moveExample(event) {
  if (draggedExample && draggedExample.classList.contains("example")) {
    draggedExample.style.position = "absolute";
    draggedExample.style.left = `${event.clientX}px`;
    draggedExample.style.top = `${event.clientY}px`;
  }
}*/