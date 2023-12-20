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


// SHOWING POPUP TO DELETE AND EDIT POSTS
function toggleDropdown(postId) {
    const dropdown = document.getElementById(`dropdown-${postId}`);
    const body = document.body;

    // Toggle the visibility of the dropdown
    if (dropdown.style.display === 'block') {
        dropdown.style.display = 'none';
        body.classList.remove('unselectable');
    } else {
        dropdown.style.display = 'block';
        body.classList.add('unselectable');
    }
}

document.addEventListener('click', function(event) {
    const dropdown = document.getElementById(`dropdown-{{ post.id }}`);

    // Check if the clicked element is part of the dropdown or the icon that opens the dropdown
    if (!dropdown.contains(event.target) && event.target.closest('.icon-dropdown') === null) {
        // Clicked outside the dropdown or the icon, hide it and remove unselectable class
        dropdown.style.display = 'none';
        document.body.classList.remove('unselectable');
    }
});

// UPDATE MODAL
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('editDetailsButton').addEventListener('click', function () {
        var myModal = new bootstrap.Modal(document.getElementById('editDetailsModal'));
        myModal.show();
    });
});

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('editDetailsButton').addEventListener('click', function () {
        // Load modal content dynamically using AJAX
        fetch('path/to/update-modal-content.html')  // Replace with the actual path
            .then(response => response.text())
            .then(html => {
                document.getElementById('modalContainer').innerHTML = html;

                // Show the modal
                var myModal = new bootstrap.Modal(document.getElementById('editDetailsModal'));
                myModal.show();
            })
            .catch(error => {
                console.error('Error loading modal content:', error);
            });
    });
});




