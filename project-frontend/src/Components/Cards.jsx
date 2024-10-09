import cardBackground from '../assets/card-background.png';

const cardData = [
    {
        title: "Big database",
        description: "Database includes all GOA members",
    },
    {
        title: "Special roles",
        description: "Roles for leaders and department members",
    },
    {
        title: "Data visualization",
        description: "Leaders can see all their info in panel",
    },
    {
        title: "Github control",
        description: "Github controllers work directly from this website",
    },
];

const Cards = () => {
    return (
        <section className="h-2/5 w-full flex flex-col items-center justify-center">
            <h2 className="text-7xl pb-20 pt-10 font-bold font-MonaSpace">About us</h2>
            <div className="grid grid-cols-4 gap-12 h-1/2 w-4/5">
                {cardData.map((card, index) => (
                    <div
                        key={index}
                        className="flex flex-col items-center justify-center rounded-xl bg-cover bg-center h-64 w-full bg-green-800 cursor-pointer shadow-inner transition-all duration-300 hover:scale-110"
                        style={{ backgroundImage: `url(${cardBackground})` }}
                    >
                        <div className="w-24 h-24 rounded-full bg-green-800 mb-4 hover:shadow-white transition-shadow duration-300"></div>
                        <h2 className="text-4xl font-bold text-white">{card.title}</h2>
                        <p className="text-xl text-center max-w-sm text-white">{card.description}</p>
                    </div>
                ))}
            </div>
        </section>
    )
}

export default Cards;