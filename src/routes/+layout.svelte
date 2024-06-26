<script lang="ts">
	import '../app.css';
	import Map from '../components/map/Map.svelte';
</script>

<svelte:head>
	<title>Gieß Bielefeld</title>
</svelte:head>

<Map />
<div class="absolute bottom-0 z-[700]">
	<slot />
</div>
