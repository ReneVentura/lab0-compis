import React from 'react';
import { Parallax, ParallaxLayer } from '@react-spring/parallax';
import bg from '../assets/img/Bg.jpg';
import axios from "axios";

import { useEffect } from 'react';


const Home = () => {
    const [inputText, setInputText] = useState("");

    function handleInputChange(event) {
        setInputText(event.target.value);
    }

    
  function getData() {
    axios({
      method: "POST",
      url:"/tree",
      data: { text: inputText }
    })
    .then((response) => {
      const res =response.data
      console.log(res)
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        }
    })}

    useEffect(() => {
        getData();
    }, []);






    const backgroundImage = bg;

    return (
        <div>
            <Parallax pages={2}>
                <ParallaxLayer
                    speed={2}
                    factor={6}
                    className="w-screen h-screen z-0"
                    style={{
                        backgroundImage: `url(${backgroundImage})`,
                        backgroundSize: 'cover',
                        backgroundPosition: 'left',
                    }}
                />
                <ParallaxLayer factor={1} offset={0} speed={0.5}>
                    <div className='flex flex-col items-center justify-center'>
                        <h1 className='text-white text-6xl font-text p-10 pt-60'>Bienvenidos!</h1>
                        <h1 className='text-white text-4xl font-text mt-5'> Al proyecto #1 de Compiladores</h1>
                        <h1 className='text-white text-4xl font-text mt-20'> Este Proyecto fue realizado por :
                            <br></br>
                            <br></br>
                           <strong> Diego Crespo 19541 </strong>
                            <br></br>
                           <strong> Rene Ventura 19554  </strong>
                        </h1>
                    </div>

                    <div className='flex flex-col items-center justify-center h-screen'>
                        <h1 className='text-white text-4xl font-text mt-20'>
                            Por favor ingrese en el recuadro de a continuacion su expresion a evaluar.
                        </h1>


                        <div className='mt-36 w-11/12 bg-gray-400 h-screen pb-10 flex flex-col items-center justify-center'>
                            <textarea  className='bg-white mt-20 w-10/12 h-5/6 p-5 font-text'
                            value={inputText}
                            onChange={handleInputChange}
                            >
                                
                            </textarea >

                            <button className='bg-white mt-5 w-1/6 font-text border border-white'
                            onClick={postData}
                            >
                                 Evaluar                          
                            </button>

                        </div>


                        
                 
                    </div>
                    <h1 className='text-white text-4xl font-text mt-40 '> Esto fue todo por este Proyecto 1
                            <br></br>
                            <br></br>
                           <strong> Muchas Gracias! </strong>
                            <br></br>
                           <strong> Hasta la Proxima!  </strong>
                        </h1>
                </ParallaxLayer>
            </Parallax>
        </div>
    );
};

export default Home;
