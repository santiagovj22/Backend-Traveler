import React from "react";
import { Link } from "react-router-dom";
import { useFetch } from "use-http";
import { Image, Rating, Icon, Card, Grid, Button } from "semantic-ui-react";

import { UserServices } from "../../services";

export default function FavoritePack({ tour }) {
  const UserService = new UserServices();
  const key = process.env.REACT_APP_LOGIN;
  const userData = JSON.parse(sessionStorage.getItem(key));
  const userId = userData.profile.sub;
  const token = userData.id_token;
  const { url, options } = UserService.favorites(userId, token);
  const { del } = useFetch(url, options);

  async function removeFavorite(tourid) {
    await del({ tourId: tourid });
    alert("Has been delete");
    window.location.reload();
  }

  return (
    <Grid.Column id={tour._id}>
      <Link to={`/tours/${tour._id}`}>
        <Image src={tour.image} size="small" centered alt={tour.location} />
        <Card.Content>
          <Card.Header className="card title">{tour.title}</Card.Header>
          <Grid.Column>
            <Card.Meta>
              <Icon name="map marker alternate" />
              <span>{tour.location}</span>
            </Card.Meta>
            <Card.Content>
              <Rating
                icon="favorite"
                defaultRating={tour.rating}
                maxRating={5}
              />
              <span className="rate">{tour.rating}</span>
              <span className="counter">({tour.ratingCount})</span>
            </Card.Content>
          </Grid.Column>
        </Card.Content>
      </Link>
      <Button onClick={() => removeFavorite(tour._id)}>Delete</Button>
    </Grid.Column>
  );
}
