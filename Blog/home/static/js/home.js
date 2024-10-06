
document.forms.HomeForm.onsubmit = (e)=>{
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/");
    let formData = new FormData(document.forms.HomeForm);
    // xhr.setRequestHeader("MessageFromHome", "application/x-www-form-urlencoded")
    
    xhr.send(formData);
}