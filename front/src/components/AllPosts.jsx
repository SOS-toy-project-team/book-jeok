import TopNav from ".//TopNav";
import styled from 'styled-components';
export default function AllPosts() {

    const dummyBookData = [
        {
            imgUrl: "https://shopping-phinf.pstatic.net/main_3731353/37313533623.20230210070935.jpg?type=w300"
        },
        {
            imgUrl: "https://shopping-phinf.pstatic.net/main_3247335/32473353629.20230131164443.jpg?type=w300"
        },
        {
            imgUrl: "https://shopping-phinf.pstatic.net/main_3742122/37421221623.20230209070918.jpg?type=w300"
        },
        {
            imgUrl: "https://shopping-phinf.pstatic.net/main_3368499/33684998621.20230210071012.jpg?type=w300"
        },
        {
            imgUrl: "https://shopping-phinf.pstatic.net/main_3393982/33939827618.20230103164648.jpg?type=w300"
        },
        {
            imgUrl: "https://shopping-phinf.pstatic.net/main_3247607/32476078068.20230207165225.jpg?type=w300"
        },
        {
            imgUrl: "https://shopping-phinf.pstatic.net/main_3517264/35172649625.20230207163733.jpg?type=w300"
        },
        {
            imgUrl: "https://shopping-phinf.pstatic.net/main_3245316/32453160133.20230207165745.jpg?type=w300"
        },
        {
            imgUrl: "https://shopping-phinf.pstatic.net/main_3244499/32444990070.20230103163248.jpg?type=w300"
        },
    ]

    return (
        <TopContainer>
            <TopNav />
            <HomeMainContent>
                {
                    dummyBookData.map((it, idx) => (
                        <BookContent key={idx}>
                            <Img src={it.imgUrl} alt="" />
                        </BookContent>       
                    ))
                }
                
               
            </HomeMainContent>
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