
var h1error = document.querySelector("#error");

document.forms.RegistrForm.onsubmit = (e)=>{
    e.preventDefault();
    h1error.textContent = "";
    var xhr = new XMLHttpRequest();
    let formData = new FormData(document.forms.RegistrForm);
    xhr.open("POST", "/user/registration/")

    xhr.onload = function(){
        if (xhr.status >= 200 && xhr.status < 300){
            let response = JSON.parse(xhr.responseText);
            if (response.redirect_url){
                window.location.href = response.redirect_url;
            } else if (response.error){
                h1error.textContent = response.error;
            };
            
        };
    };

    xhr.send(formData);
};