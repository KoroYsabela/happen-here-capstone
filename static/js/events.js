document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.delete-event-btn');
    const deleteFormModal = document.getElementById('deleteEventFormModal');

    deleteButtons.forEach(button => {
        button.addEventListener('click', () => {
        const slug = button.getAttribute('data-slug');

        deleteFormModal.action = `/events/${slug}/delete/`; 
        });
    });
});