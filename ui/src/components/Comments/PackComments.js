import React from 'react'
import { Container, Header } from 'semantic-ui-react'
import CommentCard from './CommentCard'

const comments = [
  {
    avatar: 'https://api.adorable.io/avatars/40/javier@adorable.io.png',
    content:
      'It was a great experience, its perfect for spend time with friends',
    creationDate: '22/04/2021',
    id: '1j75h29fm03j0ao8',
    name: 'Javier Roca',
    rating: 4,
    resources: [
      {
        name: 'guatape',
        type: 'image',
        uri:
          'https://cdn.zeplin.io/5e1f6633eaa26ca7c49cab85/assets/B1D1D834-4632-4645-9F3E-3817DDBEDB34.png',
      },
    ],
  },
  {
    avatar: 'https://api.adorable.io/avatars/40/ramiro@adorable.io.png',
    content: 'Its wonderful place, i love it',
    creationDate: '22/04/2021',
    id: '03g6d5an2m3l43i4n',
    name: 'Ramiro ergueta',
    rating: 3,
    resources: [],
  },
  {
    avatar: 'https://api.adorable.io/avatars/40/gary@adorable.io.png',
    content: 'I like so much, is very pretty',
    creationDate: '02/11/2020',
    id: '37h6km2m3px0a8',
    name: 'Gary ascuy',
    rating: 4,
    resources: [],
  },
]

const PackComments = () => {
  return (
    <Container text className='comments tour'>
      <Header as='h2' color='blue'>
        Travelers Experiences
      </Header>
      {comments.map((comment) => (
        <CommentCard comment={comment} key={comment.id} />
      ))}
    </Container>
  )
}

export default PackComments
