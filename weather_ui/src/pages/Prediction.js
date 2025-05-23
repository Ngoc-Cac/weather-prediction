// src/pages/Prediction.js
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import { predictWeather, CITY_COORDINATES } from '../services/weatherAPI';
import logo from '../logo.svg'; 
import '../App.css';  

const cities = Object.keys(CITY_COORDINATES);

function checkTemp(val) {
  return val>= -273.15;
}

function checkHumid(val) {
  return val>=0 && val<=100;
}
function checkWindDirection(val) {
  return val>=0 && val<=360;
}
function checkWindSpeed(val) {
  return val>=0;
}

function Prediction() {
  const navigate = useNavigate();
  const [selectedCity, setSelectedCity] = useState('');
  const [inputData, setInputData] = useState(Array(2).fill().map(() => ({
    temperature: '',
    humidity: '',
    pressure: '',
    wind_speed: '',
    wind_direction: ''
  })));
  const [predictionResult, setPredictionResult] = useState(null);

  const handleInputChange = (dayIndex, field, value) => {
    const newData = [...inputData];
    newData[dayIndex][field] = value;
    setInputData(newData);
  };

  const handlePredict = async () => {
    if (!selectedCity) {
      alert("Please select a city.");
      return;
    }

    // Kiểm tra dữ liệu đầu vào
    console.log(inputData);
    
    const atleastone = ( 
      (inputData[0].temperature!== "") && (inputData[0].humidity !== "") && (inputData[0].pressure!== "") && 
      (inputData[0].wind_speed!== "") && (inputData[0].wind_direction!== "")
    );

    if (!atleastone) {
      alert("TPlease fill in all fields for at least one day.");
      return;
    }

    //temperature
    if (inputData[0].temperature!=="" && !checkTemp(parseFloat(inputData[0].temperature))){
      alert("The temperature must non-negative");
      return;
    }
    if (inputData[1].temperature!=="" && !checkTemp(parseFloat(inputData[1].temperature))){
      alert("The temperature must non-negative");
      return;
    }

    //humidity
    if (inputData[0].humidity!=="" && !checkHumid(parseFloat(inputData[0].humidity))){
      alert("The humidity must in range 0 to 100");
      return;
    }
    if (inputData[1].humidity!=="" && !checkHumid(parseFloat(inputData[1].humidity))){
      alert("The humidity must in range 0 to 100");
      return;
    }

    //wind direction
    if (inputData[0].wind_direction!=="" && !checkWindDirection(parseFloat(inputData[0].wind_direction))){
      alert("The wind direction in meteorological degrees (0 - 360)");
      return;
    }

    if (inputData[1].wind_direction!=="" && !checkWindDirection(parseFloat(inputData[1].wind_direction))){
      alert("The wind direction in meteorological degrees (0 - 360)");
      return;
    }

    //wind speed
    if (inputData[0].wind_speed!=="" && !checkWindSpeed(parseFloat(inputData[0].wind_speed))){
      alert("The wind speed must non-negative");
      return;
    }

    if (inputData[1].wind_speed!=="" && !checkWindSpeed(parseFloat(inputData[1].wind_speed))){
      alert("The wind speed must non-negative");
      return;
    }
    

    try {
      const result = await predictWeather(selectedCity, inputData);
      setPredictionResult({
        temperature: `${result.temperature}°C`,
        humidity: `${result.humidity}%`,
        conditions: "Predicted",
        recommendation: "Stay prepared!"
      });
    } catch (error) {
      console.error("Prediction error:", error);
      alert(error.message);
    }
  };


  return (
    <div className="prediction-page">
      {/* Navigation Bar với 3 nút */}
      <nav className="navbar">
        <div className="nav-logo">
          <img src={logo} className="nav-logo-img" alt="Logo" />
          <span>Weather Prediction with LSTM API</span>
        </div>
        <div className="nav-buttons">
          <button 
            className="nav-button main-btn"
            onClick={() => navigate('/')} // Về trang chủ
          >
            Main Page
          </button>
        </div>
      </nav>

      <main className="prediction-container">
        <h1 className="prediction-title">Weather Prediction</h1>
        
        <div className="prediction-guide">
          <p>Please enter weather data for 2 consecutive days to get accurate prediction:</p>
        </div>

        {/* Dropdown */}
        <div className="city-selector">
          <label htmlFor="city">Select City:</label>
          <select 
            id="city"
            value={selectedCity}
            onChange={(e) => setSelectedCity(e.target.value)}
          >
            <option value="">-- Select a City --</option>
            {cities.map(city => (
              <option key={city} value={city}>{city}</option>
            ))}
          </select>
        </div>

        {/* Input */}
        <div className="input-grid">
          <div className="grid-header">
            <div>Day</div>
            <div>Temperature (°C)</div>
            <div>Humidity (%)</div>
            <div>Pressure (hPa)</div>
            <div>Wind Speed (m/s)</div>
            <div>Wind Direction (°)</div>
          </div>
          
          {inputData.map((dayData, dayIndex) => (
            <div key={dayIndex} className="grid-row">
              <div>Day {dayIndex + 1}</div>
              <input
                type="number"
                value={dayData.temperature}
                onChange={(e) => handleInputChange(dayIndex, 'temperature', e.target.value)}
              />
              <input
                type="number"
                value={dayData.humidity}
                onChange={(e) => handleInputChange(dayIndex, 'humidity', e.target.value)}
              />
              <input
                type="number"
                value={dayData.pressure}
                onChange={(e) => handleInputChange(dayIndex, 'pressure', e.target.value)}
              />
              <input
                type="number"
                value={dayData.wind_speed}
                onChange={(e) => handleInputChange(dayIndex, 'wind_speed', e.target.value)}
              />
              <input
                type="number"
                value={dayData.wind_direction}
                onChange={(e) => handleInputChange(dayIndex, 'wind_direction', e.target.value)}
              />
            </div>
          ))}
        </div>

        {/* Predict */}
        <div className="predict-button-container">
          <button className="predict-button" onClick={handlePredict}>
            Predict Weather
          </button>
        </div>

        {/* Kết quả dự đoán */}
        {predictionResult && (
          <div className="prediction-result">
            <h2>Prediction Result for {selectedCity}</h2>
            <div className="result-grid">
              <div>
                <span className="result-label">Temperature:</span>
                <span className="result-value">{predictionResult.temperature}</span>
              </div>
              <div>
                <span className="result-label">Humidity:</span>
                <span className="result-value">{predictionResult.humidity}</span>
              </div>
              <div>
                <span className="result-label">Conditions:</span>
                <span className="result-value">{predictionResult.conditions}</span>
              </div>
              <div>
                <span className="result-label">Recommendation:</span>
                <span className="result-value">{predictionResult.recommendation}</span>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default Prediction;