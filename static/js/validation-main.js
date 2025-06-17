document.addEventListener('DOMContentLoaded', function () {
  validateWardrobeForm(); 
});


function validateWardrobeForm() {
  const form = document.querySelector('.wardrobe');
  if (!form) return;

  const inputs = form.querySelectorAll('input[type="text"]');
  const submitBtn = form.querySelector('button[type="submit"]');

  function isValid(value) {
    const num = parseInt(value, 10);
    return !isNaN(num) && num > 0 && num <= 4000;
  }

  function checkFormValidity() {
    let allValid = true;

    inputs.forEach(input => {
      const valid = isValid(input.value);
      input.classList.toggle('is-invalid', !valid);
      input.classList.toggle('is-valid', valid);

      if (!valid) allValid = false;
    });

    if (submitBtn) {
      submitBtn.disabled = !allValid;
    }
  }

  // Инициализируем валидацию при вводе
  inputs.forEach(input => {
    input.addEventListener('input', checkFormValidity);
  });

  // Проверка при загрузке
  checkFormValidity();
}
