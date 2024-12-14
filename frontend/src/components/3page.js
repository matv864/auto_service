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

            <div className="h-full w-full p-4">
    <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2">
    {/* Первая картинка */}
    <div className="relative overflow-hidden">
      <img
        src="/image 6.png"
        alt="Image 1"
        className="object-cover w-full h-full rounded-lg shadow-lg"
      />
    </div>

    {/* Вторая картинка */}
    <div className="relative overflow-hidden">
      <img
        src="/image 7.png"
        alt="Image 2"
        className="object-cover w-full h-full rounded-lg shadow-lg"
      />
    </div>

    {/* Третья картинка */}
    <div className="relative overflow-hidden">
      <img
        src="/image 7-1.png"
        alt="Image 3"
        className="object-cover w-full h-full rounded-lg shadow-lg"
      />
    </div>


    {/* Пятая картинка */}
    <div className="relative overflow-hidden">
      <img
        src="/image 8.png"
        alt="Image 5"
        className="object-cover w-full h-full rounded-lg shadow-lg"
      />
    </div>

    {/* Шестая картинка */}
    <div className="relative overflow-hidden">
      <img
        src="/image 6.png"
        alt="Image 6"
        className="object-cover w-full h-full rounded-lg shadow-lg"
      />
    </div>

    {/* Седьмая картинка */}
    <div className="relative overflow-hidden">
      <img
        src="/image.png"
        alt="Image 7"
        className="object-cover w-full h-full rounded-lg shadow-lg"
      />
    </div>
  </div>
</div>


            
        </main>
    );
}

export default Third;