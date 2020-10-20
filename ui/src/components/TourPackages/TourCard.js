import React from 'react'
import { Image, Rating, Icon, Card, Grid } from 'semantic-ui-react'
import { Link } from 'react-router-dom'

const TourCard = ({ tour }) => (
  <Grid.Column id={tour._id}>
    <Link to={`/tours/${tour._id}`}>
      <Image src={tour.image} size='small' centered alt={tour.location} />
      <Card.Content>
        <Card.Header className='card title'>{tour.title}</Card.Header>
        <Grid.Column>
          <Card.Meta>
            <Icon name='map marker alternate' />
            <span>{tour.location}</span>
          </Card.Meta>
          <Card.Content>
            <Rating icon='favorite' defaultRating={tour.rating} maxRating={5} />
            <span className='rate'>{tour.rating}</span>
            <span className='counter'>({tour.ratingCount})</span>
          </Card.Content>
        </Grid.Column>
      </Card.Content>
    </Link>
  </Grid.Column>
)

export default TourCard
