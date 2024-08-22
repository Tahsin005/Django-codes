import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import HomePage from './pages/HomePage.jsx';
import LoginPage from './pages/LoginPage'
import PrivateRoute from './utils/PrivateRoute.jsx';
import Dashboard from './pages/Dashboard.jsx';
const router = createBrowserRouter([
  {
    path: "/",
    element: <App></App>,
    children: [
      {
        path: "/",
        element: (<PrivateRoute>
          <HomePage></HomePage>
        </PrivateRoute>),
      },
      {
        path: "/login",
        element: <LoginPage></LoginPage>,
      },
    ]
  },
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
