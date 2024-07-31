// Animação de menu responsivo
document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('nav');
    const toggle = document.createElement('div');
    toggle.classList.add('menu-toggle');
    toggle.innerHTML = '&#9776;';
    header.appendChild(toggle);

    toggle.addEventListener('click', function() {
        nav.classList.toggle('open');
    });
});
