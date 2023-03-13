const form = document.getElementById("mylogin");

form.addEventListener("submit", function(event) { 
    event.preventDefault();

    const ususario = document.getElementById("inputUsername").value.trim();
    const pass = document.getElementById("inputPassw").value.trim();

    // console.log(cuatri);

    if (ususario === ""){
        alert("introduce tu usuario ");
        return;
    }
    if (pass === ""){
        alert("introduce tu contraseña");
        return;
    }

    form.submit();
});