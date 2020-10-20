import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import Landmarks from './Landmarks'

const landmarks = [
  {
    category: 'marker',
    description:
      'El Parque Principal donde todos se juntan para charlar es un sitio muy concurrido y realmente hermosa la fuente que abarca toda la plaza, está situada en el centro de una gran represa alrededor encontrarás lugares para tomarse un café o simplemente disfrutar la vista de un bello atardecer con agradable clima, descubrir tiendas llenas de artesanías y otros negocios de abarrotes. Las construcciones a su alrededor son llamativas. Desde allí prestan el servicio de transporte de mototaxis y jeep para dirigirte a la piedra o al municipio del Peñol.',
    distance: 1.5,
    idMarker: 78214557,
    name: 'Parque Principal',
  },
  {
    category: 'marker',
    description:
      'Su construcción inicio en el año 2010. Se comenzó un proyecto el cual consistió en que cada de las personas se apropiaran más de las raíces de su pueblo, haciendo que se formaran convites en pro de la zocalizacion logrando que los Guatapenses día a día se fueran identificando más con los zócalos y los colores que engalanan esta región, mostrando en el frontis de sus hogares figuras que cuentan historia yendo desde el primer zocalo (el cordero)  hasta figuras que muestran la identidad de las familias.',
    distance: 2.5,
    idMarker: 78214558,
    name: 'Plazoleta Zocalos',
  },
  {
    category: 'info circle',
    description:
      'El museo histórico de Guatapé esta ubicado en la calle del recuerdo. en el se da a conocer la historia del municipio. La apertura del museo abre otra perspectiva cultural a Guatapé, porque se enfoca también en la recuperación de la memoria y la cultura histórica del municipio. ',
    distance: 3.2,
    idMarker: 78214559,
    name: 'Museo Historico Guatapé',
  },
]

describe('./components/TourView/Landmark.js', () => {
  describe('.render()', () => {
    it('should render the Landmark component', () => {
      const component = shallow(<Landmarks landmarks={landmarks} />)
      expect(toJson(component)).toMatchSnapshot()
    })

    it('find the title of tourview into the Landmark', () => {
      const component = shallow(<Landmarks landmarks={landmarks} />)
      const wrapper = component.find('.title')
      expect(wrapper.length).toBe(3)
    })
  })
})
