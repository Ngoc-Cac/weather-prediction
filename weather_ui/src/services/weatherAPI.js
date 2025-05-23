// Map
export const CITY_COORDINATES = {
  // Canada
  'Montreal': [45.508839, -73.587807],
  'Toronto': [43.700111, -79.416298],
  'Vancouver': [49.24966, -123.119339],

  // Israel
  'Beersheba': [31.25181, 34.791302],
  'Eilat': [29.55805, 34.948212],
  'Haifa': [32.815559, 34.98917],
  'Jerusalem': [31.769039, 35.216331],
  'Nahariyya': [33.005859, 35.09409],
  'Tel Aviv District': [32.083328, 34.799999],

  // United States
  'Albuquerque': [35.084492, -106.651138],
  'Atlanta': [33.749001, -84.387978],
  'Boston': [42.358429, -71.059769],
  'Charlotte': [35.227089, -80.843132],
  'Chicago': [41.850029, -87.650047],
  'Dallas': [32.783058, -96.806671],
  'Denver': [39.739151, -104.984703],
  'Detroit': [42.331429, -83.045753],
  'Houston': [29.763281, -95.363274],
  'Indianapolis': [39.768379, -86.158043],
  'Jacksonville': [30.33218, -81.655647],
  'Kansas City': [39.099731, -94.578568],
  'Las Vegas': [36.174969, -115.137222],
  'Los Angeles': [34.052231, -118.243683],
  'Miami': [25.774269, -80.193657],
  'Minneapolis': [44.979969, -93.26384],
  'Nashville': [36.16589, -86.784439],
  'New York': [40.714272, -74.005966],
  'Philadelphia': [39.952339, -75.163788],
  'Phoenix': [33.44838, -112.074043],
  'Pittsburgh': [40.44062, -79.995888],
  'Portland': [45.523449, -122.676208],
  'Saint Louis': [38.62727, -90.197891],
  'San Antonio': [29.42412, -98.493629],
  'San Diego': [32.715328, -117.157257],
  'San Francisco': [37.774929, -122.419418],
  'Seattle': [47.606209, -122.332069],

  // Vietnam
  'Da Nang': [16.047079, 108.20623],
  'Hanoi': [21.028511, 105.804817],
  'Ho Chi Minh City': [10.762622, 106.660172],
};



// Celsius to Kelvin
function celsiusToKelvin(c) {
  return c + 273.15;
}

// Kelvin to Celsius
function kelvinToCelsius(k) {
  return k - 273.15;
}

export const predictWeather = async (selectedCity, weatherData) => {
  if (!CITY_COORDINATES[selectedCity]) {
    throw new Error('Vui lòng chọn thành phố hợp lệ');
  }

  // Tạo payload đúng cấu trúc mà FastAPI mong đợi
  const payload = {
    city_coords: CITY_COORDINATES[selectedCity],
    day_1: formatDayData(weatherData[0]),
    day_2: weatherData[1] ? formatDayData(weatherData[1]) : null,
    day_3: weatherData[2] ? formatDayData(weatherData[2]) : null,
  };

  console.log("Sending payload:", JSON.stringify(payload, null, 2));

  try {
    const response = await fetch('http://localhost:8000/predict_weather/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    console.log(response);

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || "Lỗi từ server");
    }

    const result = await response.json();
    return {
      temperature: kelvinToCelsius(result.temperature).toFixed(1),
      humidity: result.humidity.toFixed(1),
      pressure: result.pressure.toFixed(1),
      wind_speed: result.wind_speed.toFixed(1),
      wind_direction: result.wind_direction.toFixed(1),
    };
  } catch (error) {
    console.error('API Error:', error);
    throw new Error(`Lỗi kết nối: ${error.message}`);
  }
};

// Hàm chuẩn hóa dữ liệu ngày
function formatDayData(day) {
  if (
    (day.temperature === "") || (day.humidity==="") || (day.pressure==="") || 
      (day.wind_speed==="") || (day.wind_direction==="")
  ) {
     alert('There is one day is missing data! This day will be skipped.');
     return null;
  }


  
  return {
    humidity: parseFloat(day.humidity),
    pressure: parseFloat(day.pressure),
    temperature: celsiusToKelvin(parseFloat(day.temperature)),
    wind_direction: parseFloat(day.wind_direction),
    wind_speed: parseFloat(day.wind_speed)
  };
}