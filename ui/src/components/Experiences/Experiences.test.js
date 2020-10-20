import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import Experiences from './Experiences'

describe('./components/Experiences/Experiences.js', () => {
  describe('.render()', () => {
    const id = '5ec573d6f235707135952a94'

    it('should render the Experiences component', () => {
      const wrapper = shallow(<Experiences tourId={id} />)
      expect(toJson(wrapper)).toMatchSnapshot()
    })

    it('should have class experiences into Experiences component', () => {
      const component = shallow(<Experiences tourId={id} />)
      expect(component.find('.experiences').length).toEqual(1)
    })

    it('should not class into Experiences component', () => {
      const component = shallow(<Experiences tourId={id} />)
      expect(component.hasClass('/comment/')).toBe(false)
    })
  })
})
