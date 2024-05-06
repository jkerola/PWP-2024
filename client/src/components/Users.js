import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import axios from "axios";
import { removeToken, removeUser } from "../store";

export const Users = () => {
  const token = useSelector((state) => state.auth.token);
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);
  const user = useSelector((state) => state.auth.user);
  const dispatch = useDispatch();
  useEffect(() => {
    if (token) {
      axios
        .get("http://localhost:5000/users", {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then(({ data }) => setUsers(data))
        .catch((error) => {
          console.error(error.message);
          setError(error);
        });
    }
  }, [token]);

  const deleteUser = (userId) => {
    axios
      .delete("http://localhost:5000/users/" + userId, {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then(() => {
        setUsers(users.filter((user) => user.id !== userId));
        if (user.id === userId) {
          dispatch(removeToken());
          dispatch(removeUser());
          setUsers([]);
        }
      })
      .catch((error) => console.log(error));
  };
  return (
    <div>
      {!token && <p>Please login to manage users.</p>}
      {token && error && <p>You are not an admin.</p>}
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <UserDetail user={user} callback={deleteUser} />
          </li>
        ))}
      </ul>
    </div>
  );
};

const UserDetail = (props) => {
  const deleteCallback = props.callback;
  const user = props.user;
  return (
    <div>
      <b>{user.username}</b> {user.email}{" "}
      <input
        type="button"
        onClick={() => deleteCallback(user.id)}
        value="Delete"
      />
    </div>
  );
};
