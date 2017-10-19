// Create map
var locationForm = document.getElementById('location-form');

// Listen for submit
locationForm.addEventListener('submit', geocode);

function geocode(){
	console.log("botonazo");
	console.log(document.getElementById('location-input').value);
	document.getElementById('ltnlng').innerHTML = document.getElementById('location-input').value;
	axios.get('https://maps.googleapis.com/maps/api/geocode/json',{
		params:{
			address:document.getElementById('ltnlng').innerHTML,
			key:'AIzaSyBL5XV9C6bmq7oct5X0pkLHbEvtVwInQPg'
			}
	})
	.then(function(response){
		console.log(response);
		var lat = response.data.results[0].geometry.location.lat;
        var lng = response.data.results[0].geometry.location.lng;
        var geometryOutput = `
          <ul class="list-group">
            <li class="list-group-item"><strong>Latitude</strong>: ${lat}</li>
            <li class="list-group-item"><strong>Longitude</strong>: ${lng}</li>
          </ul>
        `;
        document.getElementById('ltnlng').innerHTML = geometryOutput;
	}
	)
}

function initMap() {
  // Map options
  var options = {
    zoom: 10,
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
      content:'<h>Bellas Artes</h>'
    }
  ];

  // Loop through markers
  for (var i = 0; i < markers.length; i++) {
    // Add marker
    addMarker(markers[i]);
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
