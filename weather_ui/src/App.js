import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import logo from './logo.svg'; // Thêm dòng này
import './App.css';

function App() {
  const [projectDescription, setProjectDescription] = useState('');
  const navigate = useNavigate();

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="React logo" />
        
        <h1 className="App-title">Weather Prediction System</h1>
        
        <div className="project-input-container">
          <textarea
            className="project-input"
            placeholder="Nhập mô tả dự án của bạn..."
            value={projectDescription}
            onChange={(e) => setProjectDescription(e.target.value)}
            rows={5}
          />
        </div>

        <div className="action-buttons">
          <button 
            className="action-button prediction-btn"
            onClick={() => navigate('/prediction')}
          >
            Prediction
          </button>
          <button 
            className="action-button dashboard-btn"
            onClick={() => navigate('/dashboard')}
          >
            Dashboard
          </button>
        </div>
      </header>
    </div>
  );
}

export default App;