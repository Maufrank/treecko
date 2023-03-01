const filtro = document.querySelector('#inputFiltro');
const con = document.querySelector('#filtrar');
let permiso = document.querySelector('#permiso');

console.log(filtro.value);

filtro.addEventListener('change', () =>{
    console.log(filtro.value);
    switch (filtro.value) {
        case "Periodo":
          con.innerHTML = " <label for='inputPeriodo' class='form-label'>Selecciona el periodo</label> <select id='inputPeriodo' class='form-select'><option selected>Sin periodo</option><option>2023 A</option><option>2023 B</option><option>2023 C</option></select>";
          break;
        case "Division":
            con.innerHTML = "<label for='inputPeriodo' class='form-label'>Selecciona la division</label><select id='inputDivision' class='form-select'><option selected value='SF'>Sin division</option><option value='TIC'>TIC</option><option value='Agronomia'>Agronomia</option><option value='Contaduria'>Contaduria</option><option value='Construcción'>Construcción</option>";
        break;
        case "Carrera":
            con.innerHTML = "";
        break;
        case "SF":
            con.innerHTML = "";
        break;
        default:
            break;
            
    }
});
