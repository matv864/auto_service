import { useEffect, useState } from "react";
import Serv_card from "./Service_card";

function Second_page() {
  const [services, setServices] = useState([]);

  // Получение данных из API
  useEffect(() => {
    const fetchServices = async () => {
      try {
        const response = await fetch("https://backend.auto.love-this-domen.ru/services", {
          headers: {
            accept: "application/json",
          },
        });
        const data = await response.json();
        setServices(data); // Сохраняем данные в стейт
      } catch (error) {
        console.error("Ошибка при загрузке данных:", error);
      }
    };

    fetchServices();
  }, []);

  return (
    <div className="relative p-6 flex-grow h-[150vh] grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 grid-rows-4">
      {services.map((service) => (
        <Serv_card
          key={service.id}
          name={service.name}
          description={service.description}
          price={service.price}
        />
      ))}
    </div>
  );
}

export default Second_page;
