// Uninet — crear cuenta universidad (crearcuenta2.html)

function closeModal() {
  const modal = document.getElementById("myModal");
  if (modal) modal.classList.remove("is-open");
}

document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("myModal");
  const errorMessage = document.getElementById("error-message");
  const form = document.getElementById("form_crear_uni");

  // Si Flask mandó un error real (registrarUsuario2 con error != ''), lo mostramos solo.
  if (errorMessage && modal) {
    const text = errorMessage.textContent.trim();
    if (text.length > 0) {
      modal.classList.add("is-open");
    }
  }

  if (modal) {
    modal.addEventListener("click", (event) => {
      if (event.target === modal) closeModal();
    });
  }

  // Validación suave del lado del cliente: campos vacíos antes de enviar.
  if (form) {
    form.addEventListener("submit", (event) => {
      const requiredFields = form.querySelectorAll("input[name], select[name]");
      let hasEmpty = false;

      requiredFields.forEach((field) => {
        const isEmpty = !field.value || field.value.trim() === "";
        field.classList.toggle("is-invalid", isEmpty);
        if (isEmpty) hasEmpty = true;
      });

      if (hasEmpty) {
        event.preventDefault();
        if (errorMessage) errorMessage.textContent = "Completá todos los campos antes de continuar.";
        if (modal) modal.classList.add("is-open");
      }
    });
  }
});
