import React, { useState, useEffect } from 'react';
import Swiper from 'react-id-swiper';
import axios from 'axios';
// import 'swiper/css/swiper.css';
import './Home.css'
import { Card, Icon, Image, Rating,Container, Grid } from 'semantic-ui-react'

const Example = () => {
  const [tours, setTours] = useState([]);

  useEffect(() => {
    axios
      .get('http://64.225.28.124:8000/api/v1/tours')
      .then((res) => {
        setTours(res.data);
      })
      .catch((err) => console.log(err));
  }, [tours]);
  const params = {
    centeredSlides: true,
    spaceBetween: 30,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      dynamicBullets: true
    }
  }
  return (
    <div>
      <Grid.Column align='center'>
        <div className="trending title">
          <p>Trending</p>
          <Icon name="chart line" className="trending icon"/>
        </div>
      </Grid.Column>
    <Swiper {...params}>
      {tours.map((tour) => (
        <Container className="tour packages">
          <Container className="second">
          <Card className="card tours">
            <Image src={tour.image_tour} className="image tour"/>
            <Card.Header content={tour.tour_title} id="title"/>
              <Card.Description content={tour.short_description} id="description"/>
              <Card.Content extra className="rating-location">
                <a><Icon name='map marker alternate'/>{tour.location}</a>
                <span className="rating-points">
                  <Rating icon="star" maxRating={5} defaultRating={tour.rating}/>
                  <p>{tour.rating}</p>
                  (<p>{tour.rating_count}</p>)
                </span>
            </Card.Content>
          </Card>
          </Container>
        </Container>
      ))}
    </Swiper>
    </div>
  );
};
export default Example;
