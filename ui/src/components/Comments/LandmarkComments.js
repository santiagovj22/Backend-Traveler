import React from "react";
import {
  Container,
  Card,
  Header,
  Icon,
  Modal,
} from "semantic-ui-react";
import "./LandmarkComments.less";

export default function LandmarksComment({ landmark }) {
  return (
    <Modal
      trigger={
        <Header as="h5" color="grey" textAlign="center">
          See Comments
        </Header>
      }
      closeIcon
    >
      <Container>
        <Modal.Header></Modal.Header>
        <div className="title">
          <h2 className="number">{landmark.number}</h2>
          <Icon size="big" color="blue" name={landmark.category} />
          <div className="subtitle">
            <Header as="h2" color="blue">
              {landmark.name}
            </Header>
            <Header as="h4" color="brown">
              <i>Km {landmark.distance}</i>
            </Header>
          </div>
        </div>
        <Card.Description>{landmark.description}</Card.Description>
      </Container>
    </Modal>
  );
}
