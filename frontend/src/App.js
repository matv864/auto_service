import MainPage from "./components/mainPage";
import Service from "./components/Service";

import { BrowserRouter, Routes, Route } from "react-router";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<MainPage />} />
        <Route path="education" element={<Service />} />
        <Route path="service" element={<Service />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
