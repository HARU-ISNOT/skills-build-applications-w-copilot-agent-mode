import React, { useEffect, useState } from 'react';

// Use the GitHub Codespace URL when running in a Codespace, otherwise localhost.
const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
const API_URL = codespaceName
  ? `https://${codespaceName}-8000.app.github.dev/api/activities/`
  : 'http://localhost:8000/api/activities/';

export default function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => setActivities(data.results || data))
      .catch((err) => console.error('Failed to load activities', err));
  }, []);

  return (
    <div>
      <h2>Activities</h2>
      <ul>
        {activities.map((a) => (
          <li key={a.id}>
            {a.activity_type} — {a.duration} min
          </li>
        ))}
      </ul>
    </div>
  );
}
