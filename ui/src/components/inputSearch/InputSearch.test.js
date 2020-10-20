import React from 'react'
import { shallow, mount } from 'enzyme'
import toJson from 'enzyme-to-json'

import InputSearch from './InputSearch'

describe('./components/Search/InputSearch.js', () => {
  describe('.render()', () => {
    it('should render InputSearch component', () => {
      const component = shallow(<InputSearch />)
      expect(toJson(component)).toMatchSnapshot()
    })

    it('render InputSearch component', () => {
      const component = mount(<InputSearch />)
      expect(component.find('.prompt').at(0).props().placeholder).toEqual(
        'Looking for a new adventure?'
      )
    })
  })
})
