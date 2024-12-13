import First from "./firstpage";
import Second from "./2page";
import PopupCard from "./pop-up";
import Third from "./3page";



function Body() {
    return (
      <main class="flex-grow">
        <PopupCard/>
        <First/>
        <Second/>
        <Third/>
      </main>

    );
  }
  
export default Body;


  