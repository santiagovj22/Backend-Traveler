import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import Resources from './Resources'

const resources = [
  {
    type: 'image',
    source:
      'https://cdn.zeplin.io/5e1f6633eaa26ca7c49cab85/assets/B1D1D834-4632-4645-9F3E-3817DDBEDB34.png',
  },
  {
    type: 'video',
    source: 'https://www.youtube.com/watch?v=E_WQOBXE7us',
  },
]

describe('./components/Resources/Resources.js', () => {
  describe('.render()', () => {
    it('should render the Resources component', () => {
      const wrapper = shallow(<Resources resources={resources} />)
      expect(toJson(wrapper)).toMatchSnapshot()
    })

    it('should have class into Experiences component', () => {
      const component = shallow(<Resources resources={resources} />)
      expect(component.find('.resource').length).toEqual(1)
    })
  })
})
