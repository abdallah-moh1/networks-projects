import { useEffect, useState } from "react";
import { useStore } from "../store";
import "./styles/playground.css";

async function fetchApiHealth() {
  try {
    const res = await fetch("/api/health");
    const { status } = await res.json();
    return res.ok && status === "ok";
  } catch {
    return false;
  }
}

export function Playground() {
  const { count, increment, decrement } = useStore();
  const [apiHealthy, setApiHealthy] = useState<boolean | null>(null);

  useEffect(() => {
    fetchApiHealth().then(setApiHealthy);
  }, []);

  return (
    <main className="playground">
      <p
        className={`health-status ${apiHealthy === null ? "checking" : apiHealthy ? "healthy" : "unhealthy"}`}
      >
        {apiHealthy === null ? "Checking…" : apiHealthy ? "Healthy" : "Unhealthy"}
      </p>
      <div className="counter">
        <button className="btn btn-icon" onClick={decrement} aria-label="Decrease count">
          −
        </button>
        <span className="counter-value">{count}</span>
        <button className="btn btn-icon" onClick={increment} aria-label="Increase count">
          +
        </button>
      </div>
    </main>
  );
}
