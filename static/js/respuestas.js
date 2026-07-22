// Uninet — respuestas alumno (respuestas.html)

function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const overlay = document.querySelector(".sidebar-overlay");
  const toggleBtn = document.querySelector(".menu-toggle");
  if (sidebar) sidebar.classList.toggle("is-open");
  if (overlay) overlay.classList.toggle("is-visible");
  if (toggleBtn) toggleBtn.classList.toggle("is-hidden");
}

function eliminarRespuesta(btn, id) {
  if (!confirm("¿Eliminar esta respuesta de tu lista?")) return;

  fetch("/borrar_solicitud", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: id })
  })
    .then((res) => {
      if (!res.ok) throw new Error("No se pudo eliminar");
      const card = btn.closest(".card");
      if (card) {
        card.classList.add("is-removing");
        setTimeout(() => card.remove(), 200);
      }
    })
    .catch((err) => {
      console.error(err);
      alert("Hubo un problema al eliminar la respuesta. Probá de nuevo.");
    });
}
