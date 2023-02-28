const orden = document.querySelector('#orden');
const con = document.querySelector('#arpermisos');
let permiso = document.querySelector('#permiso');

console.log(orden.value);

orden.addEventListener('change', () =>{
    console.log(orden.value);
    switch (orden.value) {
        case "fecha":
            con.innerHTML = "<section id='permiso'><h4>Sergio Amaury Montiel Torres</h4><h4>Motivo: Medico</h4><section id='gg'><h4>Grado: 5</h4><h4>Grupo: C</h4></section></section>" ;
            con.innerHTML += "<section id='permiso' style='background-color:  grey'><h4>Andy Garcia Gonzalez</h4><h4>Motivo: Medico</h4><section><h4>Grado: 5</h4><h4>Grupo: C</h4></section></section>";
            con.innerHTML += "<section id='permiso' style='background-color:  red'><h4>Andy Garcia Gonzalez</h4><h4>Motivo: Medico</h4><section><h4>Grado: 5</h4><h4>Grupo: C</h4></section></section>";
            break;
        case "pendiente":
            con.innerHTML = "<section id='permiso' style='background-color:  grey'><h4>Andy Garcia Gonzalez</h4><h4>Motivo: Medico</h4><section><h4>Grado: 5</h4><h4>Grupo: C</h4></section></section>";
        break;
        case "rechazado":
            con.innerHTML = "<section id='permiso' style='background-color:  red'><h4>Andy Garcia Gonzalez</h4><h4>Motivo: Medico</h4><section><h4>Grado: 5</h4><h4>Grupo: C</h4></section></section>";
        break;
        case "aprobado":
            con.innerHTML = "<section id='permiso'><h4>Sergio Amaury Montiel Torres</h4><h4>Motivo: Medico</h4><section id='gg'><h4>Grado: 5</h4><h4>Grupo: C</h4></section></section>" ;
        break;
    
        default:
            break;
            
    }
});

permiso.addEventListener('click', () =>{
    console.log("hola");
    location.href = "consultaal.html";
});