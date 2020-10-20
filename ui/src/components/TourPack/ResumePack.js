import React from 'react'
import { Container } from 'semantic-ui-react'

import './ResumePack.less'

const ResumePack = ({ tour }) => {
  return (
    <Container text>
      <h3 className='resume'>
        <p>{tour.description}</p>
      </h3>
      <hr />
    </Container>
  )
}

export default ResumePack
