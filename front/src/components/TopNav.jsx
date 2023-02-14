import React from 'react';
import "../styles/TopNav.css";
import {Link} from "react-router-dom";
import styled from 'styled-components';

export default function TopNav() {
    return (
        <div className="navContainer">
            <div className="navItem">
                <StyledLink to="/"><div>HOME</div></StyledLink>
                <StyledLink to="/all"><div>다른 유저 글 보러가기</div></StyledLink>
            </div>

            <div className="navItem">
                <StyledLink to="/register"><div>회원가입</div></StyledLink>
                <StyledLink to="/login"><div>로그인</div></StyledLink>
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