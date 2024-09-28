<script lang="ts">
	import '../app.css';
	import Map from '../components/map/Map.svelte';
	import Navbar from '../components/navbar/Navbar.svelte';
</script>

<svelte:head>
	<title>Gieß Bielefeld</title>
</svelte:head>

<div class="flex flex-col min-h-screen min-w-screen">
	<div class="flex flex-col justify-end grow">
		<Map />
		<slot />
	</div>
	<Navbar />
</div>
