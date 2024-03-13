/* Get the name label to deal with the empty input error message. */
var nameLabel = document.getElementById("name-label");

/* Get the phone format propertie to deal with the phone number error messages. */
var phoneFormat = document.getElementById("phone-format");

/* This is need to check the email correction. */
var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

/* These are the input fields. */
var regForm = {
  name: document.getElementById("name"),
  birth: document.getElementById("birth"),
  phone: document.getElementById("phone"),
  email: document.getElementById("email"),
  confEmail: document.getElementById("confEmail"),
  pw: document.getElementById("password"),
  confPw: document.getElementById("confPassword"),
};

/* Get the current date to show it automaticly on the website. */
function get_current_date() {
    const date = new Date();
    let currentDay = String(date.getDate()).padStart(2, "0");
    let currentMonth = String(date.getMonth() + 1).padStart(2, "0");
    let currentYear = date.getFullYear();
    regForm.birth.value = `${currentYear}-${currentMonth}-${currentDay}`;
}

/* After clicking the button this function deals with empty fields, error messages. */
function registration_form() {
    get_current_date();
    if (nameLabel.previousSibling != document.getElementById("form-title")) {
        nameLabel.previousSibling.remove();
    }
    if (regForm.name.nextSibling != document.getElementById("birth-label")){
        regForm.name.nextSibling.remove();
    }
    if (regForm.birth.nextSibling != document.getElementById("phone-label")) {
        regForm.birth.nextSibling.remove();
    }
    if (phoneFormat.nextSibling != document.getElementById("email-label")) {
        phoneFormat.nextSibling.remove();
      }
    if (regForm.email.nextSibling != document.getElementById("confEmail-label")){
        regForm.email.nextSibling.remove();
    }
    if (regForm.confEmail.nextSibling != document.getElementById("password-label")){
        regForm.confEmail.nextSibling.remove();
    }
    if (regForm.pw.nextSibling != document.getElementById("confPassword-label")){
        regForm.pw.nextSibling.remove();
    }
    if (regForm.confPw.nextSibling != document.getElementById("submit-btn")){
        regForm.confPw.nextSibling.remove();
    }
    check_empty_form();
}

/*
    If the input field's border style was already red because of some error,
    the user clicks in it than restore the border style
*/
function check_input_field(field){
    if (regForm[field].style.borderTop == "1px solid red") {
        regForm[field].style.borderTop = "1px solid #faebd7";
        regForm[field].style.borderBottom = "1px solid #faebd7";
    }
}

/* If the user let any input field empty, this function will highlite the input field's border red. */
function check_empty_form() {
    let error = false;
    for (let data in regForm) {
        if (regForm[data].value == "") {
            regForm[data].style.borderTop = "1px solid red";
            regForm[data].style.borderBottom = "1px solid red";
            error = true;
      }
    }
    if (error) {
        empty_message();
    }
    check_correct_inputs();
}

/* This function deals with the inputs correction. */
function check_correct_inputs() {
    if (!regForm.name.value.includes(" ")) {
        error_message("name", document.createTextNode("Please enter a valid name!"));
    }
    let givenDate = regForm.birth.value;
    if (givenDate.slice(0, 4) >= 2023) {
        error_message("birth", document.createTextNode("Please select a year before 2023!"));
    }
    if (regForm.phone.value.slice(0, 2) != "06" && regForm.phone.value.slice(0, 2) != "36" || regForm.phone.value.length != 11) {
        let phoneErr = document.createTextNode("Please enter a valid phone number");
        regForm.phone.style.borderTop = "1px solid red";
        regForm.phone.style.borderBottom = "1px solid red";
        phoneFormat.parentNode.insertBefore(phoneErr, phoneFormat.nextSibling);
    }
    if (!regForm.email.value.match(validRegex)) {
        error_message("email", document.createTextNode("Please enter a valid email!"));
    }
    if (regForm.email.value != regForm.confEmail.value) {
        error_message("confEmail", document.createTextNode("The given emails do not match!"));
    }
    console.log(regForm.confPw.value.length, regForm.pw.value.length);
    if (regForm.pw.value.length < 8 || regForm.pw.value.length > 16) {
        error_message("pw", document.createTextNode("Please enter a valid password!"));
    }
    console.log(regForm.pw.value, regForm.confPw.value);
    if (regForm.pw.value != regForm.confPw.value) {
        error_message("confPw", document.createTextNode("The given passwords do not match!"));
    }
}

/* This function writes the empty field error message. */
function empty_message() {
    let emptyMessage = document.createTextNode("Please fill out everything!");
    nameLabel.parentNode.insertBefore(emptyMessage, nameLabel);
}

/* This function writes the error messages for all of the input fields. */
function error_message(inpField, errMessage) {
    regForm[inpField].style.borderTop = "1px solid red";
    regForm[inpField].style.borderBottom = "1px solid red";
    regForm[inpField].parentNode.insertBefore(errMessage, regForm[inpField].nextSibling);
}