document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const searchForm = document.getElementById('searchForm');

    let typingTimer;
    const typingDelay = 1500;

    searchInput.addEventListener('input', () => {
        clearTimeout(typingTimer);
        typingTimer = setTimeout(() => {
            searchForm.submit();
        }, typingDelay);
    });

    searchInput.addEventListener('keydown', () => {
        clearTimeout(typingTimer);
    });
});