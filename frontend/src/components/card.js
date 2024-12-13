function Card({ title, text, image }) {
    return (
      <div className="ml-8 mr-8 shadow-xl bg-black rounded-3xl flex justify-between items-center p-4">
        <div className="h-full w-[40%] sm:p-4">
          <div className="h-full w-full rounded-xl bg-white">
            {/* Используем переданный пропс image для отображения изображения */}
            <img src={image || "/images/default-image.png"} className="rounded-xl w-full h-full" alt={title} />
          </div>
        </div>
        <div className="h-full w-full pl-[4px] sm:pl-4 sm:pt-2">
          {/* Используем переданный пропс title */}
          <p className="text-white text-xl sm:text-5xl">{title}</p>
          {/* Используем переданный пропс text */}
          <p className="text-white text-[15px] sm:text-xl">{text}</p>
        </div>
      </div>
    );
  }
  
  export default Card;
  