import { useState, useEffect } from "react";
import Card from "./card";

function Second() {
  const [channels, setChannels] = useState([]);
  const [content, setContent] = useState([]);
  const [loading, setLoading] = useState(false);
  const [activeChannel, setActiveChannel] = useState(null); // Хранит активный канал

  // Загружаем каналы при монтировании компонента
  useEffect(() => {
    const fetchChannels = async () => {
      try {
        const response = await fetch('https://backend.auto.love-this-domen.ru/channels');
        const data = await response.json();
        setChannels(data);

        // Если каналы загружены, сразу отображаем первый
        if (data.length > 0) {
          handleChannelClick(data[0].id);
        }
      } catch (error) {
        console.error("Ошибка при загрузке каналов:", error);
      }
    };
    fetchChannels();
  }, []);

  // Функция для загрузки контента для конкретного канала
  const handleChannelClick = async (channelId) => {
    setLoading(true);
    setActiveChannel(channelId); // Устанавливаем активный канал
    try {
      const response = await fetch(`https://backend.auto.love-this-domen.ru/posts?channel_id=${channelId}`);
      const data = await response.json();
      setContent(data);
    } catch (error) {
      console.error("Ошибка при загрузке контента:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="relative w-full min-h-screen overflow-hidden">
      <div className="p-4 grid grid-cols-3 gap-4 items-center">
        {/* Динамически создаём кнопки */}
        {channels.map((channel) => (
          <div className="flex justify-center" key={channel.id}>
            <button
              id="proj"
              className={`w-[150px] sm:w-[200px] h-[60px] sm:h-[100px] shadow-xl rounded-3xl font-bold text-sm sm:text-xl ${
                activeChannel === channel.id
                  ? "bg-orange-500 text-white " // Активная кнопка
                  : "bg-black text-white" // Неактивная кнопка
              }`}
              onClick={() => handleChannelClick(channel.id)}
            >
              {channel.name}
            </button>
          </div>
        ))}
      </div>

      {/* Отображаем карточки контента */}
      <div className="px-4 pb-4 sm:px-10 grid grid-cols-1 xl:grid-cols-2 gap-6">
        {loading ? (
          <p className="text-white">Загрузка...</p>
        ) : (
          content.map((item, index) => (
            <Card key={index} title={item.title} text={item.text} image={item.image} />
          ))
        )}
      </div>

      <div className="h-[120px] flex justify-center items-center">
        <button className="h-[50px] sm:h-[80px] w-[70%] sm:w-[40%] bg-black rounded-3xl absolute bottom-[40px] sm:bottom-[40px] flex justify-center items-center shadow-lg">
          <div className="text-white font-bold text-center text-sm sm:text-lg">
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