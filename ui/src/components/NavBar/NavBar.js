import React from 'react'
import { Link } from 'react-router-dom'
import { Menu, Header, Icon, Segment, Image } from 'semantic-ui-react'

import isLogin from '../../utils/index'
import Avatar from '../../static/avatar-traveler.png'
import './NavBar.less'

export default function NavBar({ searchFocus }) {
  return (
    <Menu widths={3} fixed='bottom' className='main navbar'>
      <Menu.Item data-testid='item'>
        <Segment basic>
          <Icon name='search' size='large' onClick={searchFocus} />
          <Header as='h5'>EXPLORE</Header>
        </Segment>
      </Menu.Item>

      <Menu.Item data-testid='item'>
        <Link to='/favorites'>
        <Segment basic>
          <Icon name='heart outline' size='large' />
          <Header as='h5'>SAVED</Header>
        </Segment>
        </Link>
      </Menu.Item>

      <Menu.Item className='login' data-testid='item'>
        <Link to='/register'>
          <Segment basic>
            {  isLogin() ?  <Image src ={Avatar}  circular size='mini'/> : <Icon className='user' name='user' size='large' />}
            <Header className='profile'as='h5'>PROFILE</Header>
          </Segment>
        </Link>
      </Menu.Item>
    </Menu>
  )
}
