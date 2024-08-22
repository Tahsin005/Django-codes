import './App.css'
import { Outlet } from 'react-router-dom';
import Header from './components/Header';
import { AuthProvider } from './context/AuthContext.jsx';

function App() {

  return (
    <div>
      <AuthProvider>
        <Header></Header>
        <Outlet></Outlet>
      </AuthProvider>
    </div>
  )
}

export default App
