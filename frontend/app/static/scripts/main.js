function typeWriter(text, elementId, speed) {
    const element = document.getElementById(elementId);
    let i = 0;
    const typingInterval = setInterval(() => {
        element.textContent += text.charAt(i);
        i++;
        if (i > text.length - 1) {
            clearInterval(typingInterval);
        }
    }, speed);
}

// Call the typeWriter function for each headline
typeWriter("All in one bugs and defects reporting tool", "headline1", 100);

// Mark the acive nav link
document.addEventListener("DOMContentLoaded", () => {
    let navLinks = document.querySelectorAll("mark-nav a");
    navLinks = Array.from(navLinks)

    const signInLink = document.querySelector(".mark-login-link")
    navLinks.push(signInLink)
    navLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            // Remove 'active' class from all links
            navLinks.forEach((link) => link.classList.remove("active"));

            // Add 'active' class to the clicked link
            event.target.classList.add("active");
        });
    });
});
