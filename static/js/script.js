function mostrarPodio(opcion) {
    var contenido = 'opcion1';
    if (opcion === 'opcion1') {
        contenido = `
            <div class="box">
                <div class="number">1</div>
                <div class="cover"><img src="https://m.media-amazon.com/images/I/91-kmdlsEsL._SS500_.jpg" alt="01"></div>
                <div class="name"><span>Mi gente</span></div>
            </div>
            <div class="separator"></div>
            <div class="box">
                <div class="number">2</div>
                <div class="cover"><img src="http://bit.ly/2vlCeWf" alt="02"></div>
                <div class="name"><span>Feels</span></div>
            </div>
            <div class="separator"></div>
            <div class="box">
                <div class="number">3</div>
                <div class="cover"><img src="http://bit.ly/2vlRum1" alt="03"></div>
                <div class="name"><span>Attention</span></div>
            </div>`;
    } else if (opcion === 'opcion2') {
        contenido = `
            <div class="box">
                <div class="number">1</div>
                <div class="cover"><img src="static/images/fotomati.png" alt="04"></div>
                <div class="name"><span>New Song 1</span></div>
            </div>
            <div class="separator"></div>
            <div class="box">
                <div class="number">2</div>
                <div class="cover"><img src="static/images/fotomati.png" alt="05"></div>
                <div class="name"><span>New Song 2</span></div>
            </div>
            <div class="separator"></div>
            <div class="box">
                <div class="number">3</div>
                <div class="cover"><img src="static/images/fotomati.png" alt="06"></div>
                <div class="name"><span>New Song 3</span></div>
            </div>`;
    } else if (opcion === 'opcion3') {
        contenido = `
            <div class="box">
                <div class="number">1</div>
                <div class="cover"><img src="static/images/fotomati.png" alt="07"></div>
                <div class="name"><span>Another Song 1</span></div>
            </div>
            <div class="separator"></div>
            <div class="box">
                <div class="number">2</div>
                <div class="cover"><img src="static/images/fotomati.png" alt="08"></div>
                <div class="name"><span>Another Song 2</span></div>
            </div>
            <div class="separator"></div>
            <div class="box">
                <div class="number">3</div>
                <div class="cover"><img src="static/images/fotomati.png" alt="09"></div>
                <div class="name"><span>Another Song 3</span></div>
            </div>`;
    }
    document.getElementById('podio').innerHTML = contenido;
}


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
