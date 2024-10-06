
var h1error = document.querySelector("#error")

document.forms.LoginForm.onsubmit = (e)=>{
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    let formData = new FormData(document.forms.LoginForm);
    xhr.open("POST", "/user/login/");

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