function Card({ title, text, image }) {
    return (
        <div className="m-4 shadow-xl bg-black rounded-3xl flex justify-between items-center p-4">
            <div className="h-full w-[40%] p-4">
                <div className="h-full w-full rounded-xl bg-white">
                    <img src={image} alt="" className="rounded-xl w-full h-full"></img>
                </div>
            </div>
            <div className="h-full w-full pl-4 pt-2">
                <p className="text-white text-5xl">{title}</p>
                <p className="text-white text-xl">{text}</p>
            </div>
        </div>
    );
}

export default Card;
