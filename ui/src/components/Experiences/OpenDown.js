import React from 'react'
import { Button } from 'semantic-ui-react'

export default function OpenDown({
  getAllExperiences,
  experiences,
  totalExperiences,
}) {
  const openDown =
    experiences.length !== totalExperiences ? (
      <Button onClick={getAllExperiences} className='btn experiences'>
        SEE ALL EXPERIENCES
      </Button>
    ) : (
      <Button disabled className='btn experiences'>
        THERE ARE NOT MORE EXPERIENCES
      </Button>
    )
  return <div className='see experiences'>{openDown}</div>
}
