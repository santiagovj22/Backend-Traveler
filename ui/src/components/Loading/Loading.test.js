import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'
import { render } from '@testing-library/react'

import Loading from './Loading'

describe('./components/Loading/Loading.js', () => {
  describe('.render()', () => {
    it('renders text Loading', () => {
      const { getByText } = render(<Loading />)
      const loadingText = getByText(/loading/i)
    })    

    it('should render Loading component', () => {
      const component = shallow(<Loading />)
      expect(toJson(component)).toMatchSnapshot()
    })
  })
})
