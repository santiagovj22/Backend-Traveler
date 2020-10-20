import React from "react";
import { render } from "@testing-library/react";
import App from "./App";
//import { Item } from "semantic-ui-react";


test("renders learn react link", () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/routes/i);
  expect(linkElement).toBeInTheDocument();
});
test("santiago", () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/routes/i);
  expect(linkElement).toBeInTheDocument();
});
describe("App.js", () => {
  describe("render()", () => {
    it('should render the right content', () => {
      const { getByText } = render(<App />);
      const linkElement = getByText(/routes/i);
      expect(linkElement).toBeInTheDocument();
    })
  })
})
