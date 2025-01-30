<script lang="ts">
	import { onMount } from 'svelte';
	import L, { popup } from 'leaflet';
	import 'leaflet/dist/leaflet.css';
	import { goto } from '$app/navigation';

	import { MarkerClusterGroup } from '@tronscanteam/leaflet.markercluster/dist/leaflet.markercluster-src';
	import '@tronscanteam/leaflet.markercluster/dist/MarkerCluster.css';
	import './Map.css';
	import findMatchingSegments from '../../businessLogic/findSegments';
	import Layout from '../../routes/+layout.svelte';

	const id = 'map-' + Math.random().toString(36).substring(2, 9);

	let map: L.Map;

	let visibleSegments = new Set();

	const iconDefaults = {
		html: '',
		className: 'marker-cluster'
	};

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

	const greenIconClicked = L.icon({
		iconUrl: '/Tree_Marker_Clicked.svg',
		iconSize: [15, 15], // size of the icon
		iconAnchor: [10, 10], // point of the icon which will correspond to marker's location
		popupAnchor: [0, -10] // point from which the popup should open relative to the iconAnchor
	});

	let last_clicked: unknown = null;

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
										const childCount = cluster.getChildCount();
										const iconSize =
											childCount > 1000 ? 100 : childCount > 500 ? 50 : childCount > 100 ? 10 : 20;
										return L.divIcon({
											...iconDefaults,
											iconSize: L.point(iconSize, iconSize)
										});
									}
								}).addTo(map);
								L.geoJSON(segment, {
									pointToLayer: function (feature, latlng) {
										return L.marker(latlng, { icon: greenIcon }).on('click', function (e) {
											if (last_clicked != null && last_clicked._icon != null) {
												last_clicked._icon.src = '/Tree_Marker.svg';
											}
											e.target._icon.src = '/Tree_Marker_Clicked.svg';
											let treeId = e.sourceTarget.feature.properties.uuid;
											goto(`/trees/${treeId}`);
											if (e.target._icon != null) {
												last_clicked = e.target;
											}

											// center tree above card
											const lat1 = map.getBounds()._northEast.lat;
											const lat2 = map.getBounds()._southWest.lat;
											const latb = e.latlng.lat;
											const latn = latb - Math.abs(lat1 - lat2) / 2.35;
											map.panTo({ lat: latn, lng: e.latlng.lng });
										});
									}
								}).addTo(markers);
							});
					});
			});
		}, 50);
	};

	onMount(async () => {
		const tileURL: string =
			'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/light_nolabels/{z}/{x}/{y}.png';

		// Overlay Copyright
		const layer = L.tileLayer(tileURL, {
			attribution:
				'&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',
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

		const mapElement = document.querySelector('#' + id);

		mapElement?.addEventListener('click', function (e) {
			if (e.target && !e.target.className.includes('leaflet-marker-icon')) {
				goto('/');
			}
		});
	});
</script>

<!-- Map START -->
<div {id} class="absolute top-0 left-0 min-w-full min-h-full" />
<!-- Map END -->
