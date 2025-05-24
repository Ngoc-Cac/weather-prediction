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
          <span>Weather Prediction with LSTM API</span>
        </div>
        <div className="nav-buttons">
          <button 
            className="nav-button prediction-btn"
            onClick={() => navigate('/prediction')}
          >
            Prediction
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

{/* Thêm nút GitHub Repository */}
            <div className="github-button-container">
              <a 
                href="https://github.com/Ngoc-Cac/weather-prediction" 
                target="_blank" 
                rel="noopener noreferrer"
                className="github-button"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" className="github-icon">
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
                GitHub Repository
              </a>
            </div>

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