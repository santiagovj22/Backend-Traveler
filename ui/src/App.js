import React from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import Home from './pages/Home'
import TourPack from './pages/TourPack'
import Auth from './pages/Auth'
import AllTour from './pages/AllTour'
import Favorites from './pages/Favorites'
import User from './pages/User'
import PrivateRoute from './privateRoutes/PrivateRoute'
import TourView from './pages/TourView'

export default function App() {
  return (
    <Router>
      <Switch>
        <Route exact path={'/'} component={Home} />
        <Route exact path={'/tours/:tourId'} component={TourPack} />
        <Route exact path={'/auth/oidc'} component={Auth} />
        <Route exact path={'/alltours'} component={AllTour} />
        <Route exact path={'/register'} component={User} />
        <PrivateRoute exact path={'/favorites'} component={Favorites} />
        <PrivateRoute exact path={'/tours/:tourId/tourview'} component={TourView}/>
      </Switch>
    </Router>
  )
}
