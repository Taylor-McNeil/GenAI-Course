import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App"; // Import App component
import "./index.css"; // Import global CSS


ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>

      <App /> {/* App is the main component now */}

  </React.StrictMode>
);
