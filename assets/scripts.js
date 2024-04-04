
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
    var themeToggleBtn = document.getElementById('darkmode-toggle');
    var themeToggleDarkIcon = document.getElementById('darkMode');
    var themeToggleLightIcon = document.getElementById('lightMode');

    if (localStorage.getItem('color-theme') === 'light') {
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
        themeToggleBtn.click();
    } else if (localStorage.getItem('color-theme') === 'dark' || !('color-theme' in localStorage)) {
        document.documentElement.classList.add('dark');
    }

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

document.head.innerHTML += `
    <link rel="apple-touch-icon" sizes="180x180" href="/images/favicon/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon//favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon//favicon-16x16.png">
    <link rel="manifest" href="/images/favicon//site.webmanifest">
    <link rel="mask-icon" href="/images/favicon//safari-pinned-tab.svg" color="#5bbad5">
    <meta name="msapplication-TileColor" content="#000000">
    <meta name="theme-color" content="#000000">
`;

initializeDarkMode();
changeLanguage(langEsBtn, '/');
changeLanguage(langEnBtn, '/en');