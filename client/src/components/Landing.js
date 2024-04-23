import { useState } from "react";
import axios from "axios";

export const Landing = (props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post("http://localhost:5000/auth/login", { username, password })
      .then(({ data }) => {
        // TODO: state management, store this token and use it as 'login' switch
        console.log(data);
      })
      .catch((error) => console.error(error.message));
  };
  return (
    <div>
      <h2>Polls API Client demo</h2>
      <p>Created with React.</p>
      {props.token == null && (
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
