import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'
import { render } from '@testing-library/react'

import Error from './Error'

describe('./components/Error/Error.js', () => {
  describe('.render()', () => {
    it('renders text Error', () => {
      const { getByText } = render(<Error />)
      const loadingText = getByText(/fetching/i)
    }) 

    it('should render Error component', () => {
      const component = shallow(<Error />)
      expect(toJson(component)).toMatchSnapshot()
    })
  })
})
