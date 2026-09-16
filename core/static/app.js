const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
const navCta = document.getElementById('navCta');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    hamburger.classList.toggle('active');
    navCta.classList.toggle('active');

});