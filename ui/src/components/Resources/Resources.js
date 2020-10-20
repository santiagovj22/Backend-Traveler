import React from 'react'
import { Image, Embed } from 'semantic-ui-react'

import './Resources.less'

export default function Resources({ resources }) {
  const typeResource = resources.map((resource) => {
    const { type, source } = resource
    if (type === 'image') {
      return (
        <Image
          src={source}
          size='large'
          className='img resource'
          rounded
          centered
        />
      )
    }
    if (type === 'video') {
      return <Embed url={source} />
    }
    return null
  })
  return <div>{typeResource}</div>
}
