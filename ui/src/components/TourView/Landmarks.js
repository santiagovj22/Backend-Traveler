import React from 'react'
import { Icon, Container, Card, Header, Segment } from 'semantic-ui-react'
import LandmarkComment from '../Comments/LandmarkComments'

import './Landmark.less'

export default function Landmarks({ landmarks }) {
  return (
    <>
      {landmarks.map((landmark) => (
        <div className='landmark' key={landmark.idMarker}>
          <Container>
            <Card>
              <Card.Content>
                <div className='title'>
                  {landmark.category === 'marker' ? (
                    <h2 className='number'>{landmark.number}</h2>
                  ) : (
                    ''
                  )}
                  <Icon size='big' color='blue' name={landmark.category} />
                  <div className='subtitle'>
                    <Header as='h2' color='blue'>
                      {landmark.name}
                    </Header>
                    <Header as='h4' color='brown'>
                      <i>Km {landmark.distance}</i>
                    </Header>
                  </div>
                </div>
                <Card.Description>{landmark.description}</Card.Description>
              </Card.Content>
            </Card>
          </Container>
          <Segment basic className='see comments'>
            <LandmarkComment landmark={landmark}/>
          </Segment>
          <hr />
        </div>
      ))}
    </>
  )
}
