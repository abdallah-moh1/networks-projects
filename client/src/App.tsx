import { Routes, Route, Navigate } from "react-router-dom";
import { useEffect, useState } from "react";

function HealthCheck() {
  const [status, setStatus] = useState<"loading" | "ok" | "error">("loading");

  useEffect(() => {
    fetch("/api/health")
      .then((r) => r.ok && setStatus("ok"))
      .catch(() => setStatus("error"));
  }, []);

  return <div>API: {status}</div>;
}

function Login() {
  return <div>Login Page (TODO)</div>;
}

function Chats() {
  return <div>Chats Page (TODO)</div>;
}

function ChatThread() {
  return <div>Chat Thread (TODO)</div>;
}

function Metrics() {
  return <div>Metrics Dashboard (TODO)</div>;
}

export default function App() {
  return (
    <>
      <HealthCheck />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/chats" element={<Chats />} />
        <Route path="/chats/:username" element={<ChatThread />} />
        <Route path="/metrics" element={<Metrics />} />
        <Route path="/" element={<Navigate to="/chats" replace />} />
        <Route path="*" element={<Navigate to="/chats" replace />} />
      </Routes>
    </>
  );
}
