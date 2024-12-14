import Educ_card from "./Educ_card";

function Third_page() {
  return (
    <div className="App relative p-6 flex-grow h-[150vh] grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 grid-rows-4">
      <Educ_card />
    </div>
  );
}

export default Third_page;
