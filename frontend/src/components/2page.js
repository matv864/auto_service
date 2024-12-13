import Card from "./card";

function Second() {
    return (
        <main className="relative w-full min-h-screen overflow-hidden">
            <div className="p-4 grid grid-cols-3 gap-4 items-center">
                <div className="flex justify-center">
                    <button className="w-[150px] sm:w-[200px] h-[60px] sm:h-[100px] shadow-xl rounded-3xl bg-black text-white font-bold text-2xl sm:text-4xl">
                        Проекты
                    </button>
                </div>
                <div className="flex justify-center">
                    <button className="w-[150px] sm:w-[200px] h-[60px] sm:h-[100px] shadow-xl rounded-3xl bg-black text-white font-bold text-2xl sm:text-4xl">
                        Новости
                    </button>
                </div>
                <div className="flex justify-center">
                    <button className="w-[150px] sm:w-[200px] h-[60px] sm:h-[100px] shadow-xl rounded-3xl bg-black text-white font-bold text-2xl sm:text-4xl">
                        Отзывы
                    </button>
                </div>
                
                
            </div>

            <div className="px-4 sm:px-10 grid grid-cols-1 md:grid-cols-2 gap-6">
                <Card />
                <Card />
                
            </div>

            <div className="h-[120px] flex justify-center items-center">
                <button className="h-[50px] sm:h-[80px] w-[70%] sm:w-[40%] bg-black rounded-3xl absolute bottom-[40px] sm:bottom-[20px] flex justify-center items-center shadow-lg">
                    <div className="text-white font-bold text-center text-base sm:text-xl">
                        Посмотреть еще...
                    </div>
                </button>
            </div>

            <div className="px-4 sm:px-40 font-bold text-3xl sm:text-5xl text-center absolute bottom-[-10px] sm:text-left pt-[40px] sm:pt-[60px]">
                <div>О Компании</div>
            </div>
        </main>
    );
}

export default Second;