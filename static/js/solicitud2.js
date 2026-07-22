// Uninet — solicitudes recibidas (solicitud2.html)

function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const overlay = document.querySelector(".sidebar-overlay");
  const toggleBtn = document.querySelector(".menu-toggle");
  if (sidebar) sidebar.classList.toggle("is-open");
  if (overlay) overlay.classList.toggle("is-visible");
  if (toggleBtn) toggleBtn.classList.toggle("is-hidden");
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) modal.classList.remove("is-open");
}

// Trae los datos del alumno (info_alu en model.py) y los muestra en el modal de perfil.
// Columnas de info_alu: id, nombre, apellido, email, pass, dni, telefono, promedio,
// id_ciudad, id_carrera, situacion, carrera_nombre, ciudad_nombre
function verPerfil(idAlumno) {
  const modal = document.getElementById("modalPerfil");
  const body = document.getElementById("modal_alumno_body");
  body.innerHTML = '<p class="modal__loading">Cargando...</p>';
  modal.classList.add("is-open");

  fetch("/info_alumno", { //manda una petición HTTP al back sin recargar la página. Devuelve una Promesa.
    // fetch() manda una petición al servidor SIN recargar la página (a diferencia de un <form> normal).
    // Se usa cuando solo necesito actualizar una parte chica de la pantalla (un modal, una tarjeta),
    // no toda la página entera. La respuesta se procesa en el .then(), no cambia la URL ni navega a otro lado.
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: idAlumno })
  })
    .then((res) => res.json()) //cuando la respuesta llegue, hacé esto
    .then((data) => {
      const alumno = Array.isArray(data) && data.length > 0 ? data[0] : null;
      if (!alumno) {
        body.innerHTML = '<p class="modal__loading">No se encontró información del alumno.</p>';
        return;
      }

      const filas = [
        ["Correo", alumno[3]],
        ["Teléfono", alumno[6]],
        ["DNI", alumno[5]],
        ["Promedio", alumno[7]],
        ["Carrera", alumno[11]],
        ["Ciudad", alumno[12]],
        ["Presentación", alumno[10]]
      ];

      body.innerHTML = filas
        .map(([label, value]) => `
          <div class="modal__profile-row">
            <span>${label}</span>
            <span>${value ?? "-"}</span>
          </div>
        `)
        .join("");
    })
    .catch((err) => {
      console.error(err);
      body.innerHTML = '<p class="modal__loading">Hubo un problema al cargar el perfil.</p>';
    });
}

// Acepta o rechaza una solicitud (misma ruta /actualizarestado que ya usaba la version anterior).
function responderSolicitud(btn, idSolicitud, nuevoValor) {
  const card = btn.closest(".card");
  const botones = card.querySelectorAll("button");
  botones.forEach((b) => (b.disabled = true));

  fetch("/actualizarestado", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: idSolicitud, nuevo_valor: nuevoValor })
  })
    .then((res) => {
      if (!res.ok) throw new Error("No se pudo actualizar la solicitud");

      const modalId = nuevoValor === "aceptado" ? "modalAceptar" : "modalRechazar";
      document.getElementById(modalId).classList.add("is-open");

      card.classList.add("is-removing");
      setTimeout(() => card.remove(), 200);
    })
    .catch((err) => {
      console.error(err);
      alert("Hubo un problema al procesar la solicitud. Probá de nuevo.");
      botones.forEach((b) => (b.disabled = false));
    });
}
