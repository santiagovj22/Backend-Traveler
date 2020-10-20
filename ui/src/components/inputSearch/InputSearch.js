import React, { useState, useEffect } from 'react'
import {
  Header,
  Container,
  Image,
  Grid,
  Segment,
  Search,
  Form,
} from 'semantic-ui-react'
import { Link } from 'react-router-dom'
import useFetch from 'use-http'
import { useThrottle } from 'use-throttle'

import traveler from '../../static/logo-traveler.svg'
import { TourServices } from '../../services'
import Loading from '../Loading/Loading'
import Error from '../Errors/Error'
import './inputSearch.less'

export default function InputSearch({ searchInput }) {
  const [value, setValue] = useState('')

  const services = new TourServices()
  const throttledValue = useThrottle(value, 1000)
  const { url } = services.search(throttledValue)
  const { get, loading, error, data } = useFetch(url)

  useEffect(() => {
    if (!value) return
    get()
  }, [get])

  function searchChange(event) {
    let strSearchValue = event.target.value.replace(/[^a-zA-Z0-9_-]/gi, '')
    setValue(strSearchValue)
  }

  const searchTourRender = ({ title, location, image, brief, _id }) => (
    <Segment>
      <Link to={`/tours/${_id}`}>
        {loading && <Loading />}
        {error && <Error />}
        <Header as='h2' color='pink'>
          {title}
        </Header>
        <Image src={image} size='small' alt={location} floated='right' />
        <p>{brief}</p>
        <Header as='h5'>{location}</Header>
      </Link>
    </Segment>
  )

  return (
    <Container text>
      <Grid.Column align='center'>
        <Image src={traveler} centered size='small' className='logo' />
        <Form>
          <Form.Field className='search'>
            <Search
              fluid
              input={{ icon: 'search', iconPosition: 'left', ref: searchInput }}
              onKeyUp={(event) => searchChange(event)}
              placeholder='Looking for a new adventure?'
              results={data ? data.data : null}
              resultRenderer={searchTourRender}
            />
          </Form.Field>
        </Form>
      </Grid.Column>
    </Container>
  )
}
