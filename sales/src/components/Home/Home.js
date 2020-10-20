import React from "react";
import "./Home.css"
import traveler from '../../assets/img/traveler.png';
import { Image,Input, Grid, Container, Icon} from 'semantic-ui-react'
import CarruselContainer from './other';

const Home = () => {

  return(
    <Container>
        <Grid.Column align='center'>
          <Image src={traveler} centered id="logo"/>
          <Container className="input container">
            <Input size='large' icon="search" iconPosition='left' placeholder='Looking for a new adventure?' id="search"/>
          </Container>
        </Grid.Column>
        <CarruselContainer/>
    </Container>
  )
}
export default Home;
