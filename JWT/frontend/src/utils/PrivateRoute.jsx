import { Navigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
import { useContext } from "react";
import AuthContext from "../context/AuthContext";

export default function PrivateRoute  ({ children }) {
    let {user} = useContext(AuthContext)
    return user ? children: <Navigate to={'/login'}></Navigate>;
};
