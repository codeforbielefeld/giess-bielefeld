<script lang="ts">
	import { goto } from '$app/navigation';

	$: isOpen = false;

	async function handleButtonbarClick(buttonType: string): Promise<void> {
		let url = '';
		switch (buttonType) {
			case 'slidersButton':
				url = '/trees/1';
				break;
			case 'baumButton':
				url = '/trees/2';
				break;
			case 'lupeButton':
				url = '/trees/5';
				break;
		}
		if (isOpen) {
			if (window.location.pathname == url) {
				await goto('/');
				isOpen = !isOpen;
			} else {
				goto(url);
				isOpen = true;
			}
		} else {
			await goto(url);
			isOpen = true;
		}
	}
</script>

<footer
	class="z-[700] flex shrink min-h-8 py-4 bg-white flex-row justify-around align-center"
>
	<button on:click={() => handleButtonbarClick('slidersButton')}
		><img src="/slidersButton.svg" class="w-8 h-8" /></button
	>
	<button on:click={() => handleButtonbarClick('baumButton')}
		><img src="/baumButton.svg" class="w-8 h-8" /></button
	>
	<button on:click={() => handleButtonbarClick('lupeButton')}
		><img src="/lupeButton.svg" class="w-8 h-8" />
	</button>
</footer>
