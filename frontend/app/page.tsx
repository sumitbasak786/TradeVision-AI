export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-5xl font-bold">
        TradeVision AI
      </h1>

      <p className="mt-4 text-lg">
        AI-Powered Intraday Stock Prediction Platform
      </p>

      <div className="mt-10 border rounded-lg p-6">
        <h2 className="text-2xl font-semibold">
          Market Overview
        </h2>

        <p className="mt-2">
          NSE • BSE • ETFs
        </p>
      </div>

      <div className="mt-6 border rounded-lg p-6">
        <h2 className="text-2xl font-semibold">
          Top Buy Signals
        </h2>

        <p className="mt-2">
          Coming Soon...
        </p>
      </div>

      <div className="mt-6 border rounded-lg p-6">
        <h2 className="text-2xl font-semibold">
          Top Sell Signals
        </h2>

        <p className="mt-2">
          Coming Soon...
        </p>
      </div>
    </main>
  );
}