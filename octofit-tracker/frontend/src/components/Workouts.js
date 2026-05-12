import React, { useEffect, useState } from 'react';

const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
const API_URL = codespaceName
  ? `https://${codespaceName}-8000.app.github.dev/api/workouts/`
  : 'http://localhost:8000/api/workouts/';

export default function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => setWorkouts(data.results || data))
      .catch((err) => console.error('Failed to load workouts', err));
  }, []);

  return (
    <div>
      <h2>Workouts</h2>
      <ul>
        {workouts.map((w) => (
          <li key={w.id}>
            <strong>{w.name}</strong>: {w.description}
          </li>
        ))}
      </ul>
    </div>
  );
}
