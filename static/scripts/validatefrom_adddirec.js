const form = document.getElementById("mydirec");

form.addEventListener("submit", function(event) { 
    event.preventDefault();

    const name = document.getElementById("inputNombre").value.trim();
    const apellidos = document.getElementById("inputApellidos").value.trim();
    const email = document.getElementById("inputCorreo").value.trim();
    const username = document.getElementById("inputUsername").value.trim();
    const pass = document.getElementById("inputPassword").value.trim();
    const repetpass = document.getElementById("inputRepetPassword").value.trim();
    const periodo1 = document.getElementById("inputPeriodo").selectedIndex;
    const periodo2 = document.getElementById("inputPeriodof").selectedIndex;
    // const periodo = document.getElementById("inputPeriodo").selectedIndex;
    // console.log(cuatri);
    if (name === ""){
        alert("introduce tu nombre");
        return;
    }
    if (apellidos === ""){
        alert("introduce tu apellido");
        return;
    }
    if (email === ""){
        alert("introduce tu correo");
        return;
    }
    if (username === ""){
        alert("introduce tu ususario");
        return;
    }
    if (pass === ""){
        alert("introduce tu contraseña");
        return;
    }
    if (repetpass === ""){
        alert("confirma contraseña");
        return;
    }
    if (periodo1 === 0){
        alert("selecciona tu periodo inicial");
        return;
    }
    if (periodo2 === 0){
        alert("selecciona tu periodo final");
        return;
    }

    // form.submit();
});