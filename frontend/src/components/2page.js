import Card from "./card";


function Second() {
    return (
      <main class="relative w-full h-[150vh] overflow-hidden">
        <div class=" p-4 h-[200px] grid grid-cols-3 justify-center items-center">
            <div class="p-8 flex justify-center">
                <button class="w-[200px] h-[100px] shadow-xl rounded-3xl bg-black text-white text-bold text-4xl">Проекты</button>
            </div>
            <div class="p-8 flex justify-center">
                <button class="w-[200px] h-[100px] shadow-xl rounded-3xl bg-black text-white text-bold text-4xl">Новости</button>
            </div>
            <div class="p-8 flex justify-center">
                <button class="w-[200px] h-[100px] shadow-xl rounded-3xl bg-black text-white text-bold text-4xl">Отзывы</button>
            </div>
        </div>

        <div class="pl-10 pr-10 h-[70%] grid grid-cols-1 grid-rows-5 lg:grid-cols-2">
            <Card/>
            <Card/>
        </div>

        <div class="h-[120px] w-full flex justify-center">
            <div class="h-full w-[40%] p-8 flex justify-center">
                <div class="h-full w-[40%] bg-black rounded-3xl flex justify-center items-center">
                    <div class="text-white font-bold text-center text-xl"> Посмотреть еще...</div>
                </div>
            </div>
        </div>

        <div class="pl-40 font-bold text-5xl h-full">
            <div class="">О Компании</div>
        </div>


    </main>

    );
  }
  
  export default Second;