/* jshint version: */

document.addEventListener('DOMContentLoaded', function () {
  const editButtons = document.querySelectorAll('.edit-btn');
  const modal = document.getElementById('editEventFormModal');
  let descVal = ""; // store description globally in this scope

  editButtons.forEach(button => {
    button.addEventListener('click', () => {
      // ✅ Fill hidden slug field inside the modal
      const slugInput = modal.querySelector('#eventSlugInput');
      if (slugInput) slugInput.value = button.getAttribute('data-slug');

      // ✅ Fill simple text fields
      const titleInput = modal.querySelector('#id_title');
      const dateInput = modal.querySelector('#id_date');
      const capacityInput = modal.querySelector('#id_capacity');
      const locationInput = modal.querySelector('#id_location');

      if (titleInput) titleInput.value = button.getAttribute('data-title');
      if (dateInput) dateInput.value = button.getAttribute('data-date');
      if (capacityInput) capacityInput.value = button.getAttribute('data-capacity');
      if (locationInput) locationInput.value = button.getAttribute('data-location');

      const status = button.getAttribute('data-status');
      const saveDraftBtn = document.getElementById('saveDraftBtn');

      // If event is published, hide "Save as Draft" button
      if (status === '1' && saveDraftBtn) {
        saveDraftBtn.classList.add('d-none');
      } else if (saveDraftBtn) {
        saveDraftBtn.classList.remove('d-none');
      }

      // ✅ Store the event description for later use
      descVal = button.getAttribute('data-description') || "";

      console.log("Captured description:", descVal);
    });
  });



 
});
