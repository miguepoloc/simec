// --------------- PARA EL MÉTODO POST -----------
// Token necesario para que funcione el método POST
var csrftoken = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$("#nueva_salida").click(function () {
    var fecha_inicio = document.getElementById('fecha_inicial').value;
    fecha_inicio = convertir_fecha(fecha_inicio);
    console.log(fecha_inicio);
    var fecha_fin = document.getElementById('fecha_final').value;
    fecha_fin = convertir_fecha(fecha_fin);
    console.log(fecha_fin);
    // Estación
    $.ajax({
        type: "POST",
        url: "/remo/api/Calendario_Salida_De_Campo/",
        data: {
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin,
            "observaciones": document.getElementById('observaciones_estacion').value,
            "estacion": document.getElementById('select_estacion').value,
            "tipo_de_salida": document.getElementById('select_estacion_tipo').value,
        }
    });
    location.reload();
});

function convertir_fecha(fecha) {
    anio = fecha.slice(0, 4);
    mes = fecha.slice(5, 7);
    dia = fecha.slice(8, 10);
    return (nueva_fecha = anio + "-" + mes + "-" + dia);
}

