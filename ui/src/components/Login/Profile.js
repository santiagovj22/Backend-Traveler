import React from 'react'
import { Link } from 'react-router-dom'
import { Button, Segment, Dimmer, Comment, Header } from 'semantic-ui-react'
import Avatar from '../../static/avatar-traveler.png'
import './Profile.less'
export default function Profile({ logout, user }) {
  return (
    <Dimmer inverted active className='profile'>
      <Comment.Group size='massive'>
        <Comment>
          <Comment.Avatar src={Avatar} alt={user.profile.name} />
          <Comment.Author>
            <Header as='h1' color='blue'>
              Hey, {user.profile.given_name}
            </Header>
          </Comment.Author>
        </Comment>
      </Comment.Group>
      <Segment basic>
        <Header as='h1' color='brown'>
          Where would you like to go today?
        </Header>
        <Link to='/'>
          <Button color='blue' to='/' circular>
            <h1>Tell me</h1>
          </Button>
        </Link>
      </Segment>
      <Button color='pink' onClick={logout} circular>
        <h2>Logout</h2>
      </Button>
    </Dimmer>
  )
}
