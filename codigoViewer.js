const archivos = {
  "Aritmeticas": ["Suma", "Resta", "multiplicacion", "potencia", "Raiz", "Divicion"],
  "Calculadora Geométrica": ["circulo", "cuadrado", "triangulo", "VolumenCilindro", "Volumencubo", "VolumenPiramide"],
  "Converciones": ["binario_a_decimal", "decimal_a_binario", "Decimal_a_hexadecimal", "Decimal_a_octal", "Hexadecimal_a_decimal", "octal_a_decimal"],
  "Hola_mundo": ["Hola_mundo"],
  "Logicos": ["and", "or", "Not"],
  "Relacionales": ["Todos_Relacionales"]
};

function cargarArchivos() {
  const carpeta = document.getElementById("carpeta").value;
  const archivoSelect = document.getElementById("archivo");
  archivoSelect.innerHTML = "<option value=''>Selecciona un archivo</option>";

  if (archivos[carpeta]) {
    archivos[carpeta].forEach(nombre => {
      const option = document.createElement("option");
      option.value = nombre;
      option.textContent = nombre;
      archivoSelect.appendChild(option);
    });
  }
}

function mostrarCodigo() {
  const carpeta = document.getElementById("carpeta").value;
  const archivo = document.getElementById("archivo").value;

  if (carpeta && archivo) {
    fetch(`codigo/${carpeta}/${archivo}.py`)
      .then(response => {
        if (!response.ok) throw new Error("No se pudo cargar el archivo.");
        return response.text();
      })
      .then(data => {
        const codeElement = document.getElementById("codigo");

        // Limpiar clases previas (si hubo otra selección antes)
        codeElement.className = ""; 

        codeElement.textContent = data;
        codeElement.classList.add("language-python");

        // Reaplicar el resaltado
        hljs.highlightElement(codeElement);
      })
      .catch(err => {
        document.getElementById("codigo").textContent = "Error cargando el archivo.";
      });
  }
}


function copiarCodigo() {
  const codigo = document.getElementById("codigo").innerText;
  navigator.clipboard.writeText(codigo).then(() => {
    alert("¡Código copiado al portapapeles!");
  }).catch(err => {
    alert("Error al copiar: " + err);
  });
}
