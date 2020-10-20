import React from "react";
import { configure } from "enzyme";

import Adapter from "enzyme-adapter-react-16";


configure({ adapter: new Adapter() });
global.fetch = require("jest-fetch-mock");

describe("./components/Favorites/FavoritePack.js", () => {
  describe(".fetch API", () => {
    beforeEach(() => {
      fetch.resetMocks();
    });
    it("Should call API and delete data", () => {
      fetch.mockResponseOnce(
        JSON.stringify({
          token: null,
        })
      );
      fetch("http://174.138.41.78:5000/api/v1/").then((response) => {
        expect(response.token).toEqual(token);
      });
      expect(fetch.mock.calls[0][0]).toEqual(
        "http://174.138.41.78:5000/api/v1/"
      );
    });
  });
});
