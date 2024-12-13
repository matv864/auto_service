import { useEffect, useState } from 'react';

const PopupCard = () => {
  const [showCard, setShowCard] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowCard(true);
    }, 60000); // 60 секунд

    return () => clearTimeout(timer);
  }, []);

  return (
    showCard && (
      <div className=" z-20 fixed bottom-4 right-4 bg-orange-500 text-white p-4 rounded-lg shadow-lg">
        <div className="text-black">
          <p>Позвоните нам</p>
        </div>
      </div>
    )
  );
};

export default PopupCard;
