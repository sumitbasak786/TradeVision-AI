export default function Home() {
  return (
    <main className="min-h-screen bg-slate-100 p-6">
      <div className="max-w-7xl mx-auto">

        <h1 className="text-5xl font-bold">
          TradeVision AI
        </h1>

        <p className="mt-2 text-gray-600">
          AI-Powered Intraday Stock Prediction Platform
        </p>

        <input
          type="text"
          placeholder="Search NSE/BSE Stock..."
          className="w-full mt-6 p-4 rounded-lg border bg-white"
        />

        <div className="grid md:grid-cols-2 gap-4 mt-6">

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold">
              NIFTY 50
            </h2>

            <p className="text-2xl font-bold mt-2">
              +0.85%
            </p>
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold">
              SENSEX
            </h2>

            <p className="text-2xl font-bold mt-2">
              +0.92%
            </p>
          </div>

        </div>

        <div className="bg-white p-6 rounded-lg shadow mt-6">
          <h2 className="text-2xl font-bold">
            Top Buy Signals
          </h2>

          <ul className="mt-4 space-y-2">
            <li>RELIANCE — BUY — 87%</li>
            <li>TCS — BUY — 84%</li>
            <li>INFY — BUY — 82%</li>
          </ul>
        </div>

        <div className="bg-white p-6 rounded-lg shadow mt-6">
          <h2 className="text-2xl font-bold">
            Top Sell Signals
          </h2>

          <ul className="mt-4 space-y-2">
            <li>HDFCBANK — SELL — 78%</li>
            <li>ITC — SELL — 75%</li>
            <li>SBIN — SELL — 72%</li>
          </ul>
        </div>

      </div>
    </main>
  );
}