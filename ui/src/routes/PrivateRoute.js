import React from 'react'
import { Route, Redirect } from 'react-router-dom'
import isLogin from '../utils/index'

export default function withAuth({ component: Component, ...rest }) {
  return (
    <Route
      {...rest}
      render={(props) => (
        isLogin()
          ? <Component {...props} />
          : (
            <Redirect
              to={{
                pathname: '/register',
                state: { from: props.location },
              }}
            />
          )
      )}
    />
  )
}
