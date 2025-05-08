// External JavaScript for Admission Form

function setTextEditableAll(disabled) {
    let inp = document.getElementsByTagName("input");
    for (let i = 0; i < inp.length; i++) {
        if(['text','tel' , 'email', 'date', 'file', 'number'].includes(inp[i].type)){
            inp[i].disabled = disabled;
        }
    }

    let inp2 = document.getElementsByTagName("select");
    for (let i = 0; i < inp2.length; i++) {
        inp2[i].disabled = disabled;
    }
}

function categorySelected(selectElem){
    const studentCategoryOtherInput = document.getElementsByName("student_category_other")[0];
    studentCategoryOtherInput.disabled = (selectElem.value !== "Other");
    if (selectElem.value !== "Other")
        studentCategoryOtherInput.value = "";
}

function guardianSelected(elem){
    const guardianDiv = document.getElementById("guardianDiv");
    elem.value === "yes" ? guardianDiv.style.display = "block" : guardianDiv.style.display = "none";
}

function declarationStateChange(elem){
    const submitForm = document.getElementById("submitForm");
    if (elem.checked) {
        submitForm.disabled = false;
    } else {
        submitForm.disabled = true;
    }
}

function validateForm() {
    return true;
    // List of required fields to check if they are not empty
    const requiredFields = [
        { name: 'student_name', label: 'Student Name' },
        { name: 'student_class', label: 'Student Class' },
        { name: 'student_aadhar', label: 'Student Aadhar' },
        { name: 'student_date_of_birth', label: 'Student Date of Birth' },
        { name: 'student_gender', label: 'Student Gender' },
        { name: 'student_email', label: 'Student Email' },
        { name: 'student_whatsapp', label: 'Student WhatsApp Number' },
        { name: 'father_name', label: 'Father Name' },
        { name: 'father_mobile', label: 'Father Mobile Number' },
        { name: 'mother_name', label: 'Mother Name' },
        { name: 'mother_mobile', label: 'Mother Mobile Number' }
    ];

    // Loop through each required field to check if they are empty
    for (let field of requiredFields) {
        const input = document.getElementsByName(field.name)[0];
        if (input && !input.value.trim()) {
            alert(`Please fill in the "${field.label}" field.`);
            input.focus();
            return false;
        }
    }

    // Validate Aadhar numbers (should be 12 digits)
    const aadharFields = ['student_aadhar', 'father_aadhar', 'mother_aadhar'];
    for (let name of aadharFields) {
        const input = document.getElementsByName(name)[0];
        if (input && input.value && !/^\d{12}$/.test(input.value)) {
            alert(`Invalid Aadhar number in "${name.replace(/_/g, ' ')}". It must be a 12-digit number.`);
            input.focus();
            return false;
        }
    }

    // Validate mobile numbers (should be 10 digits)
    const mobileFields = ['student_whatsapp', 'father_mobile', 'mother_mobile'];
    for (let name of mobileFields) {
        const input = document.getElementsByName(name)[0];
        if (input && input.value && !/^\d{10}$/.test(input.value)) {
            alert(`Invalid mobile number in "${name.replace(/_/g, ' ')}". It must be a 10-digit number.`);
            input.focus();
            return false;
        }
    }

    // Validate email (simple email format check)
    const emailField = document.getElementsByName('student_email')[0];
    if (emailField && emailField.value && !/\S+@\S+\.\S+/.test(emailField.value)) {
        alert("Please enter a valid email address.");
        emailField.focus();
        return false;
    }

    // Validate student's age (should be >= 5 years and <= 20 years)
    const dobField = document.getElementsByName('student_date_of_birth')[0];
    if (dobField && dobField.value) {
        const dob = new Date(dobField.value);
        const today = new Date();
        const age = today.getFullYear() - dob.getFullYear();
        const month = today.getMonth() - dob.getMonth();
        if (month < 0 || (month === 0 && today.getDate() < dob.getDate())) {
            age--;
        }

        if (age < 5 || age > 20) {
            alert("Student age should be between 5 and 20 years.");
            dobField.focus();
            return false;
        }
    }

    // If all validations pass, return true to submit the form
    return true;
}
