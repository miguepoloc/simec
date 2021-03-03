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


// Adquiere el listado de los componentes, sensores y estaciones
var lista_componentes_estacion = "";

$.get('/api/Componente_Estacion/', function (result) {
    lista_componentes_estacion = result;
    console.log("Lista Componentes Estación: ");
    console.log(lista_componentes_estacion);
});

var lista_componentes = "";

$.get('/api/Componente/', function (result) {
    lista_componentes = result;
    console.log("Lista Componentes: ");
    console.log(lista_componentes);
});

var lista_sensores_estacion = "";

$.get('/api/Sensor_Estacion/', function (result) {
    lista_sensores_estacion = result;
    console.log("Lista Sensores Estación: ");
    console.log(lista_sensores_estacion);

});

var lista_sensores = "";

$.get('/api/Sensor/', function (result) {
    lista_sensores = result;
    console.log("Lista Sensores: ");
    console.log(lista_sensores);
});

var lista_tipo = "";

$.get('/api/Tipo_Salida_De_Campo/', function (result) {
    lista_tipo = result;
    console.log("Lista Tipo de salida: ");
    console.log(lista_tipo);
});

// Agregar un nuevo componente
var cant_componentes = 0;
var add_componente = document.getElementById('agregar_componente');
$("#addComponente").click(function () {
    let htmlx = "";
    htmlx += '<div class="card card-primary" id="card_c' + cant_componentes + '">';
    htmlx += '<div class="card-header">';
    htmlx += '<h3 class="card-title" id="nombre_componente' + cant_componentes + '"><i class="fas fa-tools"></i> Componente ' + cant_componentes + '</h3>';
    htmlx += '<div class="card-tools">';
    htmlx += '<button type="button" class="btn btn-tool" data-card-widget="collapse">';
    htmlx += '<i class="fas fa-minus"></i>';
    htmlx += '</button>';
    htmlx += '</div>';
    htmlx += '</div>';
    htmlx += '<div class="card-body">';
    htmlx += '<div class="form-group">';
    htmlx += '<label>Componente ' + cant_componentes + '</label>';
    htmlx += '<select class="form-control select2" style="width: 100%;" id="select_componente' + cant_componentes + '">';
    htmlx += '<option selected="selected" disabled="disabled">Selecciona un componente</option>';
    htmlx += '</select>';
    htmlx += '<label>Tipo de salida</label>';
    htmlx += '<select class="form-control select2" style="width: 100%;" required id="select_componente_tipo' + cant_componentes + '">';
    htmlx += '<option selected="selected" disabled="disabled">Selecciona el tipo de salida</option>';
    for (let index = 0; index < lista_tipo.length; index++) {
        htmlx += '<option value="' + lista_tipo[index].id + '">' + lista_tipo[index].tipo + '</option>';
    }
    htmlx += '</select>';
    htmlx += '</div>';
    htmlx += '<div class="form-group">';
    htmlx += '<label>Observaciones</label>';
    htmlx += '<textarea class="form-control" rows="3" cols="200" placeholder="Ingrese las actividades realizadas durante la salida de campo" id="observaciones_componente' + cant_componentes + '"></textarea>';
    htmlx += '</div>';
    htmlx += '</div>';
    htmlx += '</div>';
    htmlx += '</div>';
    add_componente.insertAdjacentHTML('afterend', htmlx);
    cant_componentes = cant_componentes + 1;
});


