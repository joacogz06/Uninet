// Uninet — perfil alumno (perfil.html)

function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const overlay = document.querySelector(".sidebar-overlay");
  const toggleBtn = document.querySelector(".menu-toggle");
  if (sidebar) sidebar.classList.toggle("is-open");
  if (overlay) overlay.classList.toggle("is-visible");
  if (toggleBtn) toggleBtn.classList.toggle("is-hidden");
}

function togglePassword() {
  const mask = document.getElementById("password-mask");
  const real = document.getElementById("password-real");
  if (!mask || !real) return;

  const isHidden = real.hasAttribute("hidden");
  if (isHidden) {
    real.removeAttribute("hidden");
    mask.setAttribute("hidden", "");
  } else {
    real.setAttribute("hidden", "");
    mask.removeAttribute("hidden");
  }
}
