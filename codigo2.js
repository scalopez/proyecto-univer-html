function cargarConversion(nombreArchivo) {
  fetch(`codigo/Converciones/${nombreArchivo}.py`)
    .then(response => {
      if (!response.ok) throw new Error("No se pudo cargar el archivo.");
      return response.text();
    })
    .then(data => {
      const codeElement = document.getElementById("codigo");
      codeElement.textContent = data;
      codeElement.className = "language-python";
      hljs.highlightElement(codeElement);
    })
    .catch(error => {
      document.getElementById("codigo").textContent = "Error cargando el archivo.";
      console.error(error);
    });
}
