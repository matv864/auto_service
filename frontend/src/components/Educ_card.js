import { useState, useEffect } from "react";

function Educ_card() {
    const [cards, setCards] = useState([]);

    useEffect(() => {
        fetch("https://backend.auto.love-this-domen.ru/directions", {
            method: "GET",
            headers: {
                accept: "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => setCards(data))
            .catch((error) => console.error("Ошибка загрузки данных:", error));
    }, []);

    return (
        <>
            {cards.map((card) => (
                <div key={card.id} className="flex justify-center p-4">
                    <div className="h-full w-[90%] bg-black rounded-2xl grid grid-rows-3 justify-center items-center text-white text-center p-4">
                        <p className="text-3xl">{card.name}</p>
                        <p className="text-xl">{card.description || "Описание отсутствует"}</p>
                        <div className="h-full">
                            <button className="bg-white rounded-xl text-black h-full w-[90%] text-center items-center font-bold text-2xl">
                                Записаться
                            </button>
                        </div>
                    </div>
                </div>
            ))}
        </>
    );
}

export default Educ_card;
