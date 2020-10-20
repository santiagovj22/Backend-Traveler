import React from 'react'
import { Link } from 'react-router-dom'
import { Icon, Button, Segment, Sticky } from 'semantic-ui-react'

import './Map.less'

export default function Map({ id }) {
  return (
    <div className='map'>
      <Sticky>
        <Segment basic className='mapview'>
          <img
            src='https://www.google.com/maps/about/images/mymaps/mymaps-desktop-16x9.png'
            alt='map'
          />
        </Segment>
        <Segment.Group horizontal>
          <Segment textAlign='left'>
            <Icon size='huge' className='play circle' />
            <div>
              <h5>PLAY</h5>
              <p>Listen landmark</p>
            </div>
          </Segment>
          <Segment textAlign='right'>
            <Link to={`/tours/${id}`}>
              <Button color='pink' className='play' circular>
                <h2>EXIT</h2>
              </Button>
            </Link>
          </Segment>
        </Segment.Group>
      </Sticky>
    </div>
  )
}
