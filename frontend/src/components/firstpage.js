function First() {
    return (
        <div className="relative w-full h-screen overflow-hidden">
            <img
                src="/images/image 2.png"
                className="absolute inset-0 w-full h-full object-cover blur scale-105"
                alt="Background"
            />
            <div className="absolute inset-0 bg-gradient-to-b from-white via-transparent to-white"></div>
            <div className="relative z-10 grid grid-cols-1 lg:grid-cols-2 h-full justify-start items-start sm:justify-center sm:items-center">
                <div className="text-center font-bold h-[60%] sm:h-full flex justify-center items-center p-4">
                    <div className="grid justify-center items-center w-full max-w-lg h-[80%] lg:h-[50%] bg-black rounded-3xl p-8 sm:p-10 opacity-75">
                        <h1 className="text-3xl sm:text-4xl md:text-5xl text-white">Услуги</h1>
                        <button className="h-[60px] sm:h-[80px] md:h-[100px] w-[200px] sm:w-[250px] md:w-[300px] shadow-lg bg-white rounded-xl mt-6 sm:mt-8 md:mt-10 text-black text-xl sm:text-2xl md:text-3xl">
                            Запись
                        </button>
                    </div>
                </div>
                <div className="text-center font-bold h-[60%]  sm:h-full flex justify-center items-center p-4">
                    <div className="grid justify-center items-center w-full max-w-lg h-[80%] lg:h-[50%] bg-black rounded-3xl p-8 sm:p-10 opacity-75">
                        <h1 className="text-3xl sm:text-4xl md:text-5xl text-white">Обучение</h1>
                        <button className="h-[60px] sm:h-[80px] md:h-[100px] w-[200px] sm:w-[250px] md:w-[300px] shadow-lg bg-white rounded-xl mt-6 sm:mt-8 md:mt-10 text-black text-xl sm:text-2xl md:text-3xl">
                            Запись
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default First;