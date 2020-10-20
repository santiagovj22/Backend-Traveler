import React, { useEffect } from 'react'
import { useHistory } from 'react-router-dom'
import { AuthService } from '../services/authService'

import Loading from '../components/Loading/Loading'
import { config } from '../config/config'

export default function Auth() {
  const history = useHistory()
  const authService = AuthService.getInstance()

  const API_URL = config

  useEffect(() => {
    async function userRegister() {
      try {
        console.log('Entro');

        await AuthService.getInstance().signinRedirectCallback()
        // const user = await authService.getUser()
        // console.log(user)
        // await fetch(`${API_URL}auth/login`, {
        //   method: 'POST',
        //   body: JSON.stringify({ token: user.id_token }),
        //   headers: {
        //     'Content-Type': 'application/json',
        //   },
        // })
        history.push('/')
      } catch (error) {
        alert('Your session has expired, please login again!')
      }
    }
    userRegister()
  }, [])
  return <Loading />
}
