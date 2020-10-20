import React, { useState } from 'react'
import { AuthService } from '../services/authService'

import Profile from '../components/Login/Profile'
import Login from '../components/Login/Login'

const key = process.env.REACT_APP_LOGIN

export default function User() {
  const authService = AuthService.getInstance()
  const userData = JSON.parse(sessionStorage.getItem(key))
  const [isLoggedIn] = useState(true)

  const login = () => {
    authService.login()
  }

  const logout = () => {
    authService.logout()
  }

  return (
    <>
      {isLoggedIn && userData ? (
        <Profile logout={logout} user={userData} />
      ) : (
        <Login login={login} />
      )}
    </>
  )
}
