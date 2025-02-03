// Validación simple del formulario
document
  .getElementById("contacto-form")
  .addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Gracias por tu mensaje. Nos pondremos en contacto contigo pronto.");
  });
