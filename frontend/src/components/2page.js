import React, { useState } from "react";
import Card from "./card";

function Second() {
    const [posts, setPosts] = useState([]); // Храним данные карточек

    // Функция для загрузки данных с API
    const fetchPosts = async (channelId) => {
        try {
            const response = await fetch(`https://auto.love-this-domen.ru/posts?channel_id=${channelId}`, {
                headers: { "accept": "application/json" },
            });
            const data = await response.json();
            setPosts(data); // Устанавливаем данные карточек
        } catch (error) {
            console.error("Ошибка при загрузке данных:", error);
        }
    };

    return (
        <main className="relative w-full h-[150vh] overflow-hidden">
            {/* Блок с кнопками */}
            <div className="p-4 h-[200px] grid grid-cols-3 justify-center items-center">
                <div className="p-8 flex justify-center">
                    <button
                        className="w-[200px] h-[100px] shadow-xl rounded-3xl bg-black text-white font-bold text-4xl"
                        onClick={() => fetchPosts(1)} // Айди 1 — Проекты
                    >
                        Проекты
                    </button>
                </div>
                <div className="p-8 flex justify-center">
                    <button
                        className="w-[200px] h-[100px] shadow-xl rounded-3xl bg-black text-white font-bold text-4xl"
                        onClick={() => fetchPosts(2)} // Айди 2 — Новости
                    >
                        Новости
                    </button>
                </div>
                <div className="p-8 flex justify-center">
                    <button
                        className="w-[200px] h-[100px] shadow-xl rounded-3xl bg-black text-white font-bold text-4xl"
                        onClick={() => fetchPosts(3)} // Айди 3 — Отзывы
                    >
                        Отзывы
                    </button>
                </div>
            </div>

            {/* Блок с карточками */}
            <div className="pl-10 pr-10 h-full grid grid-cols-1 grid-rows-5 lg:grid-cols-2">
                {posts.map((post, index) => (
                    <Card
                        key={index}
                        title={post.title || "Заголовок отсутствует"}
                        text={post.text || "Текст отсутствует"}
                        image={post.image || "/images/default.png"} // Показываем картинку по умолчанию, если её нет
                    />
                ))}
            </div>
<<<<<<< HEAD
        </main>
=======
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
            <p class="">О Компании</p>
        </div>


    </main>

>>>>>>> origin/main
    );
}

export default Second;
