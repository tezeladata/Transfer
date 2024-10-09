import mtskheta from '../assets/Mtskheta.png';

const About = () => {
    return (
        <section className="h-1/2">
            <div className="w-full h-full flex items-center justify-center pt-10"> {/* container */}
                <div className="w-1/2 flex items-center justify-center relative mx-auto h-auto overflow-hidden rounded-lg">
                    <img src={mtskheta} alt="Mtskheta image aerial" className="w-3/5 h-auto relative z-0 rounded-lg scale-110 transition-all duration-300 hover:scale-100"/>
                </div>

                <div className="w-1/2 h-full flex flex-col items-start justify-start pt-10">
                    <div className="relative h-max">
                        <div className="w-14 h-2 bg-black rounded-full absolute top-1/2 -left-10"></div>
                        <p className="text-3xl font-bold pt-4 pb-4 pl-8 pr-8 bg-green-800 border-4 border-black rounded-full max-w-sm mx-auto h-auto shadow-none transition-shadow duration-300 cursor-pointer hover:shadow-lg hover:shadow-gray-400">GOA <span className="text-white">Website</span></p>
                    </div>
                    <h2 className="font-bold text-6xl max-w-screen-md mb-10 mt-10 cursor-pointer">Website to automate tasks and visualize <span className="text-green-800">data.</span></h2>
                    <p className="font-semibold max-w-lg mb-10">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid animi commodi eligendi eveniet ex facilis nemo nulla numquam odit sint. Atque eaque earum in ipsum magni nesciunt nisi pariatur quis saepe, voluptas? Aspernatur blanditiis consectetur earum, facere fugiat illum incidunt maxime minima nihil numquam omnis quibusdam recusandae rem. Incidunt, nesciunt.</p>
                    <span className="text-2xl font-bold text-gray-300 pt-2 pb-2 pl-6 pr-6 bg-green-800 rounded-3xl cursor-pointer hover:bg-gradient-to-t from-green-900 to-green-900 transition-all duration-500 ease-in-out flex justify-center items-center">Log in</span>
                </div>
            </div>
        </section>
    )
}

export default About;