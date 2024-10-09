import image1 from "../assets/logo.png";

const Navbar = () => {
    return (
        <section className="h-20 bg-gray-200 flex items-center justify-between fixed w-full z-50 shadow-2xl">
            <div className="h-full w-1/4 flex items-center justify-center">
                <img src={image1} alt="GOA logo" className="h-2/4 rounded-full cursor-pointer" />
                <p className="pl-4 font-bold text-2xl cursor-pointer">GOA <span className="text-green-800">Website</span></p>
            </div>

            <div className="h-full w-1/4 flex items-center justify-center">
                <span
                    className="text-2xl font-bold text-gray-300 pt-2 pb-2 pl-6 pr-6 mr-4 bg-green-800 rounded-3xl cursor-pointer hover:bg-gradient-to-t from-green-900 to-green-900 transition-all duration-500 ease-in-out flex justify-center items-center">Register</span>
                <span className="text-2xl font-bold text-gray-300 pt-2 pb-2 pl-6 pr-6 bg-green-800 rounded-3xl cursor-pointer hover:bg-gradient-to-t from-green-900 to-green-900 transition-all duration-300 ease-in-out flex justify-center items-centerr">Log in</span>
            </div>
        </section>
    )
}

export default Navbar;