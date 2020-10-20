import React from 'react'
import {
  Image,
  Icon,
  Grid,
  Header,
  Button,
  Segment,
  Container,
  Sticky,
} from 'semantic-ui-react'

import ShareTour from '../ShareTours/ShareTour'
import FavoriteButton from '../Favorites/FavoriteButton'
import isLogin from '../../utils/index'
import './HeaderPack.less'

export default function HeaderPack({ tour, history }) {
  return (
    <div className='tour pack'>
      <Sticky>
        <Grid columns={3} padded>
          <Grid.Column width={4}>
            <Button
              color='pink'
              size='big'
              icon='arrow left'
              onClick={() => history.goBack()}
            />
          </Grid.Column>
          <Grid.Column textAlign='center' width={8}>
            <Header as='h1' color='white' inverted>
              TOUR PACK
            </Header>
          </Grid.Column>
          <Grid.Column textAlign='right' width={4}>
            <Button.Group color='pink'>
              {isLogin() ? <FavoriteButton /> : null}
              <ShareTour />
            </Button.Group>
          </Grid.Column>
        </Grid>
        <Image
          src={tour.image}
          fluid
          className='tour image'
          alt={tour.location}
        />
        <Container text>
          <Segment.Group>
            <Segment>
              <Header size='large'>{tour.title}</Header>
            </Segment>
            <Segment.Group horizontal>
              <Segment textAlign='right'>
                <Icon
                  color='blue'
                  className={
                    tour.transportType && tour.transportType.toLowerCase()
                  }
                />
                <span>{tour.transportType}</span>
              </Segment>
              <Segment textAlign='center'>
                <Icon className='clock outline' />
                <span>{tour.duration}</span>
              </Segment>
              <Segment textAlign='left'>
                <Icon color='pink' className='download' />
                <span>Offline</span>
              </Segment>
            </Segment.Group>
          </Segment.Group>
        </Container>
      </Sticky>
    </div>
  )
}
