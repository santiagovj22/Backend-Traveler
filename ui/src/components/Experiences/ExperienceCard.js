import React from 'react'
import { Comment, Icon, Rating, Image } from 'semantic-ui-react'
import moment from 'moment'

import './ExperienceCard.less'
import Resources from '../Resources/Resources'

export default function ExperienceCard({ experience }) {
  moment.locale('en', {
    relativeTime: {
      future: 'in %s',
      past: '%s ago',
      s: 's',
      m: '1 min',
      mm: '%d min',
      h: '1 h',
      hh: '%d h',
      d: '1 d',
      dd: '%d d',
      M: '1 m',
      MM: '%d m',
      y: '1 y',
      yy: '%d y',
    },
  })
  const {
    _id,
    avatar,
    name,
    creationDate,
    rating,
    content,
    resources,
  } = experience
  return (
    <Comment.Group className='recomendations'>
      <Comment id={_id}>
        <Image
          src={avatar}
          floated='left'
          circular
          rounded
          size='mini'
          avatar
          bordered
        />
        <Comment.Content>
          <Comment.Author as='a'>{name}</Comment.Author>
          <Comment.Metadata>
            <Icon className='clock outline' />
            <div>{moment(creationDate).fromNow()}</div>
          </Comment.Metadata>
          <div>
            <Rating icon='favorite' defaultRating={rating} maxRating={rating} />
          </div>
        </Comment.Content>
        <Comment.Text>{content}</Comment.Text>
        {resources ? <Resources resources={resources} /> : null}
      </Comment>
    </Comment.Group>
  )
}
