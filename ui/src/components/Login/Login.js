import React from 'react'
import { Link } from 'react-router-dom'
import {
  Header,
  Button,
  Dimmer,
  Image,
  Container,
  Segment,
  Icon,
} from 'semantic-ui-react'

import traveler from '../../static/logo-traveler.svg'
import './Login.less'

export default function Login({ login }) {
  return (
    <Container text className='login'>
      <Segment basic>
        <Link to='/'>
          <Icon size='large' className='arrow left' color='brown' />
        </Link>
      </Segment>

      <Dimmer active inverted>
        <Segment basic padded>
          <Header as='h1' color='brown'>
            Welcome to
          </Header>
        </Segment>

        <Image src={traveler} size='medium' />
        <Segment basic padded='very'>
          <Header as='h2'>your experience start here</Header>
        </Segment>
        <Button color='pink' onClick={login} data-testid='login' circular>
          <h1>Login</h1>
        </Button>
      </Dimmer>
    </Container>
  )
}
