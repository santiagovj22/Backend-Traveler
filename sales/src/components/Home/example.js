// import React from 'react';
// import { CarouselProvider, Slider, Slide, ButtonBack, ButtonNext } from 'pure-react-carousel';
// import 'pure-react-carousel/dist/react-carousel.es.css';
 
// export default class extends React.Component {
//   render() {
//     return (
//       <CarouselProvider
//         naturalSlideWidth={100}
//         naturalSlideHeight={125}
//         totalSlides={3}
//       >
//             <Slider>
//           <Slide index={0}>I am the first Slide.</Slide>
//           <Slide index={1}>I am the second Slide.</Slide>
//           <Slide index={2}>I am the third Slide.</Slide>
//         </Slider>
//       </CarouselProvider>
//     );
//   }
// }
// import React, { useState, useEffect } from "react";
// import"./Home.css"
// import { Card, Icon, Image } from 'semantic-ui-react'
// // import { Carousel } from 'react-responsive-carousel';
// import Swiper from 'react-id-swiper';
// import 'swiper/css/swiper.css';
// //import "react-responsive-carousel/lib/styles/carousel.min.css";
// import axios from 'axios'
// import { CarouselProvider, Slider, Slide, ButtonBack, ButtonNext } from 'pure-react-carousel';
// import 'pure-react-carousel/dist/react-carousel.es.css';


// const Example = () => {

//   const [tours,setTours] = useState([])
//   async function fetchData(){
    
//     const res = await axios.get('http://localhost:8000/api/v1/tours')
//     setTours(res.data)
//   }
//   useEffect(() => {
//     fetchData()
//   },[])
//   const params = {
//     pagination: {
//       el: '.swiper-pagination',
//       type: 'bullets',
//       clickable: true
//     },
//     navigation: {
//       nextEl: '.swiper-button-next',
//       prevEl: '.swiper-button-prev'
//     }
//   }
//   return(
//   // <div id="carrousel">
//     <Swiper {...params}>
//         {tours.map((tour) => (
//                 <div key={tour.tour_id}>
//                   <Card id="tour-pack" style={{padding: 20, height:150}}>
//                       <Image src={tour.image_tour} wrapped ui={false} id="imagen"/>
//                       <Card.Content>
//                           <Card.Header>{tour.tour_title}</Card.Header>
//                       <Card.Description>
//                           {tour.short_description}
//                       </Card.Description>
//                       </Card.Content>
//                       <Card.Content extra>
//                         <a>
//                           <Icon name='map marker' />
//                           {tour.location}
//                         </a>
//                       </Card.Content>
//                     </Card>
//                 </div>
//         ))}
//         </Swiper>
//         // </div>
//   )
//   }
// export default Example;