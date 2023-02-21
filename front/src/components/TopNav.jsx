import React, { useContext, useState } from 'react';
import "../styles/TopNav.css";
import {Link} from "react-router-dom";
import styled from 'styled-components';
import { AppContext } from "../App";

export default function TopNav() {

    // const [loginStatus, setLoginStatus] = useState(true);

    const login = useContext(AppContext);

    // console.log(login);

    return (
        <div className="navContainer">
            <div className="navItem">
                <StyledLink to="/"><div>HOME</div></StyledLink>
                <StyledLink to="/all"><div>다른 유저 글 보러가기</div></StyledLink>
            </div>

            <div className="navItem">
                {login.loginStatus ? <> 
                    <StyledLink to="/mypage"><div>마이페이지</div></StyledLink>
                    <LogoutDiv onClick={() => login.onLogout()}>로그아웃</LogoutDiv>
                </> : 
                <> 
                    <StyledLink to="/register"><div>회원가입</div></StyledLink>
                    <StyledLink to="/login"><div>로그인</div></StyledLink>
                </>}
                
            </div>
        </div>
    );
}

const StyledLink = styled(Link)`
    text-decoration: none;
    color: #eaf4f4;
    font-weight: bold;

    &:hover {
        color: #e9edc9;
    }
`

const LogoutDiv = styled.div`
    font-weight: bold;
    color: #fdffb6;
    cursor: pointer;
    &:hover {
        color: #ffca3a;
    }
`