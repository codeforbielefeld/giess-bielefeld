<script lang="ts">
	import '../app.css';
	import Map from '../components/map/Map.svelte';
</script>

<svelte:head>
	<title>Gieß Bielefeld</title>
</svelte:head>

<div class="flex flex-col w-full h-full">
	<div class="flex flex-col grow">

		<div >
			<slot />			
		</div>

			<Map />
	</div>
	<footer class="z-[700] shrink-0 min-h-[10%] bg-red-300 opacity-50">
		Navigations Icons
	</footer>
</div>