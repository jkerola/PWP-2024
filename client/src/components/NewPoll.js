import axios from "axios";
import { useState } from "react";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";

export const NewPoll = () => {
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);
  const [title, setTitle] = useState(null);
  const [description, setDescription] = useState(null);
  const [expires, setExpires] = useState(null);
  const token = useSelector((state) => state.auth.token);

  const [inputs, setInputs] = useState([{ itemDescription: "" }]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await createPoll();
    const id = response.id;
    const itemResponse = await addPollItems(id);
  };

  const handleDeleteInput = (index) => {
    const newInputs = [...inputs];
    newInputs.splice(index, 1);
    setInputs(newInputs);
  };

  const handleNewItemInput = () => {
    const newInputs = [...inputs];
    newInputs.push({ itemDescription: "" });
    setInputs(newInputs);
  };

  const handleInputChange = (index, value) => {
    const newInputs = [...inputs];
    newInputs[index].itemDescription = value;
    setInputs(newInputs);
  };

  const createPoll = async () => {
    return new Promise((resolve, reject) => {
      setError(null);
      setMessage(null);
      const data = {
        title,
        description,
        expires,
      };

      axios
        .post("http://localhost:5000/polls", data, {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((response) => {
          resolve({ id: response.data.id, message: "Poll created" });
        })
        .catch((error) => {
          console.error(error);
          setError(error.response.data.message);
          reject(error);
        });
    });
  };

  const addPollItems = async (pollId) => {
    return new Promise((resolve, reject) => {
      setError(null);
      setMessage(null);

      const itemData = {
        pollId,
        description,
      };
      axios
        .post("http://localhost:5000/pollitems", itemData, {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then(() => {
          setMessage("Poll created");
          resolve();
        })
        .catch((error) => {
          console.error(error);
          setError(error.response.data.message);
          reject(error);
        });
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
          <input
            placeholder="description"
            type="text"
            onChange={(e) => setDescription(e.target.value)}
          />
          <br />
          <input
            placeholder="expires"
            type="text"
            onChange={(e) => setExpires(e.target.value)}
          />
          <br />
          <h3>Add poll items</h3>
          <div>
            {inputs.map((input, index) => (
              <div className="input_container" key={index}>
                <input
                  placeholder="new item"
                  type="text"
                  value={input.itemDescription}
                  onChange={(e) => {
                    handleInputChange(index, e.target.value);
                  }}
                />
                <button onClick={() => handleDeleteInput(index)}>Delete</button>
              </div>
            ))}
            <button type="button" onClick={handleNewItemInput}>
              New
            </button>
          </div>
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
