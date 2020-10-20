import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'
import ExperienceCard from './ExperienceCard'
import { Image } from 'semantic-ui-react'

const experience = {
  avatar:
    'https://lh5.googleusercontent.com/-nfK-6KaZMRg/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucmGlEjmzOXQl1tS5svUBgOqLfcXRw/photo.jpg',
  content:
    'Vocês passam no Cristo de la Concórdia? Tem disponibilidade para o dia 18/08? E vocês pegam passageiros na rodoviária?',
  creationDate: '2020-06-14T11:40:22.227000+00:00',
  rating: 4,
  resources: [
    { type: 'video', source: 'https://www.youtube.com/watch?v=E_WQOBXE7us' },
  ],
  name: 'Albeiro Crespo',
  _id: '5eecd780c9df78c86a6ct541x',
}

describe('./components/Experiences/ExperienceCard.js', () => {
  describe('.render()', () => {
    let component

    beforeEach(() => {
      component = shallow(
        <ExperienceCard experience={experience} key={experience._id} />
      )
    })


    it('should render the ExperienceCard component', () => {
      expect(toJson(component)).toMatchSnapshot()
    })

    it('should find class into ExperienceCard component', () => {
      const wrapper = component.find('.clock')
      expect(wrapper.length).toBe(1)
    })

    it('should find avatar into ExperienceCard component', () => {
      const { avatar } = experience
      const img = <Image src={avatar} />
      expect(component.containsMatchingElement(img)).toBe(true)
    })

    it('should validate resource is not empty', () => {
      const { resources } = experience
      expect(resources.length > 0).toEqual(true)
    })

    it('should validate resource is empty', () => {
      const experienceResource = {
        _id: '5eecd780c9df78c86a6ct541x',
        avatar:
          'https://lh5.googleusercontent.com/-nfK-6KaZMRg/AAAAAAAAAAI/AAAAAAAAAAA/AMZuucmGlEjmzOXQl1tS5svUBgOqLfcXRw/photo.jpg',
        creationDate: '2020-06-14T11:40:22.227000+00:00',
        resources: []
      }
      const {resources} = experienceResource
      expect(resources.length===0).toBe(true)
    })
  })
})
