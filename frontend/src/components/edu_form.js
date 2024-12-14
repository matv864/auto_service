import Header from "./header";
import Footer from "./footer";

function Edu_form() {
  return (
    <div className="App flex flex-col min-h-screen">
      <Header />
      <body class="bg-white flex items-center justify-center min-h-screen">
        <div class="bg-black text-white p-8 md:p-16 rounded-2xl w-full max-w-6xl border border-white">
            <h1 class="text-[#E86931] text-3xl md:text-4xl font-bold mb-6 md:mb-10">Header</h1>
                <p class="text-white text-lg md:text-xl mb-8 md:mb-12">
                    Discription
                </p>
                <form action="#" method="POST" class="space-y-6 md:space-y-8">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">
        <div class="grid grid-rows-3 gap-3 md:gap-4">
          <input type="text" name="name" placeholder="Имя..." 
                 class="w-full p-3 md:p-4 bg-white text-black placeholder-black border border-white rounded-2xl text-sm md:text-md focus:outline-none focus:ring-2 focus:ring-white"  />
          <input type="text" name="phone" placeholder="Номер телефона..." 
                 class="w-full p-3 md:p-4 bg-white text-black placeholder-black border border-white rounded-2xl text-sm md:text-md focus:outline-none focus:ring-2 focus:ring-white" />
          <input type="text" name="city" placeholder="Город..." 
                 class="w-full p-3 md:p-4 bg-white text-black placeholder-black border border-white rounded-2xl text-sm md:text-md focus:outline-none focus:ring-2 focus:ring-white"/>
        </div>
        <div>
        </div>
      </div>
      <div class="flex justify-end mt-6 md:mt-8">
        <button type="submit" 
                class="bg-white text-black border border-white font-bold py-3 px-6 md:py-3 md:px-10 rounded-2xl text-lg md:text-xl">
          Отправить
        </button>
      </div>
    </form>
        </div>
    </body>
      <Footer />
    </div>
  );
}

export default Edu_form;
