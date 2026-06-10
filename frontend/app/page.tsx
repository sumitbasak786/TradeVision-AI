"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [prediction, setPrediction] = useState<any>(null);
  const [marketData, setMarketData] = useState<any>(null);
  const [scannerData, setScannerData] = useState<any[]>([]);

  useEffect(() => {
    async function loadData() {
      try {
        // Prediction API
        const predictionResponse = await fetch(
          "http://127.0.0.1:8000/prediction/reliance"
        );
        const predictionJson = await predictionResponse.json();
        setPrediction(predictionJson);

        // Market Data API
        const marketResponse = await fetch(
          "http://127.0.0.1:8000/market-data/reliance"
        );
        const marketJson = await marketResponse.json();
        setMarketData(marketJson);

        // Scanner API
        const scannerResponse = await fetch(
          "http://127.0.0.1:8000/scanner"
        );
        const scannerJson = await scannerResponse.json();
        setScannerData(scannerJson);
      } catch (error) {
        console.error("Error loading data:", error);
      }
    }

    loadData();
  }, []);

  return (
    <main
      style={{
        padding: "20px",
        background: "#f5f7fa",
        minHeight: "100vh",
      }}
    >
      <h1>TradeVision AI</h1>
      <p>AI-Powered Intraday Stock Prediction Platform</p>

      {/* Top Stats */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr 1fr",
          gap: "15px",
          marginTop: "20px",
        }}
      >
        <div
          style={{
            background: "#fff",
            padding: "15px",
            borderRadius: "10px",
          }}
        >
          <h3>BUY Signals</h3>
          <p style={{ color: "green", fontSize: "20px" }}>14</p>
        </div>

        <div
          style={{
            background: "#fff",
            padding: "15px",
            borderRadius: "10px",
          }}
        >
          <h3>SELL Signals</h3>
          <p style={{ color: "red", fontSize: "20px" }}>8</p>
        </div>

        <div
          style={{
            background: "#fff",
            padding: "15px",
            borderRadius: "10px",
          }}
        >
          <h3>HOLD Signals</h3>
          <p style={{ color: "orange", fontSize: "20px" }}>23</p>
        </div>
      </div>

      {/* Live Prediction */}
      <div
        style={{
          background: "#fff",
          padding: "20px",
          borderRadius: "10px",
          marginTop: "20px",
        }}
      >
        <h3>Live Prediction</h3>

        {prediction ? (
          <>
            <p>
              <strong>Stock:</strong> {prediction.symbol}
            </p>

            <p>
              <strong>Signal:</strong>{" "}
              <span
                style={{
                  color:
                    prediction.signal === "BUY"
                      ? "green"
                      : prediction.signal === "SELL"
                      ? "red"
                      : "orange",
                  fontWeight: "bold",
                }}
              >
                {prediction.signal}
              </span>
            </p>

            <p>
              <strong>Confidence:</strong> {prediction.confidence}%
            </p>

            <div
              style={{
                width: "100%",
                background: "#ddd",
                borderRadius: "5px",
                overflow: "hidden",
                height: "12px",
              }}
            >
              <div
                style={{
                  width: `${prediction.confidence}%`,
                  height: "100%",
                  background: "#2563eb",
                }}
              />
            </div>

            <p style={{ marginTop: "10px" }}>
              <strong>Horizon:</strong>{" "}
              {prediction.prediction_horizon}
            </p>
          </>
        ) : (
          <p>Loading prediction...</p>
        )}
      </div>

      {/* Market Data */}
      <div
        style={{
          background: "#fff",
          padding: "20px",
          borderRadius: "10px",
          marginTop: "20px",
        }}
      >
        <h3>Market Data</h3>

        {marketData ? (
          <>
            <p>
              <strong>Price:</strong> ₹{marketData.price}
            </p>

            <p>
              <strong>Volume:</strong> {marketData.volume}
            </p>

            <p>
              <strong>Daily Change:</strong>{" "}
              <span
                style={{
                  color:
                    marketData.change_percent >= 0
                      ? "green"
                      : "red",
                }}
              >
                {marketData.change_percent}%
              </span>
            </p>
          </>
        ) : (
          <p>Loading market data...</p>
        )}
      </div>

      {/* Multi Stock Scanner */}
      <div
        style={{
          background: "#fff",
          padding: "20px",
          borderRadius: "10px",
          marginTop: "20px",
        }}
      >
        <h3>Multi-Stock Scanner</h3>

        <table
          style={{
            width: "100%",
            marginTop: "10px",
          }}
        >
          <thead>
            <tr>
              <th align="left">Stock</th>
              <th align="left">Signal</th>
              <th align="left">Confidence</th>
            </tr>
          </thead>

          <tbody>
            {scannerData.map((stock) => (
              <tr key={stock.symbol}>
                <td>{stock.symbol}</td>

                <td>
                  <span
                    style={{
                      color:
                        stock.signal === "BUY"
                          ? "green"
                          : stock.signal === "SELL"
                          ? "red"
                          : "orange",
                      fontWeight: "bold",
                    }}
                  >
                    {stock.signal}
                  </span>
                </td>

                <td>{stock.confidence}%</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Prediction History */}
      <div
        style={{
          background: "#fff",
          padding: "20px",
          borderRadius: "10px",
          marginTop: "20px",
        }}
      >
        <h3>Prediction History</h3>

        <table
          style={{
            width: "100%",
            marginTop: "10px",
          }}
        >
          <thead>
            <tr>
              <th align="left">Stock</th>
              <th align="left">Signal</th>
              <th align="left">Confidence</th>
            </tr>
          </thead>

          <tbody>
            <tr>
              <td>RELIANCE</td>
              <td>HOLD</td>
              <td>62.34%</td>
            </tr>

            <tr>
              <td>TCS</td>
              <td>BUY</td>
              <td>81.12%</td>
            </tr>

            <tr>
              <td>INFY</td>
              <td>SELL</td>
              <td>72.56%</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  );
}