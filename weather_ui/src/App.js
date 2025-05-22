import { useNavigate } from 'react-router-dom';
import logo from './logo.svg';
import WeatherImage from './image_weather.png';
import './App.css';

function App() {
  const navigate = useNavigate();

  return (
    <div className="App">
      {/* Navigation Bar */}
      <nav className="navbar">
        <div className="nav-logo">
          <img src={logo} className="nav-logo-img" alt="Logo" />
          <span>WeatherAI</span>
        </div>
        <div className="nav-buttons">
          <button 
            className="nav-button prediction-btn"
            onClick={() => navigate('/prediction')}
          >
            Prediction
          </button>
          <button 
            className="nav-button dashboard-btn"
            onClick={() => navigate('/dashboard')}
          >
            Dashboard
          </button>
        </div>
      </nav>

      {/* Main */}
      <header className="App-header">
        <img src={logo} className="App-logo" alt="React logo" />

        <h1 className="App-title">Weather Prediction System</h1>
        
        <div className="content-container">
          <div className="text-content">
            <h2>Overview</h2>
            <p>
  Understanding the critical role of weather forecasting in daily life and the potential of machine learning models and scalable deployment, our team developed the project <strong>“Machine Learning-Based Weather Forecasting on Docker Cluster.”</strong> This research aims to build and evaluate an LSTM-based deep learning model using the
  <a
  href="https://www.kaggle.com/datasets/selfishgene/historical-hourly-weather-data/data"
  target="_blank"
  rel="noopener noreferrer"
  style={{ color: '#61dafb', textDecoration: 'none' }}
>
  “Historical Hourly Weather Data 2012-2017”
</a> from Kaggle, then deploy the model on a Docker Cluster to assess scalability, environmental consistency, and system performance.
</p>


          </div>
          <div className="image-content">
            <img src={WeatherImage} alt="Weather illustration" className="project-image" />
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;