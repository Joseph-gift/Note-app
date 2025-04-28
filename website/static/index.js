// This function is called when the user clicks the "Delete" button on a note
// It sends a POST request to the server with the note ID to delete the note
// and then reloads the page to reflect the changes

function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId})
    }).then((_res) =>  {
        window.location.href = "/";
    });
}



// Fade out the alert message after a delay
// This function is called when the DOM content is fully loaded
// It selects all elements with the class "alert" and sets a timeout to remove the "show" class
// and add the "fade" class after 1500 milliseconds (1.5 seconds)
// After another 500 milliseconds (2 seconds total), it removes the alert element from the DOM
// This creates a fade-out effect for the alert messages

document.addEventListener("DOMContentLoaded", () => {
    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove("show");
            alert.classList.add("fade");
        }, 1500); 
        setTimeout(() => {
            alert.remove(); 
        }, 2000); 
    });
});