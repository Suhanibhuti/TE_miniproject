document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);

        const offsetTop = targetElement.offsetTop;
        const navbarHeight = document.querySelector('nav').offsetHeight;

        window.scrollTo({
            top: offsetTop - navbarHeight,
            behavior: 'smooth'
        });
    });
});
