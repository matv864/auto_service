
import { useState, useEffect } from "react";
import Card from "./card";


function Second() {
  const [buttons, setButtons] = useState([]); // Состояние для хранения кнопок
  const [cards, setCards] = useState([]); // Состояние для хранения карточек
  const [activeChannel, setActiveChannel] = useState(null); // Активный канал (ID кнопки)

  // Получение кнопок из API при загрузке компонента
  useEffect(() => {
    fetch("https://backend.auto.love-this-domen.ru/channels")
      .then((response) => response.json())
      .then((data) => {
        setButtons(data); // Устанавливаем кнопки
      })
      .catch((error) => console.error("Ошибка при загрузке кнопок:", error));
  }, []);

  // Функция для загрузки карточек при нажатии на кнопку
  const handleButtonClick = (channelId) => {
    setActiveChannel(channelId); // Устанавливаем активный канал
    fetch(`https://backend.auto.love-this-domen.ru/posts?channel_id=${channelId}`)
      .then((response) => response.json())
      .then((data) => {
        setCards(data); // Устанавливаем карточки
      })
      .catch((error) => console.error("Ошибка при загрузке карточек:", error));
  };


  return (
    <main className="relative w-full h-[150vh] overflow-hidden">
      {/* Блок кнопок */}
      <div className="p-4 h-[200px] grid grid-cols-3 justify-center items-center">
        {buttons.map((button) => (
          <div key={button.id} className="p-8 flex justify-center">
            <button
              className="w-[200px] h-[100px] shadow-xl rounded-3xl bg-black text-white text-bold text-4xl"
              onClick={() => handleButtonClick(button.id)} // Загрузка карточек
            >
              {button.name}
            </button>
          </div>
        ))}
      </div>

      {/* Блок карточек */}
      <div className="pl-10 pr-10 h-full grid grid-cols-1 grid-rows-5 lg:grid-cols-2">
        {cards.map((card, index) => (
          <Card
            key={index}
            title={card.title}
            text={card.text}
            image={card.image}
          />
        ))}
      </div>
    </main>
    );
  }

export default Second;
