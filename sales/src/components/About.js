// import React from "react";
// import { Link } from "react-router-dom";
// import axios from "axios";
// import { Button } from "semantic-ui-react";

// class About extends React.Component {
//   constructor() {
//     super();
//     this.state = {
//       data: [],
//     };
//   }

//   async componentDidMount() {
//     const res = await axios.get("http://localhost:8000/api/v1/tours");
//     await this.setState({ ...this.state, data: res.data });
//   }

//   render() {
//     const { data } = this.state;
//     const elements = data;
//     const tours = [];
//     for (const [i, value] of elements.entries()) {
//       tours.push(
//         <div className="container-2" key={i}>
//           {value.title}
//           <h2>{value.location}</h2>
//           <h2>{value.rating_count}</h2>
//           <img src={value.image_tour} />
//         </div>,
//       );
//     }
//     return (
//       <div className="container">
//         <h2>Toures</h2>
//         {tours}

//         <Button>Hello</Button>
//         <Link to="/">Return</Link>
//       </div>


//     );
//   }
// }

// export default About;
