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
typeWriter("Don't fret. We are fixing it asap", "headline1", 100);
