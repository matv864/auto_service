import MainPage from "./components/mainPage";
import Service from "./components/Service";
import Education from "./components/Educ";

import { BrowserRouter, Routes, Route } from "react-router";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<MainPage />} />
        <Route path="education" element={<Education/>} />
        <Route path="service" element={<Service/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
