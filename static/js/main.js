/**
 * Initialize the page by styling paragraph elements.
 */
document.addEventListener('DOMContentLoaded', () => {
    const paragraphs = document.querySelectorAll('p');
    if (paragraphs.length > 0) {
        paragraphs[0].style.color = 'green';
    }
});