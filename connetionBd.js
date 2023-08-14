const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mysql = require('mysql');

// Configuración de la conexión a la base de datos
const connection = mysql.createConnection({
  host: 'bv57qrhlyjg8gwx0v1rd-mysql.services.clever-cloud.com',
  user: 'um7ydybmffyrgqor',
  password: 'fPjmy2t74uST7WRqWAn5',
  database: 'bv57qrhlyjg8gwx0v1rd'
});

connection.connect();

app.use(bodyParser.json());

// Ruta para recibir el dato y guardar en la base de datos
app.post('/guardar-dato', (req, res) => {
    //const userId = req.query.userId; // Obtener userId de los parámetros de la consulta          '+userId+', 
    const classId = req.query.classId; // Obtener classId de los parámetros de la consulta
  
  const sql = 'INSERT INTO Progreso (UserId, ClassId, Status) VALUES ('+classId+', `1`)';
  connection.query(sql, [userId], (error, results) => {
    if (error) {
      console.error('Error al insertar el dato:', error);
      res.status(500).json({ mensaje: 'Error al insertar el dato en la base de datos' });
    } else {
      console.log('Dato insertado correctamente');
      res.json({ mensaje: 'Dato insertado correctamente' });
    }
  });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Servidor en funcionamiento en el puerto ${port}`);
});
