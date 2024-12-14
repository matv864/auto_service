function Footer() {
    return (
      <footer className="bg-[#313030] text-white py-8">
        <div className="max-w-screen-lg mx-auto flex flex-col md:flex-row justify-center items-center gap-8 md:gap-12 px-4">
          <div className="flex items-center gap-4">
            <img
              src="./phone-svgrepo-com.svg"
              alt="Phone"
              className="w-6 h-6 text-orange-500 fill-current"
            />
            <span className="font-bold text-center text-sm sm:text-base">+7 (927) 867-21-45</span>
          </div>
          <div className="flex items-center gap-4">
            <img
              src="./vk-svgrepo-com.svg"
              alt="VK"
              className="w-6 h-6 text-orange-500 fill-current"
            />
            <span className="font-bold text-center text-sm sm:text-base">@cececn</span>
          </div>
          <div className="flex items-center gap-4">
            <img
              src="./instagram-logo-facebook-2-svgrepo-com.svg"
              alt="Instagram"
              className="w-6 h-6 text-orange-500 fill-current"
            />
            <span className="font-bold text-center text-sm sm:text-base">envrnvrn</span>
          </div>
          <div className="flex items-center gap-4">
            <img
              src="./telegram-svgrepo-com.svg"
              alt="Telegram"
              className="w-6 h-6 text-orange-500 fill-current"
            />
            <span className=" font-bold text-center text-sm sm:text-base">@vrhjvnr</span>
          </div>
        </div>
      </footer>
    );
  }
  
  export default Footer;