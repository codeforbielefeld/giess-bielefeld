<script lang="ts">
	import '../app.css';
	import Map from '../components/map/Map.svelte';
</script>

<svelte:head>
	<title>Gieß Bielefeld</title>
</svelte:head>

<div class="flex">
	<Map />
	<div class="z-[700]">
		<slot />
	</div>
</div>