import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

export const Polls = () => {
  const [polls, setPolls] = useState([]);
  useEffect(() => {
    axios
      .get("http://localhost:5000/polls")
      .then(({ data }) => setPolls(data))
      .catch((error) => console.error(error.message));
  }, []);
  return (
    <div>
      <h3>Current available polls</h3>
      <ul>
        {polls.map((poll) => (
          <li key={poll.id}>
            <PollLink poll={poll} />
          </li>
        ))}
      </ul>
    </div>
  );
};
const PollLink = (props) => {
  return <Link to={"/polls/" + props.poll.id}>{props.poll.title}</Link>;
};