import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Educ_card() {
    const navigate = useNavigate(); // Хук для навигации
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
                        <p className="text-2xl text-[#E86931] font-bold">{card.name}</p>
                        <p className="text-md pb-10 lg:text-xl ">{card.description || "Описание отсутствует"}</p>
                        <div className="h-full">
                            <button onClick={() => navigate("/edu_form")} className="bg-white rounded-xl text-black h-full w-[90%] text-center items-center font-bold text-2xl">
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
