import Header from "./header";
import Second_page from "./service_body";
import Footer from "./footer";

function Service() {
  return (
    <div className="App flex flex-col min-h-screen">
      <Header />
      <Second_page />
      <Footer />
    </div>
  );
}

export default Service;
