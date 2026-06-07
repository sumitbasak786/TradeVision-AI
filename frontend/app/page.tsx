'use client';

import { useEffect, useState } from 'react';

export default function Home() {
  const [prediction, setPrediction] = useState<any>(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/prediction/reliance')
      .then((res) => res.json())
      .then((data) => setPrediction(data));
  }, []);

  return (
    <main style={{ padding: '20px' }}>
      <h1>TradeVision AI</h1>
      <p>AI-Powered Intraday Stock Prediction Platform</p>

      <div
        style={{
          border: '1px solid #ccc',
          padding: '20px',
          borderRadius: '10px',
          marginTop: '20px',
        }}
      >
        <h2>Live Prediction</h2>

        {prediction ? (
          <>
            <p><strong>Stock:</strong> {prediction.symbol}</p>
            <p><strong>Signal:</strong> {prediction.signal}</p>
            <p><strong>Confidence:</strong> {prediction.confidence}%</p>
            <p><strong>Horizon:</strong> {prediction.prediction_horizon}</p>
          </>
        ) : (
          <p>Loading prediction...</p>
        )}
      </div>
    </main>
  );
}