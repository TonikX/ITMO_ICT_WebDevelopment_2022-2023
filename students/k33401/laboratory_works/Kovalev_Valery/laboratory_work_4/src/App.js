import logo from "./logo.svg";
import "./App.css";
import MainPage from "./pages/MainPage";
import { Route, Routes } from "react-router-dom";
import React from "react";
import SearchPage from "./pages/SearchPage";
import ProfilePage from "./pages/ProfilePage";

function App() {
    return (
        <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/search/:category?/:tone?" element={<SearchPage />} />
            <Route path="/profile" element={<ProfilePage />} />
        </Routes>
    );
}

export default App;
