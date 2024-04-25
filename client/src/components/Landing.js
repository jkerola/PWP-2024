import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { storeToken, removeToken } from "../store";

export const Landing = (props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const token = useSelector((state) => state.auth.token);
  const dispatch = useDispatch();
  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:5000/auth/login", { username, password })
      .then(({ data }) => {
        dispatch(storeToken(data.access_token));
      })
      .catch((error) => console.error(error.message));
  };
  return (
    <div>
      <h2>Polls API Client demo</h2>
      <p>Created with React.</p>
      {token && (
        <div>
          <p>You are logged in.</p>{" "}
          <input
            type="button"
            value="Logout"
            onClick={() => dispatch(removeToken())}
          />
        </div>
      )}
      {token == null && (
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={username}
            placeholder="username"
            onChange={(e) => setUsername(e.target.value)}
          ></input>
          <input
            type="password"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          ></input>
          <input type="submit" value="Authenticate" />
        </form>
      )}
    </div>
  );
};
