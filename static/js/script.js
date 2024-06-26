function mostrarPodio(deporte) {
    fetch(`/podio/${deporte}`)
        .then(response => response.json())
        .then(data => {
            let contenido = '';
            data.forEach((team, index) => {
                contenido += `
                <div class="box">
                    <div class="number">${index + 1}</div>
                    <div class="cover"><img src="static/images/default.jpg" alt="Team ${index + 1}"></div>
                    <div class="grup">
                        <div class="name"><span>${team[0]}</span></div>
                        <div class="colegio"><span>${team[1]}</span></div>
                    </div>
                    <div class="score"><span>${team[2]} pts</span></div>
                </div>
                <div class="separator"></div>`;
            });
            document.getElementById('podio').innerHTML = contenido;
        });
}

// Cargar el podio de futbol por defecto al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    mostrarPodio('Futbol');
});


document.addEventListener("DOMContentLoaded", function() {
    // Obtener todos los botones dentro del contenedor .buttons_categories
    var buttons = document.querySelectorAll(".buttons_categories button");

    // Iterar sobre cada botón para agregar el evento click
    buttons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Remover la clase 'active' de todos los botones
            buttons.forEach(function(btn) {
                btn.classList.remove("active");
            });

            // Agregar la clase 'active' al botón actual
            this.classList.add("active");
        });
    });
});
