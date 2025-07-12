document.addEventListener('DOMContentLoaded', function () {
  validateWardrobeForm(); 
  validateSaveOrderForm();
  validateLoginForm();
  validateRegisterForm();
  validateResetPassordForm();
  validateSetPasswordForm();
});


/**
Password Set Form Validator
*/
function validateSetPasswordForm() {
  const form = document.querySelector('.set-password-form');
  if (!form) return;

  const passwdInputs = form.querySelectorAll('.user-password')
  const submitBtn = form.querySelector('button[type="submit"]')

  // Отключить кнопку submit 
  submitBtn.disabled = true;
  // Проверить валидность полей
  function checkFormValidity() {
    let allValid = true;   
    // Валидация password
    passwdInputs.forEach(input => {
      const valid = validatePassword(input.value);
      if (!valid) allValid = false;
    });

    // Активируем или деактивируем кнопку
    submitBtn.disabled = !allValid;
  };
  // Добавляем обработчики событий на поля ввода
  passwdInputs.forEach(input => input.addEventListener('input', checkFormValidity));
  // Проверка при загрузке
  checkFormValidity();
};


/**
Password Reset Query Form Validator
*/
function validateResetPassordForm() {
  const form = document.querySelector('.reset-password-form');
  if (!form) return;

  const emailInput = form.querySelector('.user-email');
  const submitBtn = form.querySelector('button[type="submit"]')

  // Отключить кнопку submit 
  submitBtn.disabled = true;
  // Проверить валидность полей
  function checkFormValidity() {
    let allValid = true;   
    // Валидация email
    const emailValid = validateEmail(emailInput.value);
    if (!emailValid) allValid = false;
    // Активируем или деактивируем кнопку
    submitBtn.disabled = !allValid;
  };
  // Добавляем обработчики событий на поля ввода
  emailInput.addEventListener('input', checkFormValidity);
  // Проверка при загрузке
  checkFormValidity();
};


/**
Registration Page Validator
*/
function validateRegisterForm() {
  const form = document.querySelector('.user-register');
  if (!form) return;

  const nameInputs = form.querySelectorAll('.user-names')
  const emailInput = form.querySelector('.user-email');
  const passwdInputs = form.querySelectorAll('.user-password')
  const submitBtn = form.querySelector('button[type="submit"]')
  // Отключить кнопку submit 
  submitBtn.disabled = true;
  // Проверить валидность полей
  function checkFormValidity() {
    let allValid = true;   
    // Валидация имен
    nameInputs.forEach(input => {
      const valid = validateName(input.value);
      if (!valid) allValid = false;
    });
    // Валидация email
    const emailValid = validateEmail(emailInput.value);
    if (!emailValid) allValid = false;
    // Валидация password
    passwdInputs.forEach(input => {
      const valid = validatePassword(input.value);
      if (!valid) allValid = false;
    });
    // Активируем или деактивируем кнопку
    submitBtn.disabled = !allValid;
  };
  // Добавляем обработчики событий на поля ввода
  emailInput.addEventListener('input', checkFormValidity);
  nameInputs.forEach(input => input.addEventListener('input', checkFormValidity));
  passwdInputs.forEach(input => input.addEventListener('input', checkFormValidity));
  // Проверка при загрузке
  checkFormValidity();
};


/**
Login Page Validator
*/
function validateLoginForm() {
  const form = document.querySelector('.login-form');
  if (!form) return;

  const emailInput = form.querySelector('.user-email');
  const passwdInput = form.querySelector('.user-password')
  const submitBtn = form.querySelector('button[type="submit"]')
  // Отключить кнопку submit 
  submitBtn.disabled = true;
  // Проверить валидность полей
  function checkFormValidity() {
    let allValid = true;   
    // Валидация email
    const emailValid = validateEmail(emailInput.value);
    if (!emailValid) allValid = false;
    // Валидация password
    const passwdValid = validatePassword(passwdInput.value);
    if (!passwdValid) allValid = false;
    // Активируем или деактивируем кнопку
    submitBtn.disabled = !allValid;
  };
  // Добавляем обработчики событий на поля ввода
  emailInput.addEventListener('input', checkFormValidity);
  passwdInput.addEventListener('input', checkFormValidity);
  // Проверка при загрузке
  checkFormValidity();
};


/**
Wardrobe Calculator Page Validator
*/
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
      // input.classList.toggle('is-invalid', !valid);
      // input.classList.toggle('is-valid', valid);

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
};


/**
Save Order Page Validator
*/
function validateSaveOrderForm() {
  const form = document.querySelector('.saveorder') 
  if (!form) return;

  const allInputs = form.querySelectorAll('input[type="text"]')
  const nameInputs = form.querySelectorAll('.user_names');
  const phoneInput = form.querySelector('.user_phone');
  const emailInput = form.querySelector('.user_email');
  const submitBtn = form.querySelector('button[type="submit"]'); 

  // Отключить кнопку submit 
  submitBtn.disabled = true;

  // Проверить валидность полей
  function checkFormValidity() {
    let allValid = true;   
    // Валидация имен
    nameInputs.forEach(input => {
      const valid = validateName(input.value);
      // input.classList.toggle('is-invalid', !valid);
      // input.classList.toggle('is-valid', valid);
      if (!valid) allValid = false;
    })
    // Валидация телефона
    const phoneValid = validatePhoneNumber(phoneInput.value);
    // phoneInput.classList.toggle('is-invalid', !phoneValid);
    // phoneInput.classList.toggle('is-valid', phoneValid);
    if (!phoneValid) allValid = false;

    // Валидация email
    const emailValid = validateEmail(emailInput.value);
    // emailInput.classList.toggle('is-invalid', !emailValid);
    // emailInput.classList.toggle('is-valid', emailValid);
    if (!emailValid) allValid = false;

    // Активируем или деактивируем кнопку
    submitBtn.disabled = !allValid;
  };

  // Добавляем обработчики событий на поля ввода
  nameInputs.forEach(input => input.addEventListener('input', checkFormValidity));
  phoneInput.addEventListener('input', checkFormValidity);
  emailInput.addEventListener('input', checkFormValidity);

  // Проверка при загрузке
  checkFormValidity();
};



// Функции валидации
/**
Name validation func.
@param {str} name - user name or surname
@returns {boolean}
*/
function validateName(name) {
  const namePattern = /^[A-ZА-Я][a-zа-яё]+$/;
  return namePattern.test(name) && name.length <= 20;
}

/**
Phone number validation func.
@param {str} phone - phone number
@returns {boolean}
*/
function validatePhoneNumber(phone) {
  // Проверяем, что номер начинается с "+" или состоит только из цифр
  const phonePattern = /^\+?\d{1,15}$/;
  // Проверяем длину номера и соответствие шаблону
  return phonePattern.test(phone) && phone.length <= 15;
}

/**
Email validation func.
@param {str} email - email 
@returns {boolean}
*/
function validateEmail(email) {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailPattern.test(email);  
}

/**
Password validation func.
@param {str} password - password 
@returns {boolean}
*/
function validatePassword(password) {
  return password.length >= 6;  
}
