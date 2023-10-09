import React, { useState } from 'react';
import { Parallax, ParallaxLayer } from '@react-spring/parallax';
import bg from '../assets/img/Bg.jpg';
import axios from 'axios';

const Home = () => {
  const backgroundImage = bg;
  const [inputText, setInputText] = useState('');
  const [mipsAssembly, setMipsAssembly] = useState('');

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const postData = () => {
    axios({
      method: 'POST',
      url: 'http://127.0.0.1:5000/getcode',
      data: { text: inputText },
    })
      .then((response) => {
        const res = response.data;

        // Clean up the "formatted_tree" property
        const formattedTree = res.formatted_tree;
        const cleanedFormattedTree = formattedTree.replace(/\n+/g, '');
        res.formatted_tree = cleanedFormattedTree;

        console.log(res);

        // Update the first textbox with formatted_tree and symbol_table
        setInputText(JSON.stringify({ formatted_tree: res.formatted_tree, symbol_table: res.symbol_table }, null, 2));

        // Update the second textbox with mips_assembly
        setMipsAssembly(res.mips_assembly.join('\n'));
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
        }
      });
  };

  const getData = () => {
    axios({
      method: 'GET',
      url: 'http://127.0.0.1:5000/getcode',
    })
      .then((response) => {
        const res = response.data;
        console.log(res);
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
        }
      });
  };

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
          <div className="flex flex-col items-center justify-center">
            <h1 className="text-white text-6xl font-text p-10 pt-60">Bienvenidos!</h1>
            <h1 className="text-white text-4xl font-text mt-5"> Al proyecto #1 de Compiladores</h1>
            <h1 className="text-white text-4xl font-text mt-20">
              Este Proyecto fue realizado por :
              <br />
              <br />
              <strong> Diego Crespo 19541 </strong>
              <br />
              <strong> Rene Ventura 19554 </strong>
            </h1>
          </div>

          <div className="flex flex-col items-center justify-center h-screen">
            <h1 className="text-white text-4xl font-text mt-20">
              Por favor ingrese en el recuadro de a continuacion su expresion a evaluar.
            </h1>

            <div className="mt-36 w-11/12 bg-gray-400 h-screen pb-10 flex flex-col items-center justify-center">
              <textarea
                className="bg-white mt-20 w-10/12 h-screen p-5 font-text"
                value={inputText}
                onChange={handleInputChange}
                style={{ fontVariantLigatures: 'none' }}
              ></textarea>

              <button
                className="bg-white mt-5 w-1/6 font-text border border-white"
                onClick={postData}
              >
                Evaluar
              </button>
              <button
                className="bg-white mt-5 w-1/6 font-text border border-white"
                onClick={getData}
              >
                Probar
              </button>
            </div>

            <div className="mt-5 w-10/12 bg-white p-5 font-text">
              <h2>MIPS Assembly:</h2>
              <textarea
                className="bg-white w-full h-96 p-5"
                value={mipsAssembly}
                readOnly
                style={{ fontVariantLigatures: 'none' }}
              ></textarea>
            </div>
          </div>
          <h1 className="text-white text-4xl font-text mt-40 ">
            Esto fue todo por este Proyecto 1
            <br />
            <br />
            <strong> Muchas Gracias! </strong>
            <br />
            <strong> Hasta la Proxima! </strong>
          </h1>
        </ParallaxLayer>
      </Parallax>
    </div>
  );
};

export default Home;
