document.addEventListener('DOMContentLoaded', function() {
    const showToggles = document.querySelectorAll('.show');
    const cshowToggles = document.querySelectorAll('.cshow');

    showToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const passwordField = toggle.previousElementSibling; // Assuming the password field is just before the icon
            togglePasswordVisibility(passwordField, toggle);
        });
    });

    cshowToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const passwordField = toggle.previousElementSibling; // Assuming the password field is just before the icon
            togglePasswordVisibility(passwordField, toggle);
        });
    });
});

function togglePasswordVisibility(passwordField, showElement) {
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        showElement.classList.replace('fa-eye-slash', 'fa-eye');
    } else {
        passwordField.type = 'password';
        showElement.classList.replace('fa-eye', 'fa-eye-slash');
    }
}

//User profile submenu dropdown
function toggleMenu(){
const subMenu = document.getElementById('subMenu');
subMenu.classList.toggle('open-menu');
}

//TOGGLING THE SIDEBAR
let btn = document.querySelector('#btn')
let sidebar = document.querySelector('.sidebar')

btn.onclick = function(){
    sidebar.classList.toggle('active');
};