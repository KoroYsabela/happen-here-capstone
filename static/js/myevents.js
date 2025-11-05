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

      // ✅ Store the event description for later use
      descVal = button.getAttribute('data-description') || "";

      console.log("Captured description:", descVal);
    });
  });

  // ✅ When modal is fully shown
  $('#editEventFormModal').on('shown.bs.modal', function () {
    const $desc = $('#id_description');

    // Ensure Summernote is initialized (if not already)
    if (!$desc.next('.note-editor').length) {
      console.log("Initializing Summernote...");
      $desc.summernote({
        height: 300,
        placeholder: 'Write your event details...'
      });
    }

    // Wait briefly to ensure the editor has finished rendering
    setTimeout(() => {
      console.log("Setting Summernote content:", descVal);
      $desc.summernote('code', descVal);
    }, 150);
  });

  // ✅ When modal is hidden — reset all fields
  $('#host-event-modal').on('hidden.bs.modal', function () {
    console.log("Clearing Summernote and form...");

    const $desc = $('#id_description');

    // Clear the Summernote editor
    if ($desc.next('.note-editor').length) {
      $desc.summernote('destroy'); // remove editor instance cleanly
    }

    // Clear hidden textarea and inputs
    $desc.val('');
    $(this)
      .find('input[type="text"], input[type="number"], input[type="datetime-local"]')
      .val('');
    $(this).find('#eventSlugInput').val('');
  });
});