// Agregar un nuevo sensor
var cant_sensores = 0;
var add_sensor = document.getElementById('agregar_sensor');
$("#addSensor").click(function () {
    let htmlx = "";
    htmlx += '<div class="card card-primary" id="card_s' + cant_sensores + '">';
    htmlx += '<div class="card-header">';
    htmlx += '<h3 class="card-title" id="nombre_sensor' + cant_sensores + '"><i class="fas fa-cloud-sun-rain"></i> Sensor ' + cant_sensores + '</h3>';
    htmlx += '<div class="card-tools">';
    htmlx += '<button type="button" class="btn btn-tool" data-card-widget="collapse">';
    htmlx += '<i class="fas fa-minus"></i>';
    htmlx += '</button>';
    htmlx += '</div>';
    htmlx += '</div>';
    htmlx += '<div class="card-body">';
    htmlx += '<div class="form-group">';
    htmlx += '<label>Sensor ' + cant_sensores + '</label>';
    htmlx += '<select class="form-control select2" style="width: 100%;" id="select_sensor' + cant_sensores + '">';
    htmlx += '<option selected="selected" disabled="disabled">Selecciona un sensor</option>';
    htmlx += '</select>';
    htmlx += '<label>Tipo de salida</label>';
    htmlx += '<select class="form-control select2" style="width: 100%;" required id="select_sensor_tipo' + cant_sensores + '">';
    htmlx += '<option selected="selected" disabled="disabled">Selecciona el tipo de salida</option>';
    for (let index = 0; index < lista_tipo.length; index++) {
        htmlx += '<option value="' + lista_tipo[index].id + '">' + lista_tipo[index].tipo + '</option>';
    }
    htmlx += '</select>';
    htmlx += '</div>';
    htmlx += '<div class="form-group">';
    htmlx += '<label>Observaciones</label>';
    htmlx += '<textarea class="form-control" rows="3" cols="200" placeholder="Ingrese las actividades realizadas durante la salida de campo" id="observaciones_sensor' + cant_sensores + '"></textarea>';
    htmlx += '</div>';
    htmlx += '</div>';
    htmlx += '</div>';
    htmlx += '</div>';
    add_sensor.insertAdjacentHTML('afterend', htmlx);
    cant_sensores = cant_sensores + 1;
});


// ----------- Select de estación -------------------
var estacion_selecta = "";
$('#select_estacion').on('select2:select', function (e) {
    for (let index = 0; index < cant_sensores; index++) {
        document.getElementById("select_sensor" + index).innerHTML = "<option selected='selected' disabled='disabled'>Selecciona un sensor</option>";
        document.getElementById('nombre_sensor' + index).innerHTML = '<i class="fas fa-cloud-sun-rain"></i> Sensor';
    }
    for (let index = 0; index < cant_componentes; index++) {
        document.getElementById("select_componente" + index).innerHTML = "<option selected='selected' disabled='disabled'>Selecciona un componente</option>";
        document.getElementById('nombre_componente' + index).innerHTML = '<i class="fas fa-tools"></i> Componente';
    }

    var data_estacion = e.params.data;
    estacion_selecta = data_estacion.id;
    document.getElementById('nombre_estacion').innerHTML = '<i class="fas fa-broadcast-tower"></i> ' + data_estacion.text;
    // Se recorren todas las posiciones del vector que contiene a los componente
    for (let index = 0; index < cant_componentes; index++) {
        for (i = 0; i < lista_componentes_estacion.length; i++) {
            if (lista_componentes_estacion[i].ubicacion == estacion_selecta) {
                for (j = 0; j < lista_componentes.length; j++) {
                    if (lista_componentes[j].id == lista_componentes_estacion[i].componente) {
                        console.log(lista_componentes[j].nombre + " id: " + lista_componentes_estacion[i].id);
                        // Se crea un elemento tipo option
                        let z = document.createElement("option");
                        // Al cual se le asigna el valor de la variable
                        z.setAttribute("value", lista_componentes_estacion[i].id);
                        // Y se le asigna al valor a mostrar
                        let t = document.createTextNode(lista_componentes[j].nombre + " (" + lista_componentes[j].referencia + ")");
                        z.appendChild(t);
                        // Luego se añade al html
                        document.getElementById("select_componente" + index).appendChild(z);
                    }
                }
            }
        }
    }
    for (let index = 0; index < cant_sensores; index++) {
        for (i = 0; i < lista_sensores_estacion.length; i++) {
            if (lista_sensores_estacion[i].ubicacion == estacion_selecta) {
                for (j = 0; j < lista_sensores.length; j++) {
                    if (lista_sensores[j].id == lista_sensores_estacion[i].sensor) {
                        console.log(lista_sensores[j].nombre + " id: " + lista_sensores_estacion[i].id);
                        // Se crea un elemento tipo option
                        let z = document.createElement("option");
                        // Al cual se le asigna el valor de la variable
                        z.setAttribute("value", lista_sensores_estacion[i].id);
                        // Y se le asigna al valor a mostrar
                        let t = document.createTextNode(lista_sensores[j].nombre + " (" + lista_sensores[j].unidad + ")");
                        z.appendChild(t);
                        // Luego se añade al html
                        document.getElementById("select_sensor" + index).appendChild(z);
                    }
                }
            }
        }
    }
});

