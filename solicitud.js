function obtenerEstadoProgreso(userId, classId) {
    return fetch(`/api/datos/guardar-dato?userId=${userId}&classId=${classId}`)
      .then(response => response.json())
      .then(data => data.estado);
  }

  