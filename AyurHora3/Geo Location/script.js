async function getLocationInfo() {
    const placeName = document.getElementById('placeName').value;
    if (!placeName) {
        alert("Please enter a place name.");
        return;
    }

    try {
        // Get latitude and longitude
        const geocodeResponse = await fetch(`https://nominatim.openstreetmap.org/search?q=${placeName}&format=json&limit=1`);
        const geocodeData = await geocodeResponse.json();

        if (geocodeData.length === 0) {
            alert("Could not find location.");
            return;
        }

        const { lat, lon } = geocodeData[0];

        // Get timezone
        const timezoneResponse = await fetch(`https://api.timezonedb.com/v2.1/get-time-zone?key=YOUR_API_KEY&format=json&by=position&lat=${lat}&lng=${lon}`);
        const timezoneData = await timezoneResponse.json();

        if (timezoneData.status !== "OK") {
            alert("Could not find timezone.");
            return;
        }

        const { gmtOffset, zoneName } = timezoneData;

        // Display the results
        document.getElementById('place').innerText = `Place: ${placeName}`;
        document.getElementById('latitude').innerText = `Latitude: ${lat}`;
        document.getElementById('longitude').innerText = `Longitude: ${lon}`;
        document.getElementById('gmtOffset').innerText = `GMT Offset: ${gmtOffset / 3600} hours`;
        document.getElementById('timezone').innerText = `Timezone: ${zoneName}`;
    } catch (error) {
        alert("An error occurred while fetching location info.");
        console.error(error);
    }
}
