function showPassword(){
    var inputPass = document.getElementById('password');
    var btnShowPass = document.getElementById('btn-password');

    if(inputPass.type === 'password'){
        inputPass.setAttribute('type','text');
        btnShowPass.classList.remove('bi-eye-fill');
        btnShowPass.classList.add('bi-eye-slash-fill');
    } else {
        inputPass.setAttribute('type','password');
        btnShowPass.classList.remove('bi-eye-slash-fill');
        btnShowPass.classList.add('bi-eye-fill');
    }
}
