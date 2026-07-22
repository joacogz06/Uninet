// Uninet — home universidad (home2.html)

function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const overlay = document.querySelector(".sidebar-overlay");
  const toggleBtn = document.querySelector(".menu-toggle");
  if (sidebar) sidebar.classList.toggle("is-open");
  if (overlay) overlay.classList.toggle("is-visible");
  if (toggleBtn) toggleBtn.classList.toggle("is-hidden");
}

// Cambia el estado de un programa (disponible / no disponible) via AJAX,
// igual que hacía la version anterior con /actualizarestado_programa.
function programaNoDispo(selectEl, id) {
  const nuevoValor = selectEl.value;
  const isOff = selectEl.options[selectEl.selectedIndex].text.trim().toLowerCase() === "no disponible";

  fetch("/actualizarestado_programa", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: id, nuevo_valor: nuevoValor })
  })
    .then((res) => res.json())
    .then(() => {
      selectEl.classList.toggle("is-off", isOff);
      const card = selectEl.closest(".card");
      const dot = card ? card.querySelector(".card__status-dot") : null;
      if (dot) dot.classList.toggle("is-off", isOff);
    })
    .catch((err) => {
      console.error("No se pudo actualizar el estado del programa:", err);
    });
}
