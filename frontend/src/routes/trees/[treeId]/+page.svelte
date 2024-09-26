<!--Seite für 1 individuellen Baum :) -->
<script lang="ts">
	import { Accordion, AccordionItem } from 'svelte-collapsible'
	import WaterColumn from "../../../components/WaterColumn.svelte";
	export let data;
	console.log(data.treeId);

	let testreeprops = {"pitID": "00008100:00c0fbd5",
	"Standort_N": 1,
	"Zusatz": null,
	"laufende_n": "1",
	"gefaellt": 0,
	"Stammdurch": 80.0,
	"Kronendurc": 12.0,
	"Baumhoehe_": 21.0,
	"Stammumfan": 251.33,
	"Baumgruppe": 0,
	"Bezirk_Nr": "11",
	"Bezirk_Bez": "WEST - BUERGERPARK",
	"Objekt_Nr": "001",
	"Objekt_Bez": "GA BÃ¼rgerpark",
	"Baumart_bo": "Quercus robur",
	"Baumart_de": "Stiel-Eiche",
	"Baumart_ku": "q r",
	"PflE_Art_N": "1270",
	"PflE_Art_B": "Einzelbaum",
	"Stammradiu": 40.0,
	"Kronenradi": 6.0 ,
	"geometry": { "type": "Point", "coordinates": [ 8.511457515202823, 52.026940411111674 ] },
	"waterdata": [
				{
					source: 'Dir',
					amount: 20
				},
				{
					source: 'Peter',
					amount: 10
				},
				{
					label: 'Stadt',
					amount: 30,
				},
				{
					label: 'Regen',
					amount: 30,
				}
			]
		} ;


		const { 
			Baumart_de: art_de, 
			Stammdurch: durchmesser_stamm,
			Kronendurc: durchmesser_krone,
			Baumhoehe_: hoehe,
			Stammumfan: umfang_stamm,
			waterdata: water_history,
			} = testreeprops;


</script>

<div class="mx-auto">
<div class="container">

	<div class="absolute w-full h-[85%] bottom-0 self-center justify-center z-[700] bg-white">
		<p>{art_de}, ALTER</p>
		<Accordion>
			<AccordionItem key='a'>
				<h2 slot='header'>
					Über diesen Baum
					<button><img src="/plusButton.svg"/></button>
				</h2>
				<p slot='body'>
					Höhe: {hoehe}<br>
					Kronendurchmesser: {durchmesser_krone}<br>
					Stammdurchmesser: {durchmesser_stamm}
				</p>
			</AccordionItem>
		</Accordion>
		<WaterColumn {water_history}/>
	</div>

	


</div>
</div>



