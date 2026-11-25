import { RouteObject } from "react-router-dom";
import { Playground } from "./Playground";
import { Login } from "./Login";
import { Chats } from "./Chats";
import { ChatThread } from "./ChatThread";
import { Metrics } from "./Metrics";
import { SignUp } from "./SignUp";

export const routes: RouteObject[] = [
  {
    path: "/",
    element: <Playground />,
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/signup",
    element: <SignUp />,
  },
  {
    path: "chats",
    element: <Chats />,
  },
  {
    path: "chats/:username",
    element: <ChatThread />,
  },
  {
    path: "metrics",
    element: <Metrics />,
  },
];
