import React from 'react'
import { shallow} from 'enzyme'
import toJson from 'enzyme-to-json'
import { render } from '@testing-library/react'

import ShareTour from './ShareTour'

describe('./components/ShareTour/ShareTour.js', () => {
  describe('.render()', () => {
    it('should render ShareTour component', () => {
      const wrapper = shallow(<ShareTour />)
      expect(toJson(wrapper)).toMatchSnapshot()
    })

    it('renders text ShareTour', () => {
      const wrapper = shallow(<ShareTour />)
      const copied = wrapper.contains('copied').valueOf(true)
      if (copied) {
        const { getByText } = render(<ShareTour />)
        const loadingText = getByText(/copied!/i)
      }
    })
  })
})