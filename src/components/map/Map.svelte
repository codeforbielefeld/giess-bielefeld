<script lang="ts">
	import { onMount } from 'svelte';
	import L from 'leaflet';
	import 'leaflet/dist/leaflet.css';

	import {MarkerClusterGroup} from  '@tronscanteam/leaflet.markercluster/dist/leaflet.markercluster-src';
	import '@tronscanteam/leaflet.markercluster/dist/MarkerCluster.css';
	import './Map.css';
	import findMatchingSegments from '../../businessLogic/findSegments';


	const id = 'map-' + Math.random().toString(36).substring(2, 9);

	let map: L.Map;

	let visibleSegments = new Set();

	// Icon für Bäume
	//const greenIcon = L.divIcon({
	//	html: '',
	//	className: 'marker-cluster marker-cluster-tree',
	//	iconSize: L.point(10, 10)
	//});
	const greenIcon = L.icon({
	 	iconUrl: '/Tree_Marker.svg',
	 	iconSize: [15, 15], // size of the icon
	 	iconAnchor: [10, 10], // point of the icon which will correspond to marker's location
	 	popupAnchor: [0, -10] // point from which the popup should open relative to the iconAnchor
	});

	const onMove = (e: unknown) => {
		setTimeout(() => {

			const bounds = e.target.getBounds();
			const maxY = bounds._northEast.lat;
			const maxX = bounds._northEast.lng;
			const minY = bounds._southWest.lat;
			const minX = bounds._southWest.lng;
			findMatchingSegments(minX, maxX, minY, maxY).then((segmentFiles) => {
				segmentFiles
				.filter((segmentFile) => !visibleSegments.has(segmentFile))
				.forEach((segmentFile) => {
					fetch(`/segments/${segmentFile}`)
					.then((response) => {
						return response.json();
					})
					.then((segment) => {
						visibleSegments.add(segmentFile);
						const markers = new MarkerClusterGroup({
							spiderfyOnMaxZoom: false,
							showCoverageOnHover: false,
							zoomToBoundsOnClick: true,
							disableClusteringAtZoom: 20,
							iconCreateFunction: (cluster: unknown) => {
								if (cluster.getChildCount() > 1000) {
									console.log("Found > 100 group: ", cluster, cluster.getChildCount())
									return L.divIcon({
										html: '',
										className: 'marker-cluster',
										iconSize: L.point(100, 100)
									});
								} else if (cluster.getChildCount() > 500) {
									console.log("Found > 100 group: ", cluster, cluster.getChildCount())
									return L.divIcon({
										html: '',
										className: 'marker-cluster',
										iconSize: L.point(50, 50)
									});
								} 
								else if (cluster.getChildCount() > 100) {
									console.log("found group > 50 with count: ", cluster, cluster.getChildCount())
									return L.divIcon({
										html: '',
										className: 'marker-cluster',
										iconSize: L.point(10, 10)
									});
								} else {
									console.log("found else cluster group: ", cluster, cluster.getChildCount())
									return L.divIcon({
										html: '',
										className: 'marker-cluster',
										iconSize: L.point(20, 20)
									});
								}
								// return L.divIcon({ html: '', className: 'marker-cluster marker-cluster-small', iconSize: L.point(70, 40)});
							}
						}).addTo(map);
						L.geoJSON(segment, {
							pointToLayer: function(feature, latlng) {
								return L.marker(latlng, { icon: greenIcon });
							}
						}).addTo(markers);
					});
				});
			});
		}, 50);
	};

	onMount(async () => {
		const tileURL: string = 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/light_nolabels/{z}/{x}/{y}.png';

		// Overlay Copyright
		const layer = L.tileLayer(tileURL, {
			attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',
			subdomains: 'abcd',
			maxZoom: 20,
			minZoom: 0
		});

		map = L.map(id, {
			center: [52.0192873, 8.5301909],
			zoom: 16
		})
			.addLayer(layer)
			.on('moveend', onMove);


		onMove({ target: map });
	});

</script>

<div {id} class="w-full h-full" />
