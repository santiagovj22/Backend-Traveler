import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import FavoriteView from './FavoriteView'

const tours = [
  {
    _id: '5ec573d6f235707135952a95',
    title: 'Camino a la piedra de Guatapé',
  },
  {
    _id: '5ec573d6f235707135952a96',
    title: 'Historia de las playas de Bahia a pie',
  },
  {
    _id: '5ec574f6f235707135952a97',
    title: 'Cuba en bus, conociendo la Revolución Cubana',
  },
  {
    _id: '5ec574f6f235707135952a98',
    title: 'Ruta del tintico, lo mejor del café de Colombia',
  }
]

describe('./components/Favorites/FavoriteView.js', () => {
  describe('.render()', () => {
    it('should render FavoriteView component', () => {
      const wrapper = shallow(
        <FavoriteView tours={tours} />
      )
      expect(toJson(wrapper)).toMatchSnapshot()
    })
    it('renders text FavoriteView', () => {
      const wrapper = shallow(
        <FavoriteView tours={tours} />
      )
      expect(wrapper.find('h2').text()).toBe('My Favorites')
    })
  })
})
