function Serv_card({ name, description, price }) {
    return (
      <div className="p-4">
        <div className="h-full w-[90%] bg-black rounded-2xl grid grid-rows-4 justify-center items-center text-white text-center p-4">
          <p className="text-3xl">{name}</p>
          <p className="text-xl">{description || "Описание отсутствует"}</p>
          <p className="text-2xl text-start">Стоимость: {price}</p>
          <div className="h-full">
            <button className="bg-white rounded-xl text-black h-full w-[90%] text-center items-center font-bold text-2xl">
              Записаться
            </button>
          </div>
        </div>
      </div>
    );
  }
  
  export default Serv_card;
  