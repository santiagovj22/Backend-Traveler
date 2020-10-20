// import React, { useState, useEffect } from "react";
// import Slider from "react-slick";
// import "slick-carousel/slick/slick.css";
// import "slick-carousel/slick/slick-theme.css";
// import './Home.css'
// import {  Card, Icon, Image, Rating,Container, Grid} from 'semantic-ui-react'

// import axios from 'axios'
// const Slick = () => {
//     const [tours,setTours] = useState([])
//     async function fetchData(){
      
//       const res = await axios.get('http://64.225.28.124:8000/api/v1/tours')
//       setTours(res.data)
//     }
//     useEffect(() => {
//       fetchData()
//     },[])

//     const settings = {
//       dots: true,
//       infinite: true,
//       speed: 500,
//       slidesToShow: 1,
//       slidesToScroll: 1,responsive: [
//         {
//           breakpoint: 1024,
//           settings: {
//             slidesToShow: 3,
//             slidesToScroll: 3,
//             infinite: true,
//             dots: true
//           }
//         },
//         {
//           breakpoint: 600,
//           settings: {
//             slidesToShow: 2,
//             slidesToScroll: 2,
//             initialSlide: 2
//           }
//         },
//         {
//           breakpoint: 480,
//           settings: {
//             slidesToShow: 1,
//             slidesToScroll: 1
//           }
//         }
//       ]
//     };

//     return (
//       <div>
//       <Grid.Column align='center'>
//         <div className="trending title">
//           <p>Trending</p>
//           <Icon name="chart line" className="trending icon"/>
//         </div>
//       </Grid.Column>
//       <Slider {...settings}>
//         {tours.map((tour) => (
//         <Container className="tour packages">
//           <Card className="card tours">
//             <Image src={tour.image_tour} className="image tour"/>
//             <Card.Content 
//               header={tour.tour_title} 
//               description={tour.short_description}
//               id="short-description"/>
//               <Card.Content extra className="rating-location">
//                 <a><Icon name='map marker alternate'/>{tour.location}</a>
//                 <span className="rating-points">
//                   <Rating icon="star" maxRating={5} defaultRating={tour.rating}/>
//                   <p>{tour.rating}</p>
//                   (<p>{tour.rating_count}</p>)
//                 </span>
//             </Card.Content>
//           </Card>
//         </Container>
//       ))}
//       </Slider>
//       </div>
//     );
// }
// export default Slick;