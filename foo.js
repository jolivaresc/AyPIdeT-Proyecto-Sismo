// Create map



function initMap() {
  // Map options
  var options = {
    zoom: 8,
    center: { lat: 19.4326, lng: -99.1332 }
  }

  // New map
  var map = new google.maps.Map(document.getElementById('map'), options);


  // Array of markers
  var markers = [
    {
      coords: { lat: 19.3189, lng: -99.1844 },
      iconImage: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
      content: '<h>CU</h>'
    },
    {
      coords: { lat: 19.4978, lng: -99.1748 },
      content: '<h>Arena</h>'
    },
    {
      coords: { lat: 19.4352, lng: -99.1412 },
      content: '<h>Bellas Artes</h>'
    }
  ];

  // Loop through markers
  for (var i = 0; i < markers.length; i++) {
    // Add marker
    addMarker(markers[i]);
  }

  // capturar campo
  var locationForm = document.getElementById('location-form');

  // Listen for submit
  locationForm.addEventListener('submit', geocode);

  function geocode(e) {
    e.preventDefault();
    console.log("botonazo");
    var query_city = document.getElementById('location-input').value;
    console.log(query_city);
    document.getElementById('ltnlng').innerHTML = query_city;
    axios.get('https://maps.googleapis.com/maps/api/geocode/json', {
      params: {
        address: document.getElementById('ltnlng').innerHTML,
        key: 'AIzaSyBL5XV9C6bmq7oct5X0pkLHbEvtVwInQPg'
      }
    })
      .then(function (response) {
        console.log(response.data.results[0].address_components);
        var lat = response.data.results[0].geometry.location.lat;
        var lng = response.data.results[0].geometry.location.lng;
        var marker = {
          coords: {lat:lat,lng:lng},
          content: '<h>' + query_city +'</h>'
        }
        var geometryOutput = `
          <ul class="list-group">
            <li class="list-group-item"><strong>Latitude</strong>: ${lat}</li>
            <li class="list-group-item"><strong>Longitude</strong>: ${lng}</li>
          </ul>
        `;
        addMarker(marker);
        document.getElementById('ltnlng').innerHTML = geometryOutput;
      }
      )
  }


  // Add Marker Function
  function addMarker(props) {
    var marker = new google.maps.Marker({
      position: props.coords,
      map: map,
      //icon:props.iconImage
    });

    // Check for customicon
    if (props.iconImage) {
      // Set icon image
      marker.setIcon(props.iconImage);
    }

    // Check content
    if (props.content) {
      var infoWindow = new google.maps.InfoWindow({
        content: props.content
      });

      marker.addListener('click', function () {
        infoWindow.open(map, marker);
      });
    }
  }
}
