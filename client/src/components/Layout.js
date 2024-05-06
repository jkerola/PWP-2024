import { Link, Outlet } from "react-router-dom";
export const Layout = () => {
  return (
    <div>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/polls">Polls</Link>
          </li>
          <li>
            <Link to="/users">User Management</Link>
          </li>
        </ul>
      </nav>
      <hr />
      <Outlet />
    </div>
  );
};
