import React from 'react'
import InfiniteScroll from 'react-infinite-scroll-component'
import { Grid, Header, Icon, Container } from 'semantic-ui-react'
import { Link } from 'react-router-dom'

import TourCard from '../TourPackages/TourCard'
import Loading from '../Loading/Loading'

export default function TourPagination({ tours, getAllTours, loading }) {
  return (
    <Container text>
      <Grid columns={3} padded>
        <Grid.Column width={4}>
          <Link to={'/'}>
            <Icon color='pink' size='large' className='arrow left header' />
          </Link>
        </Grid.Column>
        <Grid.Column textAlign='center' width={8}>
          <Header color='pink'>
            <h2>See All Tours</h2>
          </Header>
        </Grid.Column>
      </Grid>
      <Grid.Row>
        <InfiniteScroll
          dataLength={tours.length}
          next={getAllTours}
          hasMore={true}
          loader={loading && <Loading />}
          style={{ overflow: 'hidden' }}
        >
          <Grid columns={2}>
            {tours &&
              tours.map((tour) => <TourCard tour={tour} key={tour._id} />)}
          </Grid>
        </InfiniteScroll>
      </Grid.Row>
    </Container>
  )
}