var data_tipo_estacion;
$('#select_estacion_tipo').on('select2:select', function (e) {
    data_tipo_estacion = e.params.data.id;
});

var operarios = [];
var data_operarios_add;
$('#select_operario').on('select2:select', function (e) {
    data_operarios_add = e.params.data;
    operarios.push(data_operarios_add.id);
});

var data_operarios_delete;
$('#select_operario').on('select2:unselect', function (e) {
    data_operarios_delete = e.params.data.id;
    pos = operarios.indexOf(data_operarios_delete);
    let elementoEliminado = operarios.splice(pos, 1)
});

// ----------------- Cuando selecciona un componente ----------------------
var data_componente;
$('#select_componente').on('select2:select', function (e) {
    data_componente = e.params.data;
});

var data_tipo_componente;
$('#select_componente_tipo').on('select2:select', function (e) {
    data_tipo_componente = e.params.data.id;
});

// ----------------- Cuando selecciona un sensor ----------------------
var data_sensor;
$('#select_sensor').on('select2:select', function (e) {
    data_sensor = e.params.data;
    document.getElementById('nombre_sensor').innerHTML = '<i class="fas fa-cloud-sun-rain"></i> ' + data_sensor.text;
});

var data_tipo_sensor;
$('#select_sensor_tipo').on('select2:select', function (e) {
    data_tipo_sensor = e.params.data.id;
});


$("#deleteComponente").click(function () {
    if (cant_componentes > 0) {
        $("#card_c" + (cant_componentes - 1)).remove();
        cant_componentes = cant_componentes - 1;
    }
});

$("#deleteSensor").click(function () {
    if (cant_sensores > 0) {
        $("#card_s" + (cant_sensores - 1)).remove();
        cant_sensores = cant_sensores - 1;
    }
});

// Botón de agregar a la base de datos
$("#agregar").click(function () {
    var fecha = document.getElementById('fecha_salida').value;
    fecha = convertir_fecha(fecha);

    // var observaciones_sensor = document.getElementById('observaciones_sensor').value;

    // Componente
    for (let index = 0; index < cant_componentes; index++) {
        console.log("Componente: " + document.getElementById('select_componente' + index).value);
        $.ajax({
            type: "POST",
            url: "/api/Componente_Salida_De_Campo/",
            data: {
                "fecha": fecha,
                "observaciones": document.getElementById('observaciones_componente' + index).value,
                "componente": document.getElementById('select_componente' + index).value,
                "tipo_de_salida": document.getElementById('select_componente_tipo' + index).value,
                "operarios": operarios,
            }
        });
    }

    // Sensor
    for (let index = 0; index < cant_sensores; index++) {
        console.log("Sensores: " + document.getElementById('select_sensor' + index).value);
        $.ajax({
            type: "POST",
            url: "/api/Sensor_Salida_De_Campo/",
            data: {
                "fecha": fecha,
                "observaciones": document.getElementById('observaciones_sensor' + index).value,
                "sensor": document.getElementById('select_sensor' + index).value,
                "tipo_de_salida": document.getElementById('select_sensor_tipo' + index).value,
                "operarios": operarios,
            }
        });
    }


    // Estación
    $.ajax({
        type: "POST",
        url: "/api/Salida_De_Campo/",
        data: {
            "fecha": fecha,
            "observaciones": document.getElementById('observaciones_estacion').value,
            "estacion": estacion_selecta,
            "tipo_de_salida": data_tipo_estacion,
            "operarios": operarios,
        }
    });
});

function convertir_fecha(fecha) {
    anio = fecha.slice(0, 4);
    mes = fecha.slice(5, 7);
    dia = fecha.slice(8, 10);
    return (nueva_fecha = anio + "-" + mes + "-" + dia);
}