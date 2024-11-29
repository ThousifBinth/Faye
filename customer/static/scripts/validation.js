function signup_form_validation() {
    let isvalid = true;

    const username1 = document.getElementById('username').value.trim();
    const email1 = document.getElementById('email').value;
    const password1 = document.getElementById('password').value;
    const conpass = document.getElementById('confirm-password').value;

    // Validate password
    const passwordLength = password1.length >= 8;
    const passwordUpper = /[A-Z]/.test(password1);
    const passwordLower = /[a-z]/.test(password1);
    const passwordNumber = /[0-9]/.test(password1);

    // Username validation
    if (username1 === "") {
        document.getElementById('name_error').innerHTML = 'Enter username';
        isvalid = false;
    }

    // Email validation
    if (email1 === "") {
        document.getElementById('email_error').innerHTML = "Enter email";
        isvalid = false;
    }

    // Password validation
    if (password1 === '') {
        document.getElementById('pass_error').innerHTML = 'Enter password';
        isvalid = false;
    } else if (!passwordLength || !passwordLower || !passwordNumber || !passwordUpper) {
        document.getElementById('pass_error').innerHTML = 'Password must be at least 8 characters and contain upper and lower case letters and numbers';
        isvalid = false;
    }

    // Confirm password validation
    if (password1 !== conpass) {
        document.getElementById('pass_match').innerHTML = 'Passwords do not match';
        isvalid = false;
    }

    return isvalid;
}
