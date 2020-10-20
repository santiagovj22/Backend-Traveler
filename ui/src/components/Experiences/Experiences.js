import React, { useState, useEffect } from 'react'
import { Container, Header } from 'semantic-ui-react'
import useFetch from 'use-http'

import { TourServices } from '../../services'
import ExperienceCard from './ExperienceCard'
import OpenDown from './OpenDown'
import Loading from '../Loading/Loading'
import Error from '../Errors/Error'
import './Experiences.less'

export default function Experiences({ tourId }) {
  const [experiences, setExperiences] = useState([])
  const [totalExperiences, setTotalExperiences] = useState(0)
  const [page, setPage] = useState(1)
  const services = new TourServices()
  const { url } = services.experiences(tourId, page, 2)
  
  const { get, loading, error } = useFetch(url)

  async function getAllExperiences() {
    const getExperiences = await get()
    setExperiences(experiences.concat(getExperiences.data))
    setTotalExperiences(getExperiences.totalRows)
    setPage(page + 1)
  }

  useEffect(() => {
    getAllExperiences()
  }, [])

  return (
    <Container text className='experiences tour'>
      <Header as='h2' color='blue'>
        Travelers Experiences
      </Header>
      {loading && <Loading />}
      {error && <Error />}
      {experiences.map((experience) => (
        <ExperienceCard experience={experience} key={experience._id} />
      ))}

      <OpenDown
        getAllExperiences={getAllExperiences}
        experiences={experiences}
        totalExperiences={totalExperiences}
      />
    </Container>
  )
}
