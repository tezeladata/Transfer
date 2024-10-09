import logo from '../assets/logo.png';
import facebook from '../assets/facebook.png';
import youtube from '../assets/youtube.png';
import github from '../assets/github.png';

const FooterMain = () => {
    return (
        <div className="pt-10 pb-10 px-72 shadow-2xl"> {/* container */}
            <div className="bg-green-900 border-top-custom flex items-center justify-start">
                <div className="h-16 w-16 ml-64 rounded-full bg-white cursor-pointer"></div>
                <p className="pt-16 pb-16 pl-8 text-white font-bold text-3xl cursor-pointer font-MonaSpace">Contact us</p>
            </div>

            <div className="bg-neutral-950 text-white border-bottom-custom"> {/* bottom part container */}
                <div className="ml-64 mr-64 pt-16 pb-16 grid grid-cols-2 gap-6"> {/* Main part */}
                    <div className="flex flex-col items-start justify-between">
                        <div className="flex items-center">
                            <img src={logo} alt="GOA logo" className="h-16 w-16 rounded-full cursor-pointer text-shadow-glow" />
                            <span className="pl-6 text-2xl cursor-pointer font-MonaSpace text-shadow-glow">Goal-Oriented <span>Academy</span></span>
                        </div>

                        <p className="pt-6">Lorem ipsum dolor sit amet consectetur adipisicing elit. Exercitationem laboriosam nemo tenetur ut libero consectetur tempore maiores repellat enim, dicta eos, iusto molestiae nam! Illum voluptas ad amet consectetur vel.</p>

                        <div className="flex items-center pt-10">
                            <a href="https://www.facebook.com/nika11keshelava" target='_blank'>
                                <img src={facebook} alt='facebook' />
                            </a>

                            <a href="https://www.youtube.com/@Goal_Oriented_Academy__GOA" className="pl-6" target='_blank'>
                                <img src={youtube} alt='youtube' />
                            </a>

                            <a href="https://github.com/GoaSoftwareDevelopment" className="pl-6" target='_blank'>
                                <img src={github} alt='github' />
                            </a>
                        </div>
                    </div>

                    <div className="flex flex-col items-center justify-between">
                        <p className="text-3xl font-bold">Useful links</p>
                        <a href="https://www.facebook.com/nika11keshelava" target="_blank">GOA facebook</a>
                        <a href="https://www.youtube.com/@Goal_Oriented_Academy__GOA" target="_blank">GOA youtube</a>
                        <a href="https://github.com/GoaSoftwareDevelopment" target="_blank">Software development team github</a>
                        <a href="https://docs.google.com/spreadsheets/d/1xGdFtDe28yY9fpQ14Y83JXgGCtsvYfHqYSDUD_7taiQ/edit?usp=sharing" target="_blank">Leaders sheet</a>
                        <a href="https://drive.google.com/drive/folders/1GLYEj20NThU341mmt7l1g3NnA024MWDp?usp=sharing" target="_blank">Github control sheets</a>
                    </div>
                </div>

                <div className="pt-20 mr-64 ml-64 pb-10"> {/* For copyright */}
                    <div className="w-full h-1 bg-white"></div>
                    <p className="pt-4 cursor-pointer">© Copyright 2024 By GSD</p>
                </div>
            </div>
        </div>
    )
}

export default FooterMain;