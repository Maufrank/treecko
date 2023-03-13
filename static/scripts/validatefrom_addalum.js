const form = document.getElementById("myform");

form.addEventListener("submit", function(event) { 
    event.preventDefault();

    const name = document.getElementById("inputNombre").value.trim();
    const apellidos = document.getElementById("inputApellidos").value.trim();
    const email = document.getElementById("inputCorreo").value.trim();
    const username = document.getElementById("inputUsername").value.trim();
    const pass = document.getElementById("inputPassword").value.trim();
    const repetpass = document.getElementById("inputRepetPassword").value.trim();
    const cuatri = document.getElementById("inputCuatrimestre").selectedIndex;
    const carrera = document.getElementById("inputCarrera").selectedIndex;
    const grupo = document.getElementById("inputGrupo").selectedIndex;
    console.log(cuatri);
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
    if (cuatri === 0){
        alert("selecciona tu cuatrimestre");
        return;
    }
    if (carrera === 0){
        alert("selecciona tu carrera");
        return;
    }
    if (grupo === 0){
        alert("selecciona tu grupo");
        return;
    }

    form.submit();
});