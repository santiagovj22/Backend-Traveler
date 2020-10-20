import React, { useEffect, useState } from 'react'
import { UserServices } from '../services'
import FavoriteView from '../components/Favorites/FavoriteView'

export default function FavoriteTours() {
  const UserService = new UserServices()
  const key = process.env.REACT_APP_LOGIN
  const userData = JSON.parse(sessionStorage.getItem(key))
  const userId = userData.profile.sub
  const token = userData.id_token
  const { url, options } = UserService.favorites(userId, token)
  const [favorites, setFavorites] = useState([])

  async function getData() {
    try {
      await fetch(url, options)
        .then((response) => response.json())
        .then((data) => {
          setFavorites(data)
        })
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    getData()
  }, [])

  return (
    <div>
      <FavoriteView tours={favorites} />
    </div>
  )
}
