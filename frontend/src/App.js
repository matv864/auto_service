import MainPage from "./components/mainPage";

import { BrowserRouter, Routes, Route } from "react-router";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<MainPage />} />
        <Route path="education" element={<MainPage />} />
        <Route path="service" element={<MainPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
