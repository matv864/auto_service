import Educ_card from "./Educ_card";

function Third_page() {
  return (
    <div className="App" class="relative p-6 flex-grow h-[150vh] grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 grid-rows-4">
        <Educ_card/>
        <Educ_card/>
      {/* <div className="h-[120px] flex justify-center items-center">
        <button className="h-[50px] sm:h-[80px] w-[70%] sm:w-[40%] bg-black rounded-3xl absolute bottom-[40px] sm:bottom-[40px] flex justify-center items-center shadow-lg">
          <div className="text-white font-bold text-center text-base sm:text-xl">
            Посмотреть еще...
          </div>
        </button>
      </div> */}
    </div>
  );
}

export default Third_page;