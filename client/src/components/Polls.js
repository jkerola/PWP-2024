import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

export const Polls = () => {
  const [polls, setPolls] = useState([]);
  const [privatePolls, setPrivatePolls] = useState([]);
  const token = useSelector((state) => state.auth.token);

  useEffect(() => {
    axios
      .get("http://localhost:5000/polls", {
        headers: token
          ? {
              Authorization: `Bearer ${token}`,
            }
          : null,
      })
      .then(({ data }) => {
        setPrivatePolls(data.filter((poll) => poll.private));
        setPolls(data.filter((poll) => !poll.private));
      })
      .catch((error) => console.error(error.message));
  }, [token]);
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

      {token && <h3>My private polls</h3>}
      <ul>
        {privatePolls.map((poll) => (
          <li>
            <PollLink poll={poll} />
          </li>
        ))}
      </ul>
      {token && <Link to="/polls/new">Create a new poll</Link>}
    </div>
  );
};
const PollLink = (props) => {
  return <Link to={"/polls/" + props.poll.id}>{props.poll.title}</Link>;
};
