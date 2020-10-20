import React from "react";
import { Link } from "react-router-dom";
import { Container, Icon, Grid, Header, Message } from "semantic-ui-react";

import FavoritePack from "./FavoritePack";

export default function FavoriteView({ tours }) {
  return (
    <Container text className="favorites">
      <Grid columns={3} padded>
        <Grid.Column width={4}>
          <Link to={"/"}>
            <Icon color="pink" size="large" className="arrow left header" />
          </Link>
        </Grid.Column>
        <Grid.Column textAlign="center" width={8}>
          <Header color="pink">
            <h2>My Favorites</h2>
          </Header>
        </Grid.Column>
      </Grid>
      <Grid.Row>
        <Grid columns={2}>
          {tours.length >= 1 ? (
            tours &&
            tours.map((tour) => <FavoritePack tour={tour} key={tour._id} />)
          ) : (
            <Grid textAlign="center" padded>
              <Message color="yellow">Don't have favorite tours</Message>
            </Grid>
          )}
        </Grid>
      </Grid.Row>
    </Container>
  );
}
