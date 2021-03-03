var latitud;
var longitud;
$(document).ready(function () {
    id_estacion = document.getElementById("id_estacion")
    //Obtiene los datos de la estacion de la API
    console.log(id_estacion.text);
    $.get('/api/Estacion/', function (result) {
        // Guarda en la variable estacion los resultados de la API
        estacion = result;
        console.log(estacion);
        for (let index = 0; index < estacion.length; index++) {
            console.log(estacion[index].id);
            if (estacion[index].id == parseInt(id_estacion.text)) {
                latitud = estacion[index].latitud;
                longitud = estacion[index].longitud;
                nombre = estacion[index].nombre;
            }
        }
        var latlng = L.latLng(latitud, longitud);
        var map = L.map('geovisor', { attributionControl: false }).
            setView([latitud, longitud],
                14);

        L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
            maxZoom: 18
        }).addTo(map);

        L.control.scale().addTo(map);
        var boyaIcon = L.icon({
            iconUrl: '/static/img/boya.png',
            // shadowUrl: 'leaf-shadow.png',

            iconSize: [14, 28], // size of the icon
            // shadowSize: [50, 64], // size of the shadow
            iconAnchor: [0, 0], // point of the icon which will correspond to marker's location
            // shadowAnchor: [4, 62],  // the same for the shadow
            popupAnchor: [0, 0] // point from which the popup should open relative to the iconAnchor
        });
        var marker = L.marker([latitud, longitud], { icon: boyaIcon }).addTo(map);
        marker.bindPopup("<b>" + nombre + "</b><br>Soy una estación");
        // L.marker([latitud, longitud], { draggable: true }).addTo(map);
    });

});

