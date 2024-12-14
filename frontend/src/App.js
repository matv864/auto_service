import MainPage from "./components/mainPage";
import Service from "./components/Service";
import Education from "./components/Educ";
import Serv_form from "./components/Secv_form";
import Edu_form from "./components/edu_form";

import { BrowserRouter, Routes, Route } from "react-router";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<MainPage />} />
        <Route path="education" element={<Education/>} />
        <Route path="service" element={<Service/>} />
        <Route path="serv_form" element={<Serv_form/>} />
        <Route path="edu_form" element={<Edu_form/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
