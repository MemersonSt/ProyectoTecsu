function obtenerEstadoProgreso(userId, classId) {
    return fetch(`/api/datos/estado-progreso?userId=${userId}&classId=${classId}`)
      .then(response => response.json())
      .then(data => data.estado);
  }