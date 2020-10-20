import React from 'react'
import { shallow, mount } from 'enzyme'
import { BrowserRouter as Router, Link } from 'react-router-dom'

import Map from './Map'

const id = '5f015eecf58b185ccb534d8e'

describe('./components/TourView/Map.js', () => {
  describe('.click()', () => {
    const component = shallow(<Map />)

    it('should find EXIT test into Map component', () => {
      const wrapper = component.find('h2')
      expect(wrapper.text()).toBe('EXIT')
    })

    it('shoul return to tour pack page', () => {
      const component = mount(
        <Router>
          <Map id={id} />
        </Router>
      )
      expect(component.find(Link).props().to).toBe(`/tours/${id}`)
    })
  })
})
