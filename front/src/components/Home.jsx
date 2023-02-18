import React from 'react';
import TopNav from ".//TopNav";
import styled from 'styled-components';


export default function Home() {
    return (
        <TopContainer>
            <TopNav />
            <h1>HOME</h1>
        </TopContainer>

    ); 
}

const TopContainer = styled.div`
    width: 100%;
    height: 100vh;
    max-width: 1200px;
    background-color: #e5e5e5;
`

const HomeMainContent = styled.div`
    display: flex;
    justify-content: flex-start;
    flex-wrap: wrap;

`

const BookContent = styled.div`
    display:flex;
    justify-content: center;
    margin:10px 0px;
    width:400px;
`

const Img = styled.img`
    width: 150px;
    height: auto;
`