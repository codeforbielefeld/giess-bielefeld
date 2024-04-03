<script lang="ts">
	import { supabase } from '../../supabase';
	import { onMount } from 'svelte';
	import 'leaflet/dist/leaflet.css';


	let trees;
	$: trees = [];

	let map: Map;

	let visibleTrees = new Set();

	let min_lat = 52.026731;
	let min_long = 8.5297468;

	let max_lat = 52.0195512;
	let max_long = 8.5474625;

	onMount(async () => {
		const L = await import('leaflet');

		const tileURL: string = "https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/light_nolabels/{z}/{x}/{y}.png"
		//const tileURL: string = `https://{s}.basemaps.cartocdn.com/rastertiles/light_labels_under/{z}/{x}/{y}.png`;
		// const tileURL: string = `https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`;

		const layer = L.tileLayer(tileURL, {
			attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',
			subdomains: 'abcd',
			maxZoom: 20,
			minZoom: 0
		});



		const greenIcon = L.icon({
			iconUrl: 'Baum 2@2x.png',
			iconSize:     [32, 32], // size of the icon
			iconAnchor:   [12, 12], // point of the icon which will correspond to marker's location
			popupAnchor:  [0, -12] // point from which the popup should open relative to the iconAnchor
		});



		const onMove = (e) => {
			const bounds = e.target.getBounds();
			min_lat = bounds._northEast.lat;
			min_long = bounds._northEast.lng;
			max_lat = bounds._southWest.lat;
			max_long = bounds._southWest.lng;
			console.log(min_lat, min_long, max_lat, max_long);
			getTreesInView().then(({ data, error }) => {
				if (error) {
					console.error(error);
				} else {
					trees = data;

					trees.map((tree: unknown) => {
						if (visibleTrees.has(tree.id)) {
							return;
						} else {
							visibleTrees.add(tree.id);
							L.marker([tree.lat, tree.long]).setIcon(greenIcon).addTo(e.target)
								.bindPopup(tree.tree_type_german);
						}
					});
				}
			});
		};

		map = L.map('map', {
			center: [52.02, 8.54],
			zoom: 12
		}).addLayer(layer).on("moveend", onMove);

		onMove({ target: map });


	});


	const getTreesInView = () => {
		return supabase.rpc('trees_in_view', {
			min_lat, min_long, max_lat, max_long
		});
	};
</script>

<!--<div>-->
<!--	<div class="flex row space-x-4">-->
<!--		<div>-->
<!--			<label for="min-lat-input">Längengrad links:</label>-->
<!--			<input id="min-lat-input" type="number" bind:value={min_lat} class="border border-black rounded-sm" />-->
<!--		</div>-->

<!--		<div>-->
<!--			<label for="min-long-input">Breitengrad oben:</label>-->
<!--			<input id="min-long-input" type="number" bind:value={min_long} class="border border-black rounded-sm" />-->
<!--		</div>-->

<!--		<div>-->
<!--			<label for="max-lat-input">Längengrad rechts:</label>-->
<!--			<input id="max-lat-input" type="number" bind:value={max_lat} class="border border-black rounded-sm" />-->
<!--		</div>-->

<!--		<div>-->
<!--			<label for="max-long-input">Breitengrad unten:</label>-->
<!--			<input id="max-long-input" type="number" bind:value={max_long} class="border border-black rounded-sm" />-->
<!--		</div>-->

<!--		<button on:click={()=>getTreesInView()}>Bäume laden</button>-->

<!--	</div>-->

<div id="map" class="w-full h-[1000px]"></div>

<!--	<div>Bäume in der Nähe:</div>-->
<!--	<ul class="list-disc max-h-64 overflow-y-scroll">-->
<!--		{#each trees as tree}-->
<!--			<li>-->
<!--				{tree.tree_type_german}-->
<!--			</li>-->
<!--		{/each}-->
<!--	</ul>-->
<!--</div>-->