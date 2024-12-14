function Header() {
    return (
      <header id="head" class="bg-[#201F1F] text-white py-4 border-b-4 border-orange-500">
        <div class="container mx-auto">
          <nav class="flex justify-center items-center" >
            <div class="size-20">
              <a href="/#head">
                <img src="/images/logo.png"></img>
              </a>
              
            </div>
            <text class="ml-20 grid grid-cols-4 gap-10 sm:gap-20 lg:gap-40 xl:gap-60 hidden md:flex sm:text-sm lg:text-lg font-bold"> 
              <a href="/#about" class="hover:underline">О компании</a>
              <a href="/service" class="hover:underline">Услуги</a>
              <a href="/#proj" class="hover:underline">Проекты</a>
              <a href="/education" class="hover:underline">Обучение</a>
            </text>
          </nav>
        </div>
      </header>
    );
  }
  
  export default Header;
  