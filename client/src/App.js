import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Landing } from "./components/Landing";
import { Poll } from "./components/Poll";
import { Polls } from "./components/Polls";
import { Layout } from "./components/Layout";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Landing />} />
          <Route path="polls" element={<Polls />} />
          <Route path="/polls/:pollId" element={<Poll />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
