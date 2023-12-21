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




//A POPUP FOR A COMMENT
function toggleCommentInput(postId) {
    var commentInput = document.getElementById('commentInput' + postId);
    if (commentInput) {
        if (commentInput.style.display === 'none' || commentInput.style.display === '') {
            commentInput.style.display = 'block';
        } else {
            commentInput.style.display = 'none';
        }
    } else {
        console.error('Comment input not found for post ID ' + postId);
    }
}

function postComment(postId) {
    console.log('Posting comment for post ID ' + postId);
    // Implement your logic to post the comment for the specific post
    // You can use AJAX to send the comment to the server and update the UI accordingly
}