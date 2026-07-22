// Uninet — detalle de programa (info_programa.html)

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

function aplicar(idPrograma) {
  const btn = document.getElementById("btn-aplicar");
  if (btn) {
    btn.disabled = true;
    btn.textContent = "Enviando...";
  }

  const formData = new FormData();
  formData.append("idprograma", idPrograma);

  fetch("/solicitud_programa", {
    method: "POST",
    body: formData
  })
    .then((res) => {
      if (res.ok) {
        document.getElementById("myModal").classList.add("is-open");
      } else {
        throw new Error("La solicitud no pudo enviarse");
      }
    })
    .catch((err) => {
      console.error(err);
      alert("Hubo un problema al enviar tu solicitud. Probá de nuevo.");
    })
    .finally(() => {
      if (btn) {
        btn.disabled = false;
        btn.textContent = "Aplicar a este programa";
      }
    });
}
