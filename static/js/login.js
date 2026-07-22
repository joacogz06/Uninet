// Uninet — login (inicio.html)

function closeModal() {
  const modal = document.getElementById("myModal");
  if (modal) modal.classList.remove("is-open");
}

document.addEventListener("DOMContentLoaded", () => {
  // Si Flask mandó un mensaje de error (render_template("inicio.html", error=...)),
  // lo mostramos automáticamente al cargar la página.
  const errorMessage = document.getElementById("error-message");
  const modal = document.getElementById("myModal");

  if (errorMessage && modal) {
    const text = errorMessage.textContent.trim();
    if (text.length > 0) {
      modal.classList.add("is-open");
    }
  }

  // Cerrar el modal haciendo click afuera del contenido
  if (modal) {
    modal.addEventListener("click", (event) => {
      if (event.target === modal) closeModal();
    });
  }

  // Validación simple, no bloqueante, solo para guiar al usuario.
  // No impide el submit: el backend sigue siendo la fuente de verdad.
  const emailInput = document.getElementById("ICusername");
  const passwordInput = document.getElementById("ICpassword");

  const setFieldError = (input, message) => {
    const errorEl = document.querySelector(`[data-error-for="${input.id}"]`);
    if (!errorEl) return;
    errorEl.textContent = message;
    input.classList.toggle("is-invalid", Boolean(message));
  };

  if (emailInput) {
    emailInput.addEventListener("blur", () => {
      const value = emailInput.value.trim();
      if (value.length === 0) {
        setFieldError(emailInput, "");
        return;
      }
      const isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
      setFieldError(emailInput, isValid ? "" : "Ingresá un correo válido.");
    });
  }

  if (passwordInput) {
    passwordInput.addEventListener("blur", () => {
      const value = passwordInput.value;
      if (value.length === 0) {
        setFieldError(passwordInput, "");
        return;
      }
      setFieldError(passwordInput, value.length < 4 ? "Contraseña demasiado corta." : "");
    });
  }
});
