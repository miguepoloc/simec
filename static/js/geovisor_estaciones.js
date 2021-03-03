var latitud;
var longitud;
var latlng = [];
var marker;
$(document).ready(function () {
    // var latlng = L.latLng(latitud, longitud);
    var map = L.map('geovisor_estaciones', { attributionControl: false }).
        setView([12, -76],
            5);

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
        maxZoom: 18
    }).addTo(map);
    L.control.scale().addTo(map);
    var boyaIcon = L.icon({
        iconUrl: '/static/img/boya.png',
        // shadowUrl: 'leaf-shadow.png',

        iconSize: [11.9, 23.8], // size of the icon
        // shadowSize: [50, 64], // size of the shadow
        iconAnchor: [10, 10], // point of the icon which will correspond to marker's location
        // shadowAnchor: [4, 62],  // the same for the shadow
        popupAnchor: [0, 0] // point from which the popup should open relative to the iconAnchor
    });

    $.get('/api/Estacion/', function (result) {
        // Guarda en la variable estacion los resultados de la API
        estacion = result;
        console.log(estacion);
        for (let index = 0; index < estacion.length; index++) {
            console.log(estacion[index].id);
            latitud = estacion[index].latitud;
            longitud = estacion[index].longitud;
            nombre = estacion[index].nombre;
            if (latitud == null) {
                console.log("NADA");
            } else {
                marker = L.marker([latitud, longitud], { icon: boyaIcon }).addTo(map);
                marker.bindPopup("<b>" + nombre + "</b><br>Soy una estación");
            }

        }
    });
});
