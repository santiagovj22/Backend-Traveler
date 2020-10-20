import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import Login from './Login'

describe('./components/Login/Login.js', () => {
  describe('.render()', () => {
    const mockLogin = jest.fn()
    const component = shallow(<Login login={mockLogin} />)

    it('renders and matches our snapshot', () => {
      const component = shallow(<Login />)
      expect(toJson(component)).toMatchSnapshot()
    })

    it('find the login button', () => {
      const wrapper = component.find("[data-testid='login']")
      expect(wrapper.length).toBe(1)
    })

    it('click over the login button', () => {
      component.find('Button').simulate('click')
      expect(mockLogin).toBeCalled()
    })
  })
})
