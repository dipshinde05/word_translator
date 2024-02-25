
document.addEventListener('DOMContentLoaded', function() {
    // Function to toggle language selection box
    function toggleLanguageBox() {
        var selectOptions = document.querySelector('.select-options');
        selectOptions.classList.toggle('active');
    }

    // Hide select box after clicking on it
    document.querySelector('.select-box').addEventListener('click', function() {
        toggleLanguageBox();
    });

    // Hide select box if clicked outside of it
    window.addEventListener('click', function(event) {
        var selectWrapper = document.querySelector('.select-wrapper');
        if (!selectWrapper.contains(event.target)) {
            var selectOptions = document.querySelector('.select-options');
            if (selectOptions.classList.contains('active')) {
                selectOptions.classList.remove('active');
            }
        }
    });

    // Prevent hiding select box when clicked inside it
    document.querySelector('.select-options').addEventListener('click', function(event) {
        event.stopPropagation();
    });
});
