import React from 'react'
import { Header, Rating, Icon, Button, Menu } from 'semantic-ui-react'
import { Link } from 'react-router-dom'

import './StartMenu.less'

export default function StartMenu({ tour }) {
  const { _id, location, rating, ratingCount } = tour
  return (
    <Menu widths={2} fixed='bottom' secondary className='start'>
      <Menu.Item>
        <Header>
          <Icon name='map marker alternate' color='grey' />
          <Header.Content>{location}</Header.Content>
          <Header.Subheader>
            {rating && (
              <Rating icon='favorite' defaultRating={rating} maxRating={5} />
            )}
            <span className='rate'>{rating}</span>
            <span className='counter'>({ratingCount})</span>
          </Header.Subheader>
        </Header>
      </Menu.Item>
      <Menu.Item>
        <Link to={`/tours/${_id}/tourview`}>
          <Button color='pink' circular>
            <h2>START</h2>
          </Button>
        </Link>
      </Menu.Item>
    </Menu>
  )
}
