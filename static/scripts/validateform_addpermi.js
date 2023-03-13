const form = document.getElementById("mypermiso");

form.addEventListener("submit", function(event) { 
    event.preventDefault();

    const motivo = document.getElementById("inputMotivo").selectedIndex;
    const descripcion = document.getElementById("inputDescripcion").value.trim();
    const fecha = document.getElementById("inputFechaInicial").value.trim();
    const comprobante = document.getElementById("inputComprobante").value.trim();

    // console.log(cuatri);

    if (motivo === 0){
        alert("se te olvido tu motivo!, seleccionalo porfavor ");
        return;
    }
    if (descripcion === ""){
        alert("introduce tu Descripcion");
        return;
    }
    if (fecha === ""){
        alert("se te olvido la fecha? ");
        return;
    }
    if (comprobante === ""){
        alert("selecciona tu comprobante");
        return;
    }

    form.submit();
});