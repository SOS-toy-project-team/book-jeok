import TopNav from ".//TopNav";
import styled from 'styled-components';
export default function Review() {
    return (
        <TopContainer>
            <TopNav />
            <h1>리뷰</h1>
        </TopContainer>

    );

}

const TopContainer = styled.div`
    width: 100%;
    height: 100vh;
    max-width: 1200px;
    // background-color: #e5e5e5;
`