document.addEventListener("DOMContentLoaded", () => {

    // Select the flash message element using its ID
    let flashMessage = document.querySelector("#flash-message");

    // Check if the flash message element exists
    if (flashMessage) {

        // Wait for 3 seconds after the flash message is displayed
        setTimeout(() => {

            // Resume the CSS animation for hiding the flash message
            flashMessage.style.animationPlayState = "running";

            // Wait for the animation to complete (2 seconds) before removing the flash message from the DOM
            setTimeout(() => {
                flashMessage.remove();
            }, 2000);

        }, 3000);
    }

});

