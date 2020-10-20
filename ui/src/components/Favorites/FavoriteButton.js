import React, { useState, useRef, useEffect  } from "react";
import { useFetch } from "use-http";
import { useParams } from "react-router-dom";
import { Button, Header } from "semantic-ui-react";

import { UserServices } from "../../services";

export default function FavoriteButton() {
  const UserService = new UserServices();
  const key = process.env.REACT_APP_LOGIN;
  const userData = JSON.parse(sessionStorage.getItem(key));
  const userId = userData.profile.sub;
  const token = userData.id_token;
  const { url, options } = UserService.favorites(userId, token);
  const { tourId } = useParams();
  const [favorite, setFavorite] = useState(false);
  const { post, response } = useFetch(url, options);
  const timeout = useRef()

  async function addFavorite() {
    if (!favorite) {
      await post({ tourId: tourId });
      if (response.ok) setFavorite(true);
      timeout.current = setTimeout(() => setFavorite(false), 1000)
    }
  }
  useEffect(() => {
    if (timeout.current) {
      clearTimeout(timeout.current)
    }
  }, [])

  return (
    <div>
      <Button icon="heart outline" size="big" onClick={addFavorite} />
      {favorite ? <Header as='h3' ref={timeout} color='pink'>Add to favorites </Header> : null}
    </div>
  );
}
