import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React, { createContext, useState } from 'react';
import Login from "./components/Login";
import Home from "./components/Home";
import Register from "./components/Register";
import AllPosts from "./components/AllPosts";
import MyPage from "./components/MyPage";
import Review from "./components/Review";
import "./styles/App.css";


export const AppContext = createContext(null);

export default function App() {

  const [loginStatus, setLoginStatus] = useState(false);

  const onLogout = () => {
    setLoginStatus(false);
  }
  const onLogin = () => {
    setLoginStatus(true);
  }

  return (
    <AppContext.Provider value={{loginStatus, onLogout, onLogin}}>
      <div className="AppContainer">
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/login" element={<Login />}></Route>
            <Route path="/register" element={<Register />}></Route>
            <Route path="/all" element={<AllPosts />}></Route>
            <Route path="/mypage" element={<MyPage />}></Route>
            <Route path="/review" element={<Review />}></Route>
          </Routes>
        </BrowserRouter>
      </div>
    </AppContext.Provider>
  );
}

