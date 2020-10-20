import React from 'react'
import { Link } from 'react-router-dom'
import Swiper from 'react-id-swiper'
import { Grid, Card, Icon, Image, Rating, Header } from 'semantic-ui-react'

export default function CarouselCard({ tours, updateSwiper, params }) {
  return (
    <Swiper getSwiper={updateSwiper} {...params} shouldSwiperUpdate>
      {tours.map((tour) => (
        <Card key={tour._id} id={tour._id}>
          <Link to={`/tours/${tour._id}`}>
            <Image src={tour.image} />
            <Card.Content className='detail tours'>
              <Header as='h2'>{tour.title}</Header>
              <Header as='h4' color='grey'>
                {tour.brief}
              </Header>

              <Grid columns={2}>
                <Grid.Column floated='left' width={5}>
                  <Icon name='map marker alternate' />
                  <span className='rate'>{tour.location}</span>
                </Grid.Column>
                <Grid.Column floated='right' width={8}>
                  <Grid.Column textAlign='right'>
                    <Rating
                      icon='favorite'
                      defaultRating={tour.rating}
                      maxRating={5}
                    />
                    <span className='rate'>{tour.rating}</span>
                    <span className='counter'>({tour.ratingCount})</span>
                  </Grid.Column>
                </Grid.Column>
              </Grid>
            </Card.Content>
          </Link>
        </Card>
      ))}
    </Swiper>
  )
}
