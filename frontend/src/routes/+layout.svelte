<script lang="ts">
	import '../app.css';
	import Map from '../components/map/Map.svelte';
	import { goto } from '$app/navigation';

	$: isOpen = false;
	$: console.log(isOpen)
	async function handleButtonbarClick(buttonType: string):Promise<void>{
		let url = "";
		switch (buttonType){
			case "slidersButton":
				url = "/trees/1";
				break
			case "baumButton":
				url = "/trees/2";
				break
			case "lupeButton":
				url = "/trees/5";
				break
		}
		if (isOpen){
			if (window.location.pathname == url){
				await goto("/")
				isOpen = !isOpen
			}
			else{
				goto(url)
				isOpen = true;
			}
		}
		else{
			await goto(url)
			isOpen = true;
		}	
		
	}

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
	<footer class="z-[700] w-100 shrink-0 min-h-[7%] pt-3 pb-3
	 bg-white opacity-50 flex justify-around align-center">

			<button on:click={() => handleButtonbarClick("slidersButton")}><img src="/slidersButton.svg"/></button>
			<button on:click={() => handleButtonbarClick("baumButton")}><img src="/baumButton.svg" /></button>
			<button on:click={() => handleButtonbarClick("lupeButton")}><img src="/lupeButton.svg"/> </button>
			
	</footer>
</div>
