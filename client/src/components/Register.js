import { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
export const Register = () => {
  const [username, setUsername] = useState(null);
  const [password, setPassword] = useState(null);
  const [cPassword, setCPassword] = useState(null);
  const [email, setEmail] = useState(null);
  const [firstName, setFirstName] = useState(null);
  const [lastName, setLastName] = useState(null);
  const [error, setError] = useState(null);
  const [message, setMessage] = useState(null);

  const validate = () => {
    clearMessages();
    if (username === null || username === "") {
      setError(`Invalid username ${username}`);
    } else if (password == null || password === "") {
      setError("Invalid password");
    } else if (password !== cPassword) {
      setError("Passwords do not match");
    } else {
      return true;
    }
    return false;
  };
  const handleSubmit = (event) => {
    event.preventDefault();
    clearMessages();

    if (validate()) {
      registerAccount();
    }
  };

  const clearMessages = () => {
    setError(null);
    setMessage(null);
  };

  const registerAccount = () => {
    const data = { username, password };
    if (email) data.email = email;
    if (firstName) data.firstName = firstName;
    if (lastName) data.lastName = lastName;
    axios
      .post("http://localhost:5000/auth/register", data)
      .then((res) => {
        console.log(res.status);
        setMessage("Account registered!");
      })
      .catch((error) => {
        console.error(error.message);
        setError(error.message);
      });
  };
  return (
    <div>
      {message && <h3 style={{ backgroundColor: "green" }}>{message}</h3>}
      {error && <h3 style={{ backgroundColor: "red" }}>{error}</h3>}
      <form onSubmit={handleSubmit}>
        <legend>Register</legend>
        <input
          type="text"
          placeholder="username"
          onChange={(e) => setUsername(e.target.value)}
        />
        <br />
        <input
          type="password"
          placeholder="password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <input
          type="password"
          placeholder="confirm password"
          onChange={(e) => setCPassword(e.target.value)}
        />
        <br />
        <input
          type="email"
          placeholder="email (optional)"
          onChange={(e) => setEmail(e.target.value)}
        />
        <br />
        <input
          type="text"
          placeholder="first name (optional)"
          onChange={(e) => setFirstName(e.target.value)}
        />
        <br />
        <input
          type="text"
          placeholder="last name (optional)"
          onChange={(e) => setLastName(e.target.value)}
        />
        <br />
        <input type="submit" value="Register" />
      </form>
      <Link to="/">Go Back</Link>
    </div>
  );
};
