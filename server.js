const express = require('express');
const app = express();
const path = require('path');

app.use('/img', express.static(path.join(__dirname, '../ProyectoTecsu', 'img')));

app.use('/html', express.static(path.join(__dirname, '../ProyectoTecsu', 'html')))

app.use('/html/', express.static(path.join(__dirname, '../ProyectoTecsu', 'final')))

app.use('/html/', express.static(path.join(__dirname, '../ProyectoTecsu', 'style')))

app.use('/Formularios', express.static(path.join(__dirname, '../ProyectoTecsu', 'Formularios')))

app.use('/javascript', express.static(path.join(__dirname, '../ProyectoTecsu', 'javascript')))

//app.use('/javascript', express.static(path.join(__dirname, '../ProyectoTecsu', 'getClassId')))


// Configuración de rutas estáticas
app.use(express.static(path.join(__dirname, 'ProyectoTecsu')));

// Middleware personalizado para establecer el tipo MIME correcto para archivos CSS
app.use('/css', (req, res, next) => {
  res.type('text/css');
  next();
}, express.static(path.join(__dirname, '../ProyectoTecsu', 'css')));

// Middleware personalizado para establecer el tipo MIME correcto para archivos JavaScript
app.use('/javascript', (req, res, next) => {
  res.type('application/javascript');
  next();
}, express.static(path.join(__dirname, '../ProyectoTecsu', 'javascript')));


// Configuración de rutas
app.get('/Bienvenida.html', (req, res) => {
  res.sendFile(path.join(__dirname, '../ProyectoTecsu', 'Bienvenida.html'));
});

app.get('/Menu.html', (req, res) => {
    res.sendFile(path.join(__dirname, '../ProyectoTecsu', 'Menu.html'));
  });

// Iniciar el servidor
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Servidor en funcionamiento en el puerto ${port}`);
});
