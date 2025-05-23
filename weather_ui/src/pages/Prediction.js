// src/pages/Prediction.js
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import logo from '../logo.svg'; 
import '../App.css';  

const cities = [
  "Vancouver", "Portland", "San Francisco", "Seattle", "Los Angeles",
  "San Diego", "Las Vegas", "Phoenix", "Albuquerque", "Denver",
  "San Antonio", "Dallas", "Houston", "Kansas City", "Minneapolis",
  "Saint Louis", "Chicago", "Nashville", "Indianapolis", "Atlanta",
  "Detroit", "Jacksonville", "Charlotte", "Miami", "Pittsburgh",
  "Toronto", "Philadelphia", "New York", "Montreal", "Boston",
  "Beersheba", "Tel Aviv District", "Eilat", "Haifa", "Nahariyya", "Jerusalem"
];

function Prediction() {
  const navigate = useNavigate();
  const [selectedCity, setSelectedCity] = useState('');
  const [inputData, setInputData] = useState(Array(7).fill().map(() => ({
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

  const handlePredict = () => {
    const mockResult = {
      temperature: "24°C",
      humidity: "65%",
      conditions: "Sunny",
      recommendation: "Perfect weather for outdoor activities"
    };
    setPredictionResult(mockResult);
  };

  return (
    <div className="prediction-page">
      {/* Navigation Bar với 3 nút */}
      <nav className="navbar">
        <div className="nav-logo">
          <img src={logo} className="nav-logo-img" alt="Logo" />
          <span>WeatherAI</span>
        </div>
        <div className="nav-buttons">
          <button 
            className="nav-button main-btn"
            onClick={() => navigate('/')} // Về trang chủ
          >
            Main Page
          </button>
          <button 
            className="nav-button dashboard-btn"
            onClick={() => navigate('/dashboard')} // Đến Dashboard
          >
            Dashboard
          </button>
        </div>
      </nav>

      <main className="prediction-container">
        <h1 className="prediction-title">Weather Prediction</h1>
        
        <div className="prediction-guide">
          <p>Please enter weather data for 7 consecutive days to get accurate prediction:</p>
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
            <div>Wind Speed (km/h)</div>
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