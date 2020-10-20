import React from "react";
import { Link } from "react-router-dom";

const Index = () => (
  <div>
    <header>
      <h1>Routes</h1>
    </header>
    <div>
      <Link to="/about"> About</Link>
      <Link to="/me"> Me</Link>
      <Link to="/home">Home</Link>
    </div>
  </div>
);
export default Index;
