import React, { useEffect, useRef } from 'react'
import useFetch from 'use-http'

import { TourServices } from '../services'
import InputSearch from '../components/inputSearch/InputSearch'
import Carousel from '../components/Carousel/Carousel'
import TourPackages from '../components/TourPackages/TourPackages'
import Loading from '../components/Loading/Loading'
import Error from '../components/Errors/Error'
import NavBar from '../components/NavBar/NavBar'

export default function Home() {
  const services = new TourServices()
  const searchInput = useRef(null)

  const searchFocus = () => {
    searchInput.current.focus()
  }

  const { url } = services.getAll()
  const {
    get, data, loading, error,
  } = useFetch(url)

  useEffect(() => {
    get()
  }, [])

  const tours = data ? data.data : []

  return (
    <>
      {loading && <Loading />}
      {error && <Error />}
      <NavBar searchFocus={searchFocus} />
      <InputSearch searchInput={searchInput} />
      <Carousel tours={tours} />
      <TourPackages />
    </>
  )
}
