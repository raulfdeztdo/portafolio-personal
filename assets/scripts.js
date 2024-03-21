
window.onload = function() {
    var path = window.location.pathname;
    var htmlTag = document.documentElement;

    if (path === "/") {
        htmlTag.lang = "es";
    } else if (path === "/en") {
        htmlTag.lang = "en";
    }
}

// Obtenemos los botones de cambio de idioma
var langEsBtn = document.getElementById('lang-es');
var langEnBtn = document.getElementById('lang-en');

// Función para cambiar el idioma
function changeLanguage(langBtn, langPath) {
    if (langBtn) {
        langBtn.addEventListener('click', function() {
            // Comprobamos si ya estamos en el idioma deseado
            if (window.location.pathname !== langPath) {
                // Si no, cambiamos al idioma deseado
                window.location.pathname = langPath;
            }
        });
    }
}

// Funciones para cambiar el modo oscuro
function initializeDarkMode() {
    // Modo oscuro por defecto
    document.documentElement.classList.remove('no-js', 'light');
    if (localStorage.getItem('color-theme') === 'light') {
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
    } else if (localStorage.getItem('color-theme') === 'dark' || !('color-theme' in localStorage)) {
        document.documentElement.classList.add('dark');
    }

    var themeToggleBtn = document.getElementById('darkmode-toggle');
    var themeToggleDarkIcon = document.getElementById('darkMode');
    var themeToggleLightIcon = document.getElementById('lightMode');

    // Si los elementos existen, entonces ejecuta el código
    if (themeToggleBtn && themeToggleDarkIcon && themeToggleLightIcon) {
        themeToggleBtn.addEventListener('click', function() {
            // Si se estableció previamente a través del almacenamiento local
            if (localStorage.getItem('color-theme')) {
                if (localStorage.getItem('color-theme') === 'dark') {
                    document.documentElement.classList.remove('dark');
                    document.documentElement.classList.add('light');
                    localStorage.setItem('color-theme', 'light');
                } else {
                    document.documentElement.classList.add('dark');
                    document.documentElement.classList.remove('light');
                    localStorage.setItem('color-theme', 'dark');
                }

            // Si NO se estableció previamente a través del almacenamiento local
            } else {
                if (document.documentElement.classList.contains('dark')) {
                    document.documentElement.classList.remove('dark');
                    document.documentElement.classList.add('light');
                    localStorage.setItem('color-theme', 'light');
                } else {
                    document.documentElement.classList.add('dark');
                    document.documentElement.classList.remove('light');
                    localStorage.setItem('color-theme', 'dark');
                }
            }
        });
    }
}

initializeDarkMode();
changeLanguage(langEsBtn, '/');
changeLanguage(langEnBtn, '/en');