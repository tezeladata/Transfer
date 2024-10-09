import backgroundImage from '../assets/background.jpg';
import logo from '../assets/logo.png';

const Hero = () => {
    return (
        <section className="h-full bg-black flex items-center justify-between" style={{ backgroundImage: `url(${backgroundImage})` }}>
            <div className="w-1/2 h-full flex flex-col justify-center items-center">
                <h1 className="font-bold text-8xl text-white p-4 font-MonaSpace text-shadow-glow">GOA website</h1>
                <p className="text-gray-400 text-2xl font-MonaSpace font-bold text-shadow-glow">Website for tasks automation and better data visualization</p>
            </div> 

            <div className="w-1/2 h-full flex justify-center items-center">
                <div className="absolute h-96 w-96 rounded-full bg-gradient-to-r from-green-800 to-green-500 animate-scale" />
                <img src={logo} alt="GOA logo" className="h-1/3 absolute rounded-full hover:shadow-white transition-shadow duration-300" />
            </div>
        </section>
    )
}

export default Hero;