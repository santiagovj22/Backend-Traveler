import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import CarouselCard from './CarouselCard'

const tours = [
  {
    _id: '3402397a-01a6-4bad-87a8-cdc36e4e6c0c',
    title: 'El mejor recorrido en Bici hasta Incachaca',
  },
  {
    _id: '3402397a-01a6-4bad-87a8-cdc36e4e6458',
    title: 'Camino a la piedra de Guatapé',
  },
  {
    _id: '3402397a-01a6-4bad-87a8-cdc36e446c0c',
    title: 'Historia de las playas de Bahia a pie',
  },
]

describe('./components/Carousel/CarouselCard.js', () => {
  describe('.render()', () => {
    it('should render the CarouselCard component', () => {
      const component = shallow(<CarouselCard tours={tours} />)
      expect(toJson(component)).toMatchSnapshot()
    })

    it('find the counter class into CarouselCard component', () => {
      const component = shallow(<CarouselCard tours={tours} />)
      const wrapper = component.find('.counter')
      expect(wrapper.length).toBe(3)
    })
  })
})
