function Third() {
    return (
        <main id="first" className="relative flex-grow min-h-screen bg-gradient-to-b from-black  to-[#313030] p-6 sm:p-10 grid grid-rows-2 gap-6 items-center">

            <div id="about" className="text-white text-sm sm:text-base lg:text-lg text-center sm:text-left leading-relaxed">
                Компания **EV Service** в Хабаровске — это надежный сервисный центр, который специализируется на профессиональном ремонте и техническом обслуживании автомобилей. Мы обеспечиваем комплексный подход к каждому автомобилю, начиная от точной диагностики и заканчивая полным ремонтом любых узлов и систем.
                <br />
                <br />
                Мы обслуживаем все марки и модели автомобилей, включая легковые, внедорожники и коммерческие машины. Наши опытные механики и инженеры используют только современное оборудование и сертифицированные запчасти, что позволяет нам гарантировать высокое качество и долговечность выполненных работ.
                <br />
                <br />
                В EV Service мы понимаем важность каждой детали: от своевременного технического обслуживания до устранения неисправностей, которые могут повлиять на безопасность и комфорт при эксплуатации автомобиля. В нашем центре можно пройти плановое ТО, диагностику всех систем автомобиля, замену масла, тормозных колодок, фильтров и жидкости, а также более сложные ремонты двигателя, подвески, трансмиссии и электрооборудования.
                <br />
                <br />
                Мы гордимся индивидуальным подходом к каждому клиенту и прозрачностью в расчетах. Наша цель — обеспечить ваш автомобиль качественными услугами по доступным ценам и вернуть его в идеальное техническое состояние. Обращайтесь к нам, и мы гарантируем, что ваш автомобиль будет надежно работать, не доставляя вам неприятных сюрпризов на дороге.
            </div>

            <div className="flex justify-center">
                <img
                    src="/Галерея.png"
                    alt="Галерея EV Service"
                    className="w-full max-w-md sm:max-w-lg lg:max-w-3xl rounded-lg shadow-lg"
                />
            </div>
        </main>
    );
}

export default Third;