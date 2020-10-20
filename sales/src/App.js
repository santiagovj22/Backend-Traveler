import React from "react";
import "./App.css";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Aboutme from "./components/About";
import Home from "./components/Home/Home";
import Me from "./components/Me";
import Index from "./components/Index";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Index}/>
        <Route  path="/about" component={Aboutme}/>
        <Route  path="/home" component={Home}/>
        <Route  path="/me" component={Me}/>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
