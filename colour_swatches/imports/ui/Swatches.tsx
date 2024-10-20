import React, { useState } from 'react';
import { HTTP } from 'meteor/http'

export const Swatches = () => {
  let [swatches, setSwatches] = useState([{type: "RGB", red: 213, green: 12, blue: 234},
  {type: "RGB", red: 123, green: 112, blue: 111},
  {type: "RGB", red: 23, green: 123, blue: 32},
  {type: "RGB", red: 67, green: 57, blue: 30},
  {type: "HSL", hue: 167, saturation: 100, lightness: 100},
  ])

  const generate = () => {
    console.log("here")
    HTTP.call("GET", "http://127.0.0.1:8000/generate_colours", {}, (err, res) => {
      setSwatches(res?.data.colours)
      console.log(swatches)
    })
  };

  return (
    <div>
      <button className='border-black border rounded-3xl px-3 py-3' onClick={generate}>Generate swatches</button>
      <div className='flex justify-between'>
        {swatches.map((swatch, index) => {
          return (
            <div key={index} className={`px-10 py-10`} style={{backgroundColor: `${
              swatch.type == "RGB" ? 
              `rgb(${swatch.red},${swatch.green},${swatch.blue})`
              : 
              `color:hsl(${swatch.hue},${swatch.saturation}%,${swatch.lightness})`
            }`}}></div>
          )
        })}
      </div>
    </div>
  );
};
