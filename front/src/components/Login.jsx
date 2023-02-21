import TopNav from ".//TopNav";
import styled from 'styled-components';
import "../styles/Form.css";
import { useReducer, useContext } from "react";
import { AppContext } from "../App";
import { useNavigate } from 'react-router-dom';

const initialLoginInfo = {
    loginId: "",
    loginPassword: "",
}

const loginReducer = (state, action) => {
    switch(action.type) {
        case "USER_ID": {
            return {
                ...state,
                loginId: action.id,
            }
        }

        case "USER_PASSWORD": {
            return {
                ...state,
                loginPassword: action.password,
            }
        }

        default: return state;
    }

}

export default function Login() {
    const [loginInfo, loginDispatch] = useReducer(loginReducer, initialLoginInfo);
    const login = useContext(AppContext);
    const navigate = useNavigate();
    
    const loginIdHandler = (e) => {
        const id = e.target.value;
        loginDispatch({
            type: "USER_ID",
            id,
        })
        console.log(id + "아이디가 입력되었습니다."); 
    }

    const loginPasswordHandler = (e) => {
        const password = e.target.value;
        loginDispatch({
            type: "USER_PASSWORD",
            password,
        })
        console.log(password + "비밀번호가 입력되었습니다.");
    }

    const loginFormSubmitHnadler = (e) => {
        e.preventDefault();
        console.log("입력된 유저 정보" + "\n아이디는: " + loginInfo.loginId + "\n비밀번호는: " + loginInfo.loginPassword);
        login.onLogin();
        navigate("/");
        // axios 백엔드와 통신.
    }

    return (
        <TopContainer>
            <TopNav />
            <div className="formContainer">
                <h1>로그인</h1>
                <form action="" onSubmit={loginFormSubmitHnadler}>
                    <label htmlFor="">아이디</label>
                    <input type="text" onChange={loginIdHandler}/>

                    <label htmlFor="">비밀번호</label>
                    <input type="password" onChange={loginPasswordHandler}/>

                    <button>로그인</button>
                </form>
            </div>
        </TopContainer>

    );

}

const TopContainer = styled.div`
    width: 100%;
    height: 100vh;
    max-width: 1200px;
    background-color: #e5e5e5;
`
