import { NavLink, Navigate, Route, Routes } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="app-shell container py-4 py-lg-5">
      <div className="card border-0 shadow-sm mb-4 app-hero">
        <div className="card-body p-4 p-lg-5">
          <h1 className="display-6 fw-bold mb-2">OctoFit Tracker</h1>
          <p className="lead mb-0 text-secondary">Fitness analytics dashboard powered by Django REST API endpoints.</p>
        </div>
      </div>

      <nav className="navbar navbar-expand-lg bg-body-tertiary rounded-4 border shadow-sm mb-4 px-2">
        <div className="container-fluid">
          <span className="navbar-brand fw-semibold">Navigation</span>
          <ul className="navbar-nav me-auto mb-2 mb-lg-0 gap-lg-1">
            <li className="nav-item">
              <NavLink className="nav-link px-3 rounded-pill" to="/activities">
                Activities
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link px-3 rounded-pill" to="/leaderboard">
                Leaderboard
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link px-3 rounded-pill" to="/teams">
                Teams
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link px-3 rounded-pill" to="/users">
                Users
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link px-3 rounded-pill" to="/workouts">
                Workouts
              </NavLink>
            </li>
          </ul>
        </div>
      </nav>

      <div className="card border-0 shadow-sm">
        <div className="card-body p-3 p-lg-4">
          <Routes>
            <Route path="/" element={<Navigate to="/activities" replace />} />
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
          </Routes>
        </div>
      </div>
    </div>
  );
}

export default App;
