import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import Login from "./components/Login";
import Home from "./components/Home";
import Register from "./components/Register";
import AllPosts from "./components/AllPosts";
import "./styles/App.css";

export default function App() {
  return (
    <div className="AppContainer">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/login" element={<Login />}></Route>
          <Route path="/register" element={<Register />}></Route>
          <Route path="/all" element={<AllPosts />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

