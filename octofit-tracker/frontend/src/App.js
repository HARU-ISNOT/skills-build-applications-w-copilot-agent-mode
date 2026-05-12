import React from 'react';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

export default function App() {
  return (
    <div className="container">
      <h1>OctoFit Tracker</h1>
      <Users />
      <Teams />
      <Activities />
      <Leaderboard />
      <Workouts />
    </div>
  );
}
