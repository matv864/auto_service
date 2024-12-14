import React, { useState } from "react";
import Header from "./header";
import Footer from "./footer";

function Serv_form() {
  const [formData, setFormData] = useState({
    name: "",
    phone: "",
    city: "",
    comment: "",
  });

  // Обработчик изменения данных в форме
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault(); // Предотвращает стандартное поведение отправки формы

    // const data = {
    //   first_name: formData.name, // Например, поле name в форме отправляем как first_name
    //   last_name: "", // Можно добавить если будет поле last_name
    //   additional_contacts: formData.comment,
    //   phone: formData.phone,
    //   service_id: 3, // Используйте правильный ID услуги
    // };

    try {
      // Отправка POST запроса через fetch
      const response = await fetch('https://backend.auto.love-this-domen.ru/service-request', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          "first_name": formData.name,
          "last_name": "",
          "additional_contacts": formData.comment,
          "phone": formData.phone,
          "service_id": 3

        }),
      });

      if (response.ok) {
        // Если запрос успешен, перенаправляем на другую страницу
        window.location.href = "/#head"; // Перенаправление после успешной отправки
      } else {
        console.error('Ошибка отправки данных:', response.statusText);
      }
    } catch (error) {
      console.error('Ошибка сети:', error);
    }
  };

  return (
    <div className="App flex flex-col min-h-screen">
      <Header />
      <body className="bg-white flex items-center justify-center min-h-screen">
        <div className="bg-black text-white p-8 md:p-16 rounded-2xl w-full max-w-6xl border border-white">
          <h1 className="text-[#E86931] text-3xl md:text-4xl font-bold mb-6 md:mb-10">Монтаж, балансировка, снятие/установка "бэдлоков"</h1>
          <p className="text-white text-lg md:text-xl mb-8 md:mb-12">
          По этой услуге мы лучшие в городе
          </p>
          <p className="text-white text-lg md:text-xl font-bold mb-8 md:mb-12">
            Стоимость: <span className="font-bold">от 10000 р.</span>
          </p>
          <form
            onSubmit={handleSubmit}
            className="space-y-6 md:space-y-8"
          >
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">
              <div className="grid grid-rows-3 gap-3 md:gap-4">
                <input
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={handleChange}
                  placeholder="Имя..."
                  className="w-full p-3 md:p-4 bg-white text-black placeholder-black border border-white rounded-2xl text-sm md:text-md focus:outline-none focus:ring-2 focus:ring-white"
                />
                <input
                  type="text"
                  name="phone"
                  value={formData.phone}
                  onChange={handleChange}
                  placeholder="Номер телефона..."
                  className="w-full p-3 md:p-4 bg-white text-black placeholder-black border border-white rounded-2xl text-sm md:text-md focus:outline-none focus:ring-2 focus:ring-white"
                />
                <input
                  type="text"
                  name="city"
                  value={formData.city}
                  onChange={handleChange}
                  placeholder="Город..."
                  className="w-full p-3 md:p-4 bg-white text-black placeholder-black border border-white rounded-2xl text-sm md:text-md focus:outline-none focus:ring-2 focus:ring-white"
                />
              </div>
              <div>
                <textarea
                  name="comment"
                  value={formData.comment}
                  onChange={handleChange}
                  placeholder="Комментарий..."
                  className="h-full w-full p-4 md:p-6 bg-white text-black placeholder-black border-none rounded-2xl text-lg md:text-xl focus:outline-none"
                ></textarea>
              </div>
            </div>
            <div className="flex justify-end mt-6 md:mt-8">
              <button
                type="submit"
                className="bg-white text-black border border-white font-bold py-3 px-6 md:py-3 md:px-10 rounded-2xl text-lg md:text-xl"
              >
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

export default Serv_form;
