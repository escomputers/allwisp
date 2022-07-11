// Use Signer from @aws-amplify/core
const { Signer } = window.aws_amplify_core;

// AWS Resources
// Cognito:
const identityPoolId = "eu-central-1:0155dfbd-31ca-43ca-86ec-ece0b638d417";
// Amazon Location Service resource names:
const mapName = "explore.map.def";
const placesName = "defaultidx";

// Extract the region from the Identity Pool ID
AWS.config.region = identityPoolId.split(":")[0];

// Instantiate a Cognito-backed credential provider
const credentials = new AWS.CognitoIdentityCredentials({
  IdentityPoolId: identityPoolId,
});

// Sign requests made by MapLibre GL JS using AWS SigV4:
function transformRequest(url, resourceType) {
  if (resourceType === "Style" && !url.includes("://")) {
    // Resolve to an AWS URL
    url = `https://maps.geo.${AWS.config.region}.amazonaws.com/maps/v0/maps/${url}/style-descriptor`;
  }

  if (url.includes("amazonaws.com")) {
    // Sign AWS requests (with the signature as part of the query string)
    return {
      url: Signer.signUrl(url, {
        access_key: credentials.accessKeyId,
        secret_key: credentials.secretAccessKey,
        session_token: credentials.sessionToken,
      }),
    };
  }

  // If not amazonaws.com, falls to here without signing
  return { url };
}

// Initialize a map
async function initializeMap() {
  // Load credentials and set them up to refresh
  await credentials.getPromise();
  
  // Initialize the map
  const mlglMap = new maplibregl.Map({
    container: "map", // HTML element ID of map element
    center: [-77.03674, 38.891602], // Initial map centerpoint
    zoom: 16, // Initial map zoom
    style: mapName,
    transformRequest,
  });

  // Add navigation control to the top left of the map
  mlglMap.addControl(new maplibregl.NavigationControl(), "top-left");
  
  return mlglMap;
}

async function main() {
  // Initialize map and AWS SDK for Location Service:
  const map = await initializeMap();
  const location = new AWS.Location({credentials, region: AWS.config.region});
  searchPoisTermTextBox = document.getElementById('pois-search-term');
  searchPoisForm = document.getElementById('search-pois-form');
  poiMarker = null;
  
  //***********FUNZIONE DI RICERCA SU "SUBMIT"*****************
  this.searchPoisForm.onsubmit = (e) => {
  e.preventDefault();
  
  const term = this.searchPoisTermTextBox.value.trim();
  
  // Set up parameters for search call
  var params = {
  Text: term,
  IndexName: placesName,
  };

  location.searchPlaceIndexForText(params, function(err, data) {
  if (err) {
  alert("There was an error searching.");
  } else {
  // Remove the previous marker
  if (poiMarker != null) {
  poiMarker.remove();
  poiMarker = null;
  }
  //Add new marker if there's at least one result
  const marker = new maplibregl.Marker().setLngLat(data.Results[0].Place.Geometry.Point).addTo(map);
  poiMarker = marker;
  map.flyTo({
  center: data.Results[0].Place.Geometry.Point
  });
  poiMarker.setPopup(new maplibregl.Popup({className: 'my-class'}).setHTML("<h5>" + data.Results[0].Place.Label + "</h5>"))
  }
  });
  
};

  //***********FUNZIONE SUGGERIMENTI RICERCA SU "KEYUP"*****************  
  this.searchPoisTermTextBox.onkeyup = (e) => {
  e.preventDefault();
  
  const term = this.searchPoisTermTextBox.value.trim();
  
  // Set up parameters for search call
  var params = {
  Text: term,
  IndexName: placesName,
  Language: "it",
  //MaxResults: "5"
  };

  location.searchPlaceIndexForSuggestions(params, function(err, data) {
  const res = document.getElementById("result");
  res.innerHTML = '';
  let list = '';
  for (let i = 0; i < data.Results.length; i++) {
  list += `<li data-value="${data.Results[i].Text}">${data.Results[i].Text}</li>`;
  }
  res.innerHTML = `<ul id="autocompletedlist">${list}</ul>`;
  document.getElementById("autocompletedlist").addEventListener('click', function(e) {
  // e.target is our targetted element.
  if(e.target && e.target.nodeName == 'LI') {
  document.getElementById('pois-search-term').value = e.target.getAttribute('data-value');
  document.getElementById('result').innerHTML = '';
  }
  });
 });
 }
 
}
main();