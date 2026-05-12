import React, { useEffect, useState } from 'react';

const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
const API_URL = codespaceName
  ? `https://${codespaceName}-8000.app.github.dev/api/teams/`
  : 'http://localhost:8000/api/teams/';

export default function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => setTeams(data.results || data))
      .catch((err) => console.error('Failed to load teams', err));
  }, []);

  return (
    <div>
      <h2>Teams</h2>
      <ul>
        {teams.map((t) => (
          <li key={t.id}>{t.name}</li>
        ))}
      </ul>
    </div>
  );
}
