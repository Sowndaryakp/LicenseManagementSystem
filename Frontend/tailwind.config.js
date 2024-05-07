/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        'deep-cerulean': {
          '50': '#f1fafe',
          '100': '#e1f4fd',
          '200': '#bce9fb',
          '300': '#81d8f8',
          '400': '#3fc4f1',
          '500': '#16aee1',
          '600': '#0880af',
          '700': '#08709c',
          '800': '#0b5f81',
          '900': '#0f4e6b',
          '950': '#0a3347',
        },
        
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
