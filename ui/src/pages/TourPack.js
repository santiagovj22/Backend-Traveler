import React, { useEffect } from 'react'
import { useParams, useHistory } from 'react-router-dom'
import useFetch from 'use-http'

import { TourServices } from '../services'
import HeaderPack from '../components/TourPack/HeaderPack'
import ResumePack from '../components/TourPack/ResumePack'
import Experiences from '../components/Experiences/Experiences'
import Loading from '../components/Loading/Loading'
import Error from '../components/Errors/Error'
import StartMenu from '../components/StartMenu/StartMenu'

export default function TourPack() {
  const services = new TourServices()
  const { tourId } = useParams()
  const history = useHistory()
  const { url } = services.get(tourId)
  const {
    get, data, loading, error,
  } = useFetch(url)

  useEffect(() => {
    get()
  }, [url])

  const tour = data || {}

  return (
    <div>
      {loading && <Loading />}
      {error && <Error />}
      <HeaderPack tour={tour} history={history} />
      <ResumePack tour={tour} />
      <Experiences tourId={tourId} />
      <StartMenu tour={tour} />
    </div>
  )
}
