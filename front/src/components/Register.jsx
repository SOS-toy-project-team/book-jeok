import TopNav from ".//TopNav";
import styled from 'styled-components';
import "../styles/Form.css";
import { useReducer } from "react";

const initialRegisterInfo = {
    registerNickName: "",
    registerId: "",
    registerPassword: "",
}

const registerReducer = (state, action) => {
    switch(action.type) {
        case "REGI_NICK_NAME": {
            return {
                ...state,
                registerNickName: action.nickname,
            }
        }

        case "REGI_ID": {
            return {
                ...state,
                registerId: action.id,
            }
        }   

        case "REGI_PASSWORD": {
            return {
                ...state,
                registerPassword: action.password,
            }
        }

        default: return state;
    }
}

export default function Register() {

    const [registerInfo, registerDispatch] = useReducer(registerReducer, initialRegisterInfo);

    const registerNickNameHandler = (e) => {
        const nickname = e.target.value;
        registerDispatch({
            type: "REGI_NICK_NAME",
            nickname,
        })
    }
    const registerIdHandler = (e) => {
        const id = e.target.value;
        registerDispatch({
            type: "REGI_ID",
            id,
        })
    }
    const registerPasswordHandler = (e) => {
        const password = e.target.value;
        registerDispatch({
            type: "REGI_PASSWORD",
            password,
        })
    }
    const registerFormSubmitHandler = (e) => {
        e.preventDefault();
        
        console.log("회원가입 유저 정보" + "\n닉네임은: " + 
        registerInfo.registerNickName + "\n아이디는: " + 
        registerInfo.registerId + "\n비밀번호는: " + 
        registerInfo.registerPassword);

    }

    return (
        <TopContainer>
            <TopNav />
            <div className="formContainer">
                <h1>등록하기</h1>
                <form action="" onSubmit={registerFormSubmitHandler}>
                    <label htmlFor="regiNickname">닉네임</label>
                    <input type="text" name="" id="regiNickname" onChange={registerNickNameHandler}/> 

                    <label htmlFor="regiId">아이디</label>
                    <input type="text" name="" id="regiId" onChange={registerIdHandler}/> 

                    <label htmlFor="regiPassword">비밀번호</label>
                    <input type="password" name="" id="regiPassword" onChange={registerPasswordHandler}/> 
                    
                    <button>회원가입</button>
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
