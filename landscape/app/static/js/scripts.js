// Datos iniciales para el mapa
var data = [{
    type: 'scattermapbox',
    lat: [],
    lon: [],
    mode: 'markers',
    marker: {size: 12, color: 'blue'}
}];

// Configuración inicial del mapa
var layout = {
    mapbox: {
        style: 'open-street-map',
        center: { lat: 0, lon: 0 },
        zoom: 2
    },
    margin: {t: 0, b: 0}, // Remover márgenes innecesarios
    width: 600,
    height: 400
};

// Renderizar el mapa
Plotly.newPlot('map', data, layout).then(function() {
    var mapDiv = document.getElementById('map');

    // Usar un pequeño retraso para asegurar que el mapa se haya cargado completamente
    setTimeout(function() {
        // Obtener el objeto mapbox desde el gráfico renderizado por Plotly
        var mapbox = mapDiv._fullLayout.mapbox._subplot.map;

        if (mapbox) {
            // Añadir evento 'click' en el mapa de Mapbox
            mapbox.on('click', function(e) {
                var lat = e.lngLat.lat;
                var lon = e.lngLat.lng;

                // Actualizar los inputs de latitud y longitud
                document.getElementById('lat').value = lat;
                document.getElementById('lon').value = lon;

                // Agregar el marcador en la posición clicada
                Plotly.extendTraces('map', {
                    lat: [[lat]],
                    lon: [[lon]]
                }, [0]);
            });
        } else {
            console.error("Error: No se pudo obtener el objeto Mapbox.");
        }
    }, 500); // Retraso de 500ms para asegurar que el mapa esté cargado
});
