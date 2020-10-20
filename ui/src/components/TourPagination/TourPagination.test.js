import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import TourPagination from './TourPagination'

const tours = [
  {
    _id: '5ec573d6f235707135952a94',
    title: 'El mejor recorrido en Bici hasta Incachaca',
  },
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
  },
  {
    _id: '5ec574f6f235707135952a99',
    title: 'Tour de Boliches en la Ciudad Maravilla',
  },
]

describe('./components/TourPagination/TourPagination.js', () => {
  describe('.render()', () => {
    it('should render TourPagination component', () => {
      const wrapper = shallow(
        <TourPagination tours={tours} returnPath={'/alltours'} />
      )
      expect(toJson(wrapper)).toMatchSnapshot()
    })

    it('renders text TourPagination', () => {
      const wrapper = shallow(
        <TourPagination tours={tours} returnPath={'/alltours'} />
      )
      expect(wrapper.find('h2').text()).toBe('See All Tours')
    })
  })
})
