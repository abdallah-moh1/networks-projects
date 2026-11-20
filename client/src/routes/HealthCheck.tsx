import { useEffect, useState } from "react";

export function HealthCheck() {
  async function healthCheck(): Promise<{ status: string }> {
    const response = await fetch("api/health");
    if (!response.ok) {
      throw new Error("Health check failed");
    }
    return response.json();
  }

  const [status, setStatus] = useState<"loading" | "ok" | "error">("loading");

  useEffect(() => {
    healthCheck()
      .then(() => setStatus("ok"))
      .catch(() => setStatus("error"));
  }, []);

  return <div className="health-check">API: {status}</div>;
}
