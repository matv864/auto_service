import { useState, useEffect } from "react";
import Card from "./card";

function Second() {
  // Состояние для каналов и контента
  const [channels, setChannels] = useState([]);
  const [content, setContent] = useState([]);
  const [loading, setLoading] = useState(false);

  // Загружаем каналы при монтировании компонента
  useEffect(() => {
    const fetchChannels = async () => {
      try {
        const response = await fetch('https://backend.auto.love-this-domen.ru/channels');
        const data = await response.json();
        setChannels(data);
      } catch (error) {
        console.error("Ошибка при загрузке каналов:", error);
      }
    };
    fetchChannels();
  }, []);

  // Функция для загрузки контента для конкретного канала
  const handleChannelClick = async (channelId) => {
    setLoading(true);
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
              className="w-[150px] sm:w-[200px] h-[60px] sm:h-[100px] shadow-xl rounded-3xl bg-black text-white font-bold text-2xl sm:text-3xl "
              onClick={() => handleChannelClick(channel.id)}
            >
              {channel.name}
            </button>
          </div>
        ))}
      </div>

      {/* Отображаем карточки контента */}
      <div className="px-4 sm:px-10 grid grid-cols-1 md:grid-cols-2 gap-6">
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
