import TopNav from ".//TopNav";
import styled from 'styled-components';
import { useState } from "react";
export default function AllPosts() {

    const user = "SOS";
    const userReviewData = [
        {
            bookTitle: "모 이야기",
            bookImg: "https://shopping-phinf.pstatic.net/main_3752479/37524796620.20230214162228.jpg?type=w300",
            bookPublish: "엣눈북스", 
            bookWriter: "최연주",
        },
        {
            bookTitle: "오늘 밤, 세계에서 이 눈물이 사라진다 해도",
            bookImg: "https://shopping-phinf.pstatic.net/main_3351154/33511544869.20230131163126.jpg?type=w300",
            bookPublish: "모모", 
            bookWriter: "이치조 미사키",
        },
        {
            bookTitle: "오래된 골동품 상점",
            bookImg: "https://shopping-phinf.pstatic.net/main_3641034/36410342620.20230218110227.jpg?type=w300",
            bookPublish: "B612", 
            bookWriter: "디킨스",
        },
        {
            bookTitle: "사랑의 이해",
            bookImg: "https://shopping-phinf.pstatic.net/main_3247335/32473351726.20230103163554.jpg?type=w300",
            bookPublish: "민음사", 
            bookWriter: "이혁진",
        },
        {
            bookTitle: "안젤리크",
            bookImg: "https://shopping-phinf.pstatic.net/main_3633574/36335748622.20230110165953.jpg?type=w300",
            bookPublish: "밝은세상", 
            bookWriter: "기욤 뮈소",
        },
        {
            bookTitle: "이방인",
            bookImg: "https://shopping-phinf.pstatic.net/main_3782464/37824640619.20230216071303.jpg?type=w300",
            bookPublish: "현대지성", 
            bookWriter: "알베르 카뮈",
        },
        {
            bookTitle: "화이트 러시",
            bookImg: "https://shopping-phinf.pstatic.net/main_3715861/37158617631.20230131165128.jpg?type=w300",
            bookPublish: "소미미디어", 
            bookWriter: "히가시노게이고",
        },
        {
            bookTitle: "달팽이 식당",
            bookImg: "https://shopping-phinf.pstatic.net/main_3544208/35442089619.20230103124859.jpg?type=w300",
            bookPublish: "알에이치코리아", 
            bookWriter: "오가와 이토",
        },
        {
            bookTitle: "밝은 밤",
            bookImg: "https://shopping-phinf.pstatic.net/main_3247206/32472061338.20221019141949.jpg?type=w300",
            bookPublish: "문학동네", 
            bookWriter: "최은영",
        },
    ]

    return (
        <TopContainer>
            <TopNav />
            <h1>{user}님이 작성한 글 입니다.</h1>
            <MyPageContentContainer>
                <MyPageBox>
                    {userReviewData.map((it, idx) => (
                        <BookBox key={idx}>
                            <BookImg src={it.bookImg} alt="" />
                            <BookInfomation>
                                <BookTitleH5>{it.bookTitle}</BookTitleH5>
                                <BookPubAndWriter>
                                    <BookPublishedDiv>{it.bookPublish}</BookPublishedDiv>
                                    <div>{it.bookWriter}</div>         
                                </BookPubAndWriter>
                            </BookInfomation>
                        </BookBox>
                    ))
                    }   
                </MyPageBox>
            </MyPageContentContainer>
        </TopContainer>

    );

}

const TopContainer = styled.div`
    width: 100%;
    height: 100vh;
    max-width: 1200px;
    // background-color: #e5e5e5;
`

const MyPageContentContainer = styled.div`
    display: flex;
    width: 100%;
    justify-content: center;
`

const MyPageBox = styled.div`
    display: flex;
    width: 100%;
    justify-content: flex-start;
    flex-wrap: wrap;
    // background-color: black;
`

const BookBox = styled.div`
    width: 260px;
    height: 400px;
    display: flex;
    flex-direction: column;
    align-items: center;
    // background-color: #94d2bd;
    padding: 10px;
    margin: 20px 10px;
`

const BookImg = styled.img`
    width: 250px;
    max-height: 330px;
    height: auto;
`

const BookInfomation = styled.div`
    display: flex;
    width: 100%;
    height: 100%;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
`

const BookPubAndWriter = styled.div`
    margin-top: 0;
    display: flex;
    width: 100%;
    justify-content: center;
    color: #6c757d;
`

const BookPublishedDiv = styled.div`
    margin-right: 10px;
`

const BookTitleH5 = styled.h5`
    margin-bottom: 5px;
`