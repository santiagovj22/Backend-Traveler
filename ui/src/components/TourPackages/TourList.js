import React from 'react'
import { Grid } from 'semantic-ui-react'

import TourCard from './TourCard'

export default function TourList({ tours }) {
  return (
    <Grid.Row className='packages'>
      <Grid columns={2}>
        {tours.map((tour) => (
          <TourCard tour={tour} key={tour._id} />
        ))}
      </Grid>
    </Grid.Row>
  )
}
