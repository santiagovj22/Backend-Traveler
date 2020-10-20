import React, { useEffect } from 'react'
import { useParams } from 'react-router-dom'
import useFetch from 'use-http'

import { TourServices } from '../services'
import Loading from '../components/Loading/Loading'
import Error from '../components/Errors/Error'
import Map from '../components/TourView/Map'
import Landmarks from '../components/TourView/Landmarks'

export default function TourView() {
  const service = new TourServices()
  const { tourId } = useParams()
  const { url } = service.getTourView(tourId)
  const {
    get, data, loading, error,
  } = useFetch(url)
  const view = data || {}

  useEffect(() => {
    get()
  }, [])

  return (
    <>
      {view.landmarks ? (
        <>
          <Map id={view.tourId} />
          <Landmarks landmarks={view.landmarks} />
        </>
      ) : (
        <div>
          {loading && <Loading />}
          {error && <Error />}
        </div>
      )}
    </>
  )
}
