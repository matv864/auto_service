function Serv_card({ name, description, price }) {
    return (
        <div className="flex justify-center p-4">
            <div className="h-full w-full max-w-md bg-black rounded-2xl grid grid-rows-4 justify-center items-center text-white text-center p-4 sm:p-6">
                <p className="text-[#E86931] font-bold text-md sm:text-xl lg:text-xl">{name}</p>
                <p className="text-sm sm:text-base md:text-xl">
                    {description || "Описание отсутствует"}
                </p>
                <p className="text-lg sm:text-xl md:text-2xl text-start">
                    Стоимость: {price || "Цена отсутствует"}
                </p>
                <div className="h-full flex justify-center items-center">
                    <button className="bg-white rounded-xl text-black h-10 w-[80%] sm:h-12 sm:w-[70%] md:h-14 md:w-[60%] text-center font-bold text-base sm:text-lg md:text-xl">
                        Записаться
                    </button>
                </div>
            </div>
        </div>
    );
}

export default Serv_card;