import React, { useState, useEffect } from 'react'
import useFetch from 'use-http'
import TourPagination from '../components/TourPagination/TourPagination'

import { TourServices } from '../services'
import Loading from '../components/Loading/Loading'
import Error from '../components/Errors/Error'

export default function AllTour() {
  const [tours, setTours] = useState([])
  const [page, setPage] = useState(1)
  const services = new TourServices()
  const { url } = services.pagination(page, 6)
  const { get, loading, error } = useFetch(url)

  async function getAllTours() {
    const getTours = await get()
    setTours(tours.concat(getTours.data))
    setPage(page + 1)
  }

  useEffect(() => {
    getAllTours()
  }, [])

  return (
    <div>
      {loading && <Loading />}
      {error && <Error />}
      <TourPagination
        tours={tours}
        getAllTours={getAllTours}
        loading={loading}
      />
    </div>
  )
}
