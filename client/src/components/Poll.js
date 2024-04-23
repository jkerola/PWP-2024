import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export const Poll = () => {
  const { pollId } = useParams();
  const [poll, setPoll] = useState(Object);
  const [items, setItems] = useState([]);

  const getPollItems = (pollId) => {
    axios
      .get("http://localhost:5000/polls/" + pollId + "/pollitems")
      .then(({ data }) => setItems(data))
      .catch((error) => console.error(error.message));
  };

  useEffect(() => {
    axios
      .get("http://localhost:5000/polls/" + pollId)
      .then(({ data }) => setPoll(data))
      .catch((error) => console.error(error.message));
    getPollItems(pollId);
  }, [pollId]);

  return (
    <div>
      <h2>{poll.title}</h2>
      <p>{poll.id}</p>
      <PollItems items={items} updateCallback={() => getPollItems(pollId)} />
    </div>
  );
};

const PollItems = (props) => {
  return (
    <ul>
      {props.items.map((item) => (
        <li key={item.id}>
          <PollItem item={item} updateCallback={props.updateCallback} />
        </li>
      ))}
    </ul>
  );
};

const PollItem = (props) => {
  const dispatchVote = () => {
    axios
      .post("http://localhost:5000/pollitems/" + props.item.id, null)
      .then(() => props.updateCallback());
  };

  return (
    <div>
      <p>
        {props.item.description} -- {props.item.votes} votes
      </p>
      <button onClick={dispatchVote}>Vote</button>
    </div>
  );
};
