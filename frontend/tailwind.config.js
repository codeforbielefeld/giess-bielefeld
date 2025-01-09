/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			spacing: {
				128: '32rem',
				'3/4': '75vh'
			},
			colors: {
				green: {
					50: '#f0f9f5',
					100: '#daf1e5',
					200: '#b7e3ce',
					300: '#88cdb1',
					400: '#51af8b',
					500: '#97cfb9',
					600: '#24775b',
					700: '#1d5f4b',
					800: '#194c3d',
					900: '#153f33',
					950: '#0b231d'
				},
				gray: {
					150: '#efefef'
				}
			}
		}
	},
	plugins: []
};
