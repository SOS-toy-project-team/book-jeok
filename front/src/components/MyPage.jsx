import TopNav from ".//TopNav";
import styled from 'styled-components';
import { useState } from "react";
import { useParams } from "react-router";
import {Link} from "react-router-dom";
export default function AllPosts() {

    const { userId } = useParams();
    const userReviewData = [
        {
            id: "1",
            bookTitle: "모 이야기",
            bookImg: "https://shopping-phinf.pstatic.net/main_3752479/37524796620.20230214162228.jpg?type=w300",
            bookPublish: "엣눈북스", 
            bookWriter: "최연주",
            rank: 3,
            genre: "판타지",
            desc: "Would you be surprised that road rage can be good for society? Or that most crashes happen on sunny, dry days? That our minds can trick us into thinking the next lane is moving faster? Or that you can gauge a nation s driving behavior by its levels of corruption? These are only a few of the remarkable dynamics that Tom Vanderbilt explores in this fascinating tour through the mysteries of the road."
        },
        {
            id: "2",
            bookTitle: "오늘 밤, 세계에서 이 눈물이 사라진다 해도",
            bookImg: "https://shopping-phinf.pstatic.net/main_3351154/33511544869.20230131163126.jpg?type=w300",
            bookPublish: "모모", 
            bookWriter: "이치조 미사키",
            rank: 2,
            genre: "미스터리",
            desc: "마음속 다양한 감정을 알고 자신의 감정을 슬기롭게 다루며 친구와 건강하게 소통하는 방법을 안내하는 「어린이를 위한 마음 처방」 시리즈가 출간되었어요. 이 시리즈는 어린이가 마주하는 다양한 감정과 관계를 상황별 예시를 들어 알려 주고, 구체적인 솔루션을 통해 감정을 적절하게 표현하고 해소하며 원만한 친구 관계를 형성할 수 있게 도와줘요."
        },
        {
            id: "3",
            bookTitle: "오래된 골동품 상점",
            bookImg: "https://shopping-phinf.pstatic.net/main_3641034/36410342620.20230218110227.jpg?type=w300",
            bookPublish: "B612", 
            bookWriter: "디킨스",
            rank: 5,
            genre: "추리",
            desc: "뛰어난 전시 기획자이자 『명화 속 신기한 수학 이야기』등 활발한 저작으로 미술 스토리텔링의 새 지평을 연 이명옥 관장은 단순히 보고 느끼고 즐기는 수동적 감상법에서 벗어나 능동적인 감상자가 되어야 한다고 강조한다. 능동적인 감상자가 되는 것은 ‘특별한 방식으로 사물을 보는 작가, 그리고 그렇게 사물을 보는 방식을 예술적으로 표현하는 작가’가 누구인지부터 찾는 것부터가 시작이다."
        },
        {
            id: "4",
            bookTitle: "사랑의 이해",
            bookImg: "https://shopping-phinf.pstatic.net/main_3247335/32473351726.20230103163554.jpg?type=w300",
            bookPublish: "민음사", 
            bookWriter: "이혁진",
            rank: 4,
            genre: "자기계발",
            desc: "오늘날 국가 경쟁력이 국가와 개인의 화두로 떠오르고 각국마다 국민의 경쟁력을 높이기 위해 힘쓰고 있다. 이때 반드시 언급되는 것이 모어(母語)능력과 외국어 능력이다. 특히 국제화 시대를 맞아 나라마다 외국어 교육에 힘을 쏟으면서, 모어를 잘해야 외국어를 잘할 수 있다는 언어학적 법칙에 따라 그 토대가 되는 모어 교육에도 엄청난 투자를 하여 자국민의 모어능력 향상에 전력을 다하고 있다."
        },
        {
            id: "5",
            bookTitle: "안젤리크",
            bookImg: "https://shopping-phinf.pstatic.net/main_3633574/36335748622.20230110165953.jpg?type=w300",
            bookPublish: "밝은세상", 
            bookWriter: "기욤 뮈소",
            rank: 1,
            genre: "고전",
            desc: "아기 고양이 모는 잠이 오지 않는 밤, 창밖으로 우연히 보게 된 웃는 빛을 따라 숲을 탐험하게 된다. 숲을 걸으며 모는 친절하고 재미있는 숲속 친구들을 만나고... 그들을 통해 길을 떠나기 전 준비하는 법, 처음 만난 이에게 인사하는 법, 마음을 나누는 법, 함께 힘을 모아 문제를 해결하는 법, 걱정을 잊고 순간을 즐기는 법 등 다양한 지혜를 얻게 된다."
        },
        {
            id: "6",
            bookTitle: "이방인",
            bookImg: "https://shopping-phinf.pstatic.net/main_3782464/37824640619.20230216071303.jpg?type=w300",
            bookPublish: "현대지성", 
            bookWriter: "알베르 카뮈",
            rank: 4,
            genre: "고전",
            desc: "영어회화를 잘하고 싶은데 뭐부터 할지 모르겠다면 구동사부터 시작하세요. 원어민과 몇 마디만 해 봐도 빠짐없이 나오는 것이 이 구동사이기 때문입니다. 하지만 아무 구동사나 하는 건 아닙니다. 미국통 플로리다 아선생이 골라낸, 미국인들이 일상 다반사로 많이 쓰는 구동사로 하세요. 정확한 뜻, 풍부한 예문, 현실적인 회화 지문으로 한 번을 해도 구동사를 제대로 학습합니다."
        },
        {
            id: "7",
            bookTitle: "화이트 러시",
            bookImg: "https://shopping-phinf.pstatic.net/main_3715861/37158617631.20230131165128.jpg?type=w300",
            bookPublish: "소미미디어", 
            bookWriter: "히가시노게이고",
            rank: 4,
            genre: "일본 문학",
            desc: "2000년부터 발표된 그의 주옥같은 글들. 독자들이 자발적으로 만든 제본서는 물론, 전자책과 앱까지 나왔던 《세이노의 가르침》이 드디어 전국 서점에서 독자들을 마주한다. 여러 판본을 모으고 저자의 확인을 거쳐 최근 생각을 추가로 수록하였다. 정식 출간본에만 추가로 수록된 글들은 목차와 본문에 별도 표시하였다."
        },
        {
            id: "8",
            bookTitle: "달팽이 식당",
            bookImg: "https://shopping-phinf.pstatic.net/main_3544208/35442089619.20230103124859.jpg?type=w300",
            bookPublish: "알에이치코리아", 
            bookWriter: "오가와 이토",
            rank: 4,
            genre: "달팽이 문학",
            desc: "2023 금융위기, 미중 패권전쟁, 마지막 때를 준비하는 가장 구체적인 12가지 방법과 이기는 자가 되는 DO IT! 『DO IT 두잇』 은 2022년 12월 1일 부터 12월 16일 까지 진행된 라이트하우스 10차 특별기도회의 메세지를 바탕으로 만들어진 책이다. 총 12편의 DO IT 메세지는 생방송 동시 시청자수 4800명, 누적 조회수 200만 회의 놀라운 참여로 전 세계의 많은 성도들을 변화시킨 메세지이다."
        },
        {
            id: "9",
            bookTitle: "밝은 밤",
            bookImg: "https://shopping-phinf.pstatic.net/main_3247206/32472061338.20221019141949.jpg?type=w300",
            bookPublish: "문학동네", 
            bookWriter: "최은영",
            rank: 4,
            genre: "소설",
            desc: "전 국민이 힘겨워하는 불황에 여느 세대보다 더 많이 흔들리는 이들이 있다. 가족을 짊어지고 커리어의 정점을 향해가고 있는 40대들이다. 마흔이 되면 괜찮아질 줄 았았는데, 삶이 좀 더 안정될 거라 믿었는데 실상은 그렇지가 않다. 대기업과 금융권에서 올해 만 40세가 된 1982년생을 희망퇴직 대상자에 포함시킨다는 소식이 들려오면서 40대의 불안은 더욱 커지고 있다."
        },
    ]

    return (
        <TopContainer>
            <TopNav />
            <h1>{userId}님이 작성한 글 입니다.</h1>
            <MyPageContentContainer>
                <MyPageBox>
                    {userReviewData.map((it, idx) => (
                        <BookBox key={idx}>
                            <Link to={`/bookreview/${it.id}`}><BookImg src={it.bookImg} alt="" /></Link>
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