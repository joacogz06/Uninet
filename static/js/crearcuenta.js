// Uninet — crear cuenta alumno (crearcuenta.html)

function closeModal() {
  const modal = document.getElementById("myModal");
  if (modal) modal.classList.remove("is-open");
}

document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("myModal");
  const form = document.getElementById("form_crear_alumno");

  if (modal) {
    modal.addEventListener("click", (event) => {
      if (event.target === modal) closeModal();
    });
  }

  // Validación suave: si falta algún campo requerido al enviar,
  // mostramos el modal en vez de dejar que el navegador lo bloquee en silencio.
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
        if (modal) modal.classList.add("is-open");
      }
    });
  }
});
