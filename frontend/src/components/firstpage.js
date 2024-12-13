function First() {
    return (
        <div class="relative w-full h-screen overflow-hidden">
            <img src="/images/image 2.png" class="absolute inset-0 w-full h-full object-cover blur scale-105"></img>
            <div class="absolute inset-0 bg-gradient-to-b from-white via-transparent to-white"></div>
            <div class="relative z-10 grid grid-cols-1 lg:grid-cols-2 h-full  justify-center items-center">
                <div class="text-center font-bold h-full flex justify-center items-center">
                    <div class="grid justify-center items-center h-[80%] lg:h-[50%] bg-black rounded-3xl p-10 opacity-75">
                        <h1 class="text-5xl text-white">Услуги</h1>
                        <button class="h-[100px] w-[300px] shadow-lg bg-white rounded-xl m-10 text-black text-3xl">Запись</button>
                    </div>

                </div>
                <div class="text-center font-bold h-full flex justify-center items-center">
                    <div class="grid justify-center items-center h-[80%] lg:h-[50%] bg-black rounded-3xl p-10 opacity-75">
                        <h1 class="text-5xl text-white">Обучение</h1>
                        <button class="h-[100px] w-[300px] shadow-lg bg-white rounded-xl m-10 text-black text-3xl">Запись</button>
                    </div>

                </div>
            </div>
        </div>
    );
  }
  
  export default First;