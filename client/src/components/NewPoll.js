import axios from "axios";
import { useState } from "react";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";

export const NewPoll = () => {
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);
  const [title, setTitle] = useState(null);
  const token = useSelector((state) => state.auth.token);
  const handleSubmit = (event) => {
    event.preventDefault();
    createPoll();
  };

  const createPoll = () => {
    setError(null);
    setMessage(null);
    const data = {
      title,
    };
    axios
      .post("http://localhost:5000/polls", data, {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then(() => setMessage("Poll created"))
      .catch((error) => {
        console.error(error);
        setError(error.response.data.message);
      });
  };
  return (
    <div>
      {error && <h3 style={{ backgroundColor: "red" }}>{error}</h3>}
      {message && <h3 style={{ backgroundColor: "green" }}>{message}</h3>}
      {token && (
        <form onSubmit={handleSubmit}>
          <h2>Create a new poll</h2>
          <input
            placeholder="title"
            type="text"
            onChange={(e) => setTitle(e.target.value)}
          />
          <br />
          <input type="submit" value="Create" />
        </form>
      )}
      {token == null && (
        <p>
          <Link to="/">Login to create polls</Link>
        </p>
      )}
    </div>
  );
};
