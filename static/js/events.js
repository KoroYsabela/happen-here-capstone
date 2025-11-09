document.addEventListener('DOMContentLoaded', function () {
  // The "Cancel Booking" trigger buttons open a modal and include data attributes
  // with the booking id and event slug. When clicked we set the cancel form's
  // action to the correct URL: /<slug>/<booking_id>/cancel/
  const cancelTriggers = document.querySelectorAll('.cancel-trigger');
  const cancelForm = document.getElementById('cancelEventBookingForm');

  cancelTriggers.forEach(button => {
    button.addEventListener('click', () => {
      const bookingId = button.getAttribute('data-booking-id');
      const slug = button.getAttribute('data-slug');
      if (cancelForm && bookingId && slug) {
        cancelForm.action = `/${slug}/${bookingId}/cancel/`;
      }
    });
  });
});