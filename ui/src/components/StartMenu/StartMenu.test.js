import React from 'react'
import { shallow, mount } from 'enzyme'
import { MemoryRouter, Link } from 'react-router-dom'
import toJson from 'enzyme-to-json'

import StartMenu from './StartMenu'

const tour = {
  _id: '4912397a-023-4bad-87a8-cdf36e4e6c0c',
  title:
    'El Metro de Medellín es un sistema de transporte masivo que sirve directamente no sólo a Medellin',
  location: 'Cochabamba',
  rating: 3.7,
}

describe('./components/StartMenu/StartMenu.js', () => {
  describe('.render()', () => {
    it('should render the StartMenu component', () => {
      const component = shallow(<StartMenu tour={tour} />)
      expect(toJson(component)).toMatchSnapshot()
    })

    it('should find START text StartMenu component', () => {
      const component = shallow(<StartMenu tour={tour} />)
      const wrapper = component.find('h2')
      expect(wrapper.text()).toBe('START')
    })

    it('should include link to tourview', () => {
      const component = mount(
        <MemoryRouter>
          <StartMenu tour={tour} />
        </MemoryRouter>
      )
      expect(component.find(Link).props().to).toBe(`/tours/${tour._id}/tourview`)
    })
  })
})
