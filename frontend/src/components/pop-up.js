import { useEffect, useState } from 'react';

const PopupCard = () => {
  const [showCard, setShowCard] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowCard(true);
    }, 60000); // 60 секунд

    return () => clearTimeout(timer);
  }, []);

  const handleClose = () => {
    setShowCard(false);
  };

  return (
    showCard && (
      <div className="z-20 fixed bottom-4 left-4 bg-orange-500 text-white p-4 rounded-lg shadow-lg flex justify-between items-center">
        <div className="text-black">
          <p>Позвоните нам!!!!</p>
        </div>
        <button
          onClick={handleClose}
          className="ml-4 bg-black text-white p-1 rounded-full w-6 h-6 flex items-center justify-center text-sm"
        >
          ×
        </button>
      </div>
    )
  );
};

export default PopupCard;
