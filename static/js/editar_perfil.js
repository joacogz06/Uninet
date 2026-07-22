// Uninet — editar perfil alumno (editar_perfil.html)

function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const overlay = document.querySelector(".sidebar-overlay");
  const toggleBtn = document.querySelector(".menu-toggle");
  if (sidebar) sidebar.classList.toggle("is-open");
  if (overlay) overlay.classList.toggle("is-visible");
  if (toggleBtn) toggleBtn.classList.toggle("is-hidden");
}

function closeModal() {
  const modal = document.getElementById("myModal");
  if (modal) modal.classList.remove("is-open");
}

document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("myModal");
  const errorMessage = document.getElementById("error-message");
  const form = document.getElementById("form_editar_perfil");

  // Si Flask mandó un error real (editarperfilalu con error != ''), lo mostramos.
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

  // Validación suave: campos vacíos antes de enviar.
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
        if (errorMessage) errorMessage.textContent = "Completá todos los campos antes de guardar.";
        if (modal) modal.classList.add("is-open");
      }
    });
  }
});
