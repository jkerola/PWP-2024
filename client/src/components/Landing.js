import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { storeToken, removeToken, storeUser, removeUser } from "../store";
import { Link } from "react-router-dom";

export const Landing = (props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const token = useSelector((state) => state.auth.token);
  const user = useSelector((state) => state.auth.user);
  const dispatch = useDispatch();

  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:5000/auth/login", { username, password })
      .then(({ data }) => {
        dispatch(storeToken(data.access_token));
        getProfile(data.access_token);
      })
      .catch((error) => console.error(error.message));
  };

  const getProfile = (token) => {
    axios
      .get("http://localhost:5000/auth/profile", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then(({ data }) => dispatch(storeUser(data)))
      .catch((error) => console.error(error.message));
  };

  return (
    <div>
      <h2>Polls API Client demo</h2>
      <p>Created with React.</p>
      {token && (
        <div>
          {user && (
            <p>
              Welcome {user.username}
              <br />
              Your id is {user.id}
            </p>
          )}
          {!user && <p>Welcome, ...</p>}
          <input
            type="button"
            value="Logout"
            onClick={() => {
              dispatch(removeToken());
              dispatch(removeUser());
            }}
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
      <div>
        {!token && (
          <p>
            No account? <Link to="/register">Register here!</Link>
          </p>
        )}
      </div>
    </div>
  );
};
