import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import TourCard from './TourCard'

const tour = {
    _id: '3402397a-01a6-4bad-87a8-cdc36e4e6c0c',
    title: 'El mejor recorrido en Bici hasta Incachaca',
  }

describe('./components/TourPackages/TourCard.js', () => {
  describe('.render()', () => {
    it('should render the TourCard component', () => {
      const component = shallow(<TourCard tour={tour} />)
      expect(toJson(component)).toMatchSnapshot()
    })

    it('find the rate class into TourCard component', () => {
      const component = shallow(<TourCard tour={tour} />)
      const wrapper = component.find('.rate')
      expect(wrapper.length).toBe(1)
    })
  })
})
