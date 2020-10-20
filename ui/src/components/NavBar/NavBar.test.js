import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import NavBar from './NavBar'

describe('./components/NavBar/NavBar.js', () => {
  describe('.render()', () => {
    const component = shallow(<NavBar />)

    it('renders and matches our snapshot', () => {
      const component = shallow(<NavBar />)
      expect(toJson(component)).toMatchSnapshot()
    })

    it('find the login buttons in NavBar', () => {
      const wrapper = component.find("[data-testid='item']")
      expect(wrapper.length).toBe(3)
    })
  })
})
