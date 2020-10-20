import React, { useState } from 'react'
import 'swiper/css/swiper.css'
import { Header, Icon, Container, Grid, Button } from 'semantic-ui-react'

import CarouselCard from './CarouselCard'
import './Carousel.less'

const params = {
  spaceBetween: 20,
  centeredSlides: true,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    dynamicBullets: true,
  },
}

export default function Carousel({ tours }) {
  const [swiper, updateSwiper] = useState(null)

  return (
    <>
      <Container text className='carousel'>
        <Grid columns={2} padded='vertically'>
          <Grid.Column textAlign='left' className='trending'>
            <Header color='pink' as='h2'>
              Trending
              <Icon name='chart line' className='icon map' />
            </Header>
          </Grid.Column>
          <Grid.Column textAlign='right'>
            <Button.Group basic size='mini' compact>
              <Button
                onClick={() => swiper && swiper.slidePrev()}
                icon='left chevron'
              />
              <Button
                onClick={() => swiper && swiper.slideNext()}
                icon='right chevron'
              />
            </Button.Group>
          </Grid.Column>
        </Grid>
        <CarouselCard
          tours={tours}
          params={params}
          updateSwiper={updateSwiper}
        />
      </Container>
    </>
  )
}
