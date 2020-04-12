const pw = document.getElementById("passwordsignin");
const cpw = document.getElementById("confirmpasswordsignin");
const emess = document.getElementById("passwordErrorText");
const ButSignin = document.getElementById("signinsubmit");


cpw.oninput = function () {
    if (cpw.value !== pw.value){
        emess.textContent = "Senhas diferentes!";
        ButSignin.disabled = true;
    } else {
        ButSignin.disabled = false;
        emess.textContent = "";
    }
};

pw.oninput = function () {
    if (cpw.value !== pw.value && cpw.value !== ''){
        emess.textContent = "Senhas diferentes!";
        ButSignin.disabled = true;
    } else {
        ButSignin.disabled = false;
        emess.textContent = "";
    }
};
