import React, { useEffect } from 'react'
import useFetch from 'use-http'
import { Header, Icon, Container, Grid } from 'semantic-ui-react'

import TourList from './TourList'
import { TourServices } from '../../services'
import Loading from '../Loading/Loading'
import Error from '../Errors/Error'
import './TourPackages.less'
import { Link } from 'react-router-dom'

export default function TourPackages() {
  const services = new TourServices()
  const { url } = services.pagination(1, 6)
  const { get, data, loading, error } = useFetch(url)

  useEffect(() => {
    get()
  }, [])

  const tours = data ? data.data : []

  return (
    <Container text>
      {loading && <Loading />}
      {error && <Error />}
      <Grid columns={2}>
        <Grid.Column floated='left' width={10}>
          <Header as='h2' floated='left' color='pink'>
            More Tours Packs
            <Icon name='map outline' />
          </Header>
        </Grid.Column>
        <Grid.Column floated='right' width={5}>
          <Grid.Column textAlign='right'>
            <Link to={'/alltours'}>
              <Header as='h5' color='grey' floated='right'>
                SEE ALL
              </Header>
            </Link>
          </Grid.Column>
        </Grid.Column>
      </Grid>

      <TourList tours={tours} />
    </Container>
  )
}
